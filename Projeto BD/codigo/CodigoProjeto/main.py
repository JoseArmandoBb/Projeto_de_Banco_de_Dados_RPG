import time


from PyQt6 import uic, QtWidgets
import mysql.connector
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456789",
    database = "rpg"
)
try:
    def Cadastro():
        Tela_Cadastro.caixa_notificacao.setText("")
        #essa parte ESTA DANDO CERTO EBAAAAA
        Nome1 = Tela_Cadastro.Nome_Usuario.text()
        Nome2 = Tela_Cadastro.Repita_NomeUsuario.text()
        Senha1 = Tela_Cadastro.Senha.text()
        Senha2 = Tela_Cadastro.Repita_Senha.text()
        if(Senha1 == Senha2 and Nome1 == Nome2):
            try:
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO jogador (nome,senha) VALUES(%s,%s)"
                dados_registrar = (str(Nome1), str(Senha1))
                cursor.execute(comando_SQL, dados_registrar)
                banco.commit()
                Tela_Cadastro.caixa_notificacao.setText("Casdastro realizado com sucesso")
                time.sleep(3.0)
                Tela_Cadastro.Nome_Usuario.setText("")
                Tela_Cadastro.Repita_NomeUsuario.setText("")
                Tela_Cadastro.Senha.setText("")
                Tela_Cadastro.Repita_Senha.setText("")
            except mysql.Error as erro:
                print("erro ao inserir os dados" , erro)
                Tela_Cadastro.caixa_notificacao.setText("")

        else:
            Tela_Cadastro.caixa_notificacao.setText("Dados invalidos")


     #essa de baixo parte nao ta servindo para nada
    def AcessarLogin():
        Tela_login.Mensagem.setText("")
        Nome = Tela_login.line_Nome.text()
        Senha = int(Tela_login.line_Senha.text())
        try:
            if (Nome == 'admin' and Senha == 00000):
                Tela_login.close()
                Tela_Principal.show()
                Mostrar_Dados()
                Tela_login.line_Nome.setText("")
                Tela_login.line_Senha.setText("")
        except:
            print('erro no login do admin')

        else:
            try:
                global Senha_bd

                Tela_login.Mensagem.setText("")
                Nome = Tela_login.line_Nome.text()
                Senha = int(Tela_login.line_Senha.text())

                cursor = banco.cursor()
                try:
                    cursor.execute("SELECT senha FROM jogador WHERE nome = '{}'".format(Nome))
                    Senha_bd = cursor.fetchall()
                except:

                    print("Erro Ao validar o login")



                if (Senha == Senha_bd[0][0]):
                    Tela_login.close()
                    Tela_da_comunidade.show()
                    Mostrar_Dados_comunidade()
                    Tela_login.line_Nome.setText("")
                    Tela_login.line_Senha.setText("")



                else:
                    #aqui tira a imagem entao modifica a tela principal e coloca outra label


                    if(Senha != Senha_bd):
                        Tela_login.Mensagem.setText("Senha Errada")
                        Tela_login.line_Senha.setText("")



            except:

                    Tela_login.Mensagem.setText("Dados de login incorretos!")
                    Tela_login.line_Nome.setText("")
                    Tela_login.line_Senha.setText("")




    #essa parte esta dando errado porque estar adiconando sem o idPersonagem do primeiro
    def Cria_Personagem():
        try:
            #INSERIR PERSONAGEM
            id = Tela_CriarPersonagem.Id.text()
            Nome = Tela_CriarPersonagem.Nome_Personagem.text()
            Classe = Tela_CriarPersonagem.Classe.text()
            Raca = Tela_CriarPersonagem.Raca.text()
            idade = Tela_CriarPersonagem.idade.text()
            Descricao = Tela_CriarPersonagem.Descricao.text()
            Sexo = Tela_CriarPersonagem.Sexo.text()

            Dados_Personagem= (str(id),str(Nome),str(Raca),str(Classe),str(Descricao),str(idade),str(Sexo))

            #INSERIR FICHA
            vida = Tela_CriarPersonagem.Vida.text()
            ataque = Tela_CriarPersonagem.Ataque.text()
            defesa = Tela_CriarPersonagem.Defesa.text()
            inteligencia = Tela_CriarPersonagem.Inteligencia.text()
            carisma = Tela_CriarPersonagem.Carisma.text()
            forca = Tela_CriarPersonagem.Forca.text()
            velocidade = Tela_CriarPersonagem.velocidade.text()
            furtividade = Tela_CriarPersonagem.Furtividade.text()
            Dados_Ficha = (str(id),str(vida),str(ataque), str(defesa), str(inteligencia)
             , str(carisma), str(forca), str(velocidade), str(furtividade))

            #INSERIR NA BOLSA
            item1 = Tela_CriarPersonagem.Item1.text()
            item2 = Tela_CriarPersonagem.Item2.text()
            item3 = Tela_CriarPersonagem.Item3.text()
            item4 = Tela_CriarPersonagem.Item4.text()
            item5 = Tela_CriarPersonagem.Item5.text()
            item6 = Tela_CriarPersonagem.Item6.text()
            dinheiro = Tela_CriarPersonagem.Dinheiro.text()
            Dados_Bolsa = (str(id),str(item1), str(item2), str(item3), str(item4),
                           str(item5), str(item6), str(dinheiro))


            comando_Personagem = "INSERT INTO Personagem VALUES(%s,%s,%s,%s,%s,%s,%s)"
            comando_Ficha = "INSERT INTO ficha VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            comando_Bolsa = "INSERT INTO bolsa VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor = banco.cursor()
            cursor.execute(comando_Personagem, Dados_Personagem)
            cursor.execute(comando_Ficha, Dados_Ficha)
            cursor.execute(comando_Bolsa,Dados_Bolsa)
            banco.commit()
            Tela_Ficha_personagem.label_3.clicked.connect("Dados Salvos")
            print(Dados_Personagem, "\n", Dados_Ficha, "\n", Dados_Bolsa)
        except:
            print('erro ao criar personagem')

    # Fazer algo que limpe os dados depois que a pessoa apertar excluir. Essa parte estar a dar certo la no mysql
    def Mostrar_Dados():
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM Personagem"
            cursor.execute(comando_SQL)
            Dados_Lidos = cursor.fetchall()
            Tela_Principal.tableWidget.setRowCount(len(Dados_Lidos))
            Tela_Principal.tableWidget.setColumnCount(7)
            for i in range(0 , len(Dados_Lidos)):
                for j in range(0,7):
                    Tela_Principal.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(Dados_Lidos[i][j])))

        except:
            print("dados mostrados com algum erro")

        try:
            cursor = banco.cursor()
            '''comando_SQL = "SELECT * FROM ficha"'''
            comando_SQL = "select p.nome, f.vida, f.ataque, f.defesa, f.inteligencia, f.carisma, f.forca, f.velocidade, f.furtividade from ficha f inner join personagem p on p.idPersonagem = f.idPersonagem;"
            cursor.execute(comando_SQL)
            Dados_Lidos_ficha = cursor.fetchall()
            Tela_Principal.tableWidget_2.setRowCount(len(Dados_Lidos_ficha))
            Tela_Principal.tableWidget_2.setColumnCount(9)
            for i in range(0, len(Dados_Lidos_ficha)):
                for j in range(0, 9):
                    Tela_Principal.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(Dados_Lidos_ficha[i][j])))

            banco.commit()

        except:
            print("dados incorretos do personagem")

        try:
            cursor = banco.cursor()
            '''comando_SQL = "SELECT * FROM bolsa"'''
            comando_SQL = "select p.nome, b.item1, b.item2, b.item3, b.item4 , b.item5, b.item6, b.dinheiro from bolsa b inner join personagem p on p.idPersonagem = b.idPersonagem;"
            cursor.execute(comando_SQL)
            Dados_Lidos_bolsa = cursor.fetchall()
            Tela_Principal.tableWidget_3.setRowCount(len(Dados_Lidos_bolsa))
            Tela_Principal.tableWidget_3.setColumnCount(8)
            for i in range(0, len(Dados_Lidos_bolsa)):
                for j in range(0, 8):
                    Tela_Principal.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(Dados_Lidos_bolsa[i][j])))
        except:
            print("dados incorretos da bolsa")

    def Mostrar_Dados_comunidade():
        try:
            cursor = banco.cursor()
            comando_SQL = "SELECT * FROM Personagem"
            cursor.execute(comando_SQL)
            Dados_Lidos = cursor.fetchall()
            Tela_da_comunidade.tableWidget.setRowCount(len(Dados_Lidos))
            Tela_da_comunidade.tableWidget.setColumnCount(7)
            for i in range(0 , len(Dados_Lidos)):
                for j in range(0,7):
                    Tela_da_comunidade.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(Dados_Lidos[i][j])))

        except:
            print("dados da comunidade mostrados com algum erro")

        try:
            cursor = banco.cursor()
            '''comando_SQL = "SELECT * FROM ficha"'''
            comando_SQL = "select p.nome, f.vida, f.ataque, f.defesa, f.inteligencia, f.carisma, f.forca, f.velocidade, f.furtividade from ficha f inner join personagem p on p.idPersonagem = f.idPersonagem;"
            cursor.execute(comando_SQL)
            Dados_Lidos_ficha = cursor.fetchall()
            Tela_da_comunidade.tableWidget_2.setRowCount(len(Dados_Lidos_ficha))
            Tela_da_comunidade.tableWidget_2.setColumnCount(9)
            for i in range(0, len(Dados_Lidos_ficha)):
                for j in range(0, 9):
                    Tela_da_comunidade.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(Dados_Lidos_ficha[i][j])))

            banco.commit()

        except:
            print("dados incorretos do ficha da comunidade")

        try:
            cursor = banco.cursor()
            '''comando_SQL = "SELECT * FROM bolsa"'''
            comando_SQL = "select p.nome, b.item1, b.item2, b.item3, b.item4 , b.item5, b.item6, b.dinheiro from bolsa b inner join personagem p on p.idPersonagem = b.idPersonagem;"
            cursor.execute(comando_SQL)
            Dados_Lidos_bolsa = cursor.fetchall()
            Tela_da_comunidade.tableWidget_3.setRowCount(len(Dados_Lidos_bolsa))
            Tela_da_comunidade.tableWidget_3.setColumnCount(8)
            for i in range(0, len(Dados_Lidos_bolsa)):
                for j in range(0, 8):
                    Tela_da_comunidade.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(Dados_Lidos_bolsa[i][j])))
        except:
            print("dados incorretos da bolsa da comunidade")

    def Excluir_Dados():
        try:
            linha = Tela_Principal.tableWidget.currentRow()
            Tela_Principal.tableWidget.removeRow(linha)
            Tela_Principal.tableWidget_2.removeRow(linha)
            Tela_Principal.tableWidget_3.removeRow(linha)
            

            cursor = banco.cursor()
            cursor.execute("SELECT idPersonagem FROM Personagem")
            DADOS = cursor.fetchall()
            IdValor = DADOS[linha][0]
            cursor.execute("DELETE FROM Personagem WHERE idPersonagem="+str(IdValor))
            banco.commit()
            Tela_excluir_personagem.show()
            Tela_excluir_personagem.mensagem.setText("!!EXCLUIDO COM SUCESSO!!")



        except:
                print('erro ao excluir')

    Id_do_personagem = 0
    def Mostrar_Dados_Ficha():
        try:
            global Id_do_personagem
            linha = Tela_Principal.tableWidget.currentRow()
            cursor = banco.cursor()
            cursor.execute("SELECT idPersonagem FROM Personagem")
            DADOS = cursor.fetchall()
            IdValor = DADOS[linha][0]
            Id_do_personagem = IdValor
            cursor.execute("SELECT * FROM Personagem WHERE idPersonagem=" + str(IdValor))
            Dados_Personagem = cursor.fetchall()
            Tela_Ficha_personagem.show()
            Tela_Ficha_personagem.Id_personagem.setText(str(Dados_Personagem[0][0]))
            Tela_Ficha_personagem.nome_Personagem.setText(str(Dados_Personagem[0][1]))
            Tela_Ficha_personagem.raca.setText(str(Dados_Personagem[0][2]))
            Tela_Ficha_personagem.classe.setText(str(Dados_Personagem[0][3]))
            Tela_Ficha_personagem.descricao.setText(str(Dados_Personagem[0][4]))
            Tela_Ficha_personagem.idade_3.setText(str(Dados_Personagem[0][5]))
            Tela_Ficha_personagem.Sexo.setText(str(Dados_Personagem[0][6]))
            print(Dados_Personagem)
        except:
            print('erro ao mostrar dados da ficha')
    Id_do_personagem_Status = 0
    def Mostrar_Dados_Status():
        try:
            global Id_do_personagem_Status
            linha = Tela_Principal.tableWidget_2.currentRow()
            cursor = banco.cursor()
            cursor.execute("SELECT idPersonagem FROM ficha")
            DADOS = cursor.fetchall()
            IdValor = DADOS[linha][0]
            Id_do_personagem_Status = IdValor
            cursor.execute("SELECT * FROM ficha WHERE idPersonagem=" + str(IdValor))
            Dados_ficha = cursor.fetchall()
            Tela_Status_Personagem.show()
            Tela_Status_Personagem.Id_personagem.setText(str(Dados_ficha[0][0]))
            Tela_Status_Personagem.Vida.setText(str(Dados_ficha[0][1]))
            Tela_Status_Personagem.Ataque.setText(str(Dados_ficha[0][2]))
            Tela_Status_Personagem.Defesa.setText(str(Dados_ficha[0][3]))
            Tela_Status_Personagem.Inteligencia.setText(str(Dados_ficha[0][4]))
            Tela_Status_Personagem.Carisma.setText(str(Dados_ficha[0][5]))
            Tela_Status_Personagem.Forca.setText(str(Dados_ficha[0][6]))
            Tela_Status_Personagem.velocidade.setText(str(Dados_ficha[0][7]))
            Tela_Status_Personagem.Furtividade.setText(str(Dados_ficha[0][8]))

        except:
            print('erro ao mostrar dados do status')

    Id_do_personagem_Bolsa = 0
    def Mostrar_Dados_Bolsa():
        try:
            global Id_do_personagem_Bolsa
            linha = Tela_Principal.tableWidget_3.currentRow()
            cursor = banco.cursor()
            cursor.execute("SELECT idPersonagem FROM Bolsa")
            DADOS = cursor.fetchall()
            IdValor = DADOS[linha][0]
            Id_do_personagem_Bolsa = IdValor
            cursor.execute("SELECT * FROM Bolsa WHERE idPersonagem=" + str(IdValor))
            Dados_ficha = cursor.fetchall()
            Tela_Bolsa_Personagem.show()
            Tela_Bolsa_Personagem.Id_personagem.setText(str(Dados_ficha[0][0]))
            Tela_Bolsa_Personagem.Item1.setText(str(Dados_ficha[0][1]))
            Tela_Bolsa_Personagem.Item2.setText(str(Dados_ficha[0][2]))
            Tela_Bolsa_Personagem.Item3.setText(str(Dados_ficha[0][3]))
            Tela_Bolsa_Personagem.Item4.setText(str(Dados_ficha[0][4]))
            Tela_Bolsa_Personagem.Item5.setText(str(Dados_ficha[0][5]))
            Tela_Bolsa_Personagem.Item6.setText(str(Dados_ficha[0][6]))
            Tela_Bolsa_Personagem.Dinheiro.setText(str(Dados_ficha[0][7]))
        except:
            print('erro ao mostrar dados da bolsa na parte de editar')

    def Atualizar_dados_Personagem():
        try:
            global Id_do_personagem
            Nome = Tela_Ficha_personagem.nome_Personagem.text()
            Classe = Tela_Ficha_personagem.classe.text()
            Raca = Tela_Ficha_personagem.raca.text()
            idade = Tela_Ficha_personagem.idade_3.text()
            Descricao = Tela_Ficha_personagem.descricao.text()
            Sexo = Tela_Ficha_personagem.Sexo.text()

            cursor = banco.cursor()
            cursor.execute("UPDATE Personagem SET nome = '{}', Raca = '{}', Classe = '{}', Descricao = '{}', idade = '{}', sexo = '{}' WHERE idPersonagem = {}".format(Nome,Raca,Classe,Descricao,idade,Sexo,Id_do_personagem))
            banco.commit()
            print(Id_do_personagem)
        except:
            print('erro ao atualizar dados do personagem')

    def Atualizar_Dados_Status():
        try:
            global Id_do_personagem_Status
            vida = Tela_Status_Personagem.Vida.text()
            ataque = Tela_Status_Personagem.Ataque.text()
            defesa = Tela_Status_Personagem.Defesa.text()
            inteligencia = Tela_Status_Personagem.Inteligencia.text()
            carisma = Tela_Status_Personagem.Carisma.text()
            forca = Tela_Status_Personagem.Forca.text()
            velocidade = Tela_Status_Personagem.velocidade.text()
            furtividade = Tela_Status_Personagem.Furtividade.text()

            cursor = banco.cursor()
            cursor.execute("UPDATE ficha SET vida = '{}', ataque = '{}', defesa = '{}', inteligencia = '{}', carisma = '{}', forca = '{}', velocidade = '{}', furtividade = '{}' WHERE idPersonagem = {}".format(vida, ataque, defesa, inteligencia, carisma, forca, velocidade, furtividade, Id_do_personagem_Status))
            banco.commit()
            print(Id_do_personagem_Status)
        except:
            print('erro ao atualizar status')


    def Atualizar_Dados_Bolsa():
        try:
            global Id_do_personagem_Bolsa
            item1 = Tela_Bolsa_Personagem.Item1.text()
            item2 = Tela_Bolsa_Personagem.Item2.text()
            item3 = Tela_Bolsa_Personagem.Item3.text()
            item4 = Tela_Bolsa_Personagem.Item4.text()
            item5 = Tela_Bolsa_Personagem.Item5.text()
            item6 = Tela_Bolsa_Personagem.Item6.text()
            dinheiro = Tela_Bolsa_Personagem.Dinheiro.text()

            cursor = banco.cursor()
            cursor.execute("UPDATE Bolsa SET item1 = '{}', item2 = '{}', item3 = '{}', item4 = '{}', item5 = '{}', item6 = '{}', dinheiro = '{}' WHERE idPersonagem = {}".format(item1, item2, item3, item4, item5, item6, dinheiro, Id_do_personagem_Bolsa))
            banco.commit()
            print(Id_do_personagem_Status)
        except:
            print('erro ao atualizar ficha')


    #comandos para abrir e fechar telas
    def Abre_Tela_Cadastro():
        try:
            Tela_Cadastro.show()
        except:
            print('erro ao abrir tela de cadastro')

    def Sair():
        try:
            Tela_Principal.close()
            Tela_login.show()
        except:
            print('erro ao sair da tela principal')

    def Cancelar_Cadastro():
        try:
            Tela_Cadastro.close()
        except:
            print('erro ao fechar tela cadrasto')

    def Abrir_TelaCriarPersonagem():
        try:
            Tela_CriarPersonagem.show()
        except:
            print('erro ao abrir tela de personagem')

    def Sair_Tela_Criacao_Personagem():
        try:
            Tela_CriarPersonagem.Id.setText("")
            Tela_CriarPersonagem.Nome_Personagem.setText("")
            Tela_CriarPersonagem.Classe.setText("")
            Tela_CriarPersonagem.Raca.setText("")
            Tela_CriarPersonagem.idade.setText("")
            Tela_CriarPersonagem.Descricao.setText("")
            # status
            Tela_CriarPersonagem.Vida.setText("")
            Tela_CriarPersonagem.Ataque.setText("")
            Tela_CriarPersonagem.Defesa.setText("")
            Tela_CriarPersonagem.Inteligencia.setText("")
            Tela_CriarPersonagem.Carisma.setText("")
            Tela_CriarPersonagem.Forca.setText("")
            Tela_CriarPersonagem.velocidade.setText("")
            Tela_CriarPersonagem.Furtividade.setText("")
            # bolsa
            Tela_CriarPersonagem.Item1.setText("")
            Tela_CriarPersonagem.Item2.setText("")
            Tela_CriarPersonagem.Item3.setText("")
            Tela_CriarPersonagem.Item4.setText("")
            Tela_CriarPersonagem.Item5.setText("")
            Tela_CriarPersonagem.Item6.setText("")
            Tela_CriarPersonagem.Dinheiro.setText("")
            Mostrar_Dados()
            Tela_CriarPersonagem.close()
            Tela_Principal.show()
        except:
            print('erro ao sair da tela de personagem')

    def abrir_tela_exclusao():
        try:
            Tela_excluir_personagem.show()
        except:
            print('erro ao abrir tela de exclusao')
    def Fechar_Tela_excluir():
        try:
            Tela_excluir_personagem.close()
        except:
            print('erroa ao fechar a tela de esclusao')

    def Sair_Tela_Comunidade():
        Tela_da_comunidade.close()
        Tela_login.show()


    #le as telas
    app = QtWidgets.QApplication([])
    Tela_login = uic.loadUi("login.ui")
    Tela_Cadastro = uic.loadUi("Fazer_Cadastro.ui")
    Tela_Principal = uic.loadUi("Tela_inicial.ui")
    Tela_CriarPersonagem = uic.loadUi("Criar_Personagem.ui")
    Tela_Ficha_personagem = uic.loadUi("Tela_Ficha_personagem.ui")
    Tela_Status_Personagem = uic.loadUi("Status_Personagem.ui")
    Tela_Bolsa_Personagem = uic.loadUi("Bolsa_Personagem.ui")
    tela_teste = uic.loadUi("Teste.ui")
    Tela_excluir_personagem = uic.loadUi("Excluir_personagem.ui")
    Tela_da_comunidade = uic.loadUi("Tela_Comunidade.ui")


    #comando dos botoes da tela de login
    Tela_login.botao_registrar.clicked.connect(Abre_Tela_Cadastro)
    Tela_login.botao_acessar.clicked.connect(AcessarLogin)
    Tela_login.botao_acessar.clicked.connect(Mostrar_Dados)

    #comandos dos botoes da tela de cadastro
    Tela_Cadastro.Salvar.clicked.connect(Cadastro)
    Tela_Cadastro.Cancelar.clicked.connect(Cancelar_Cadastro)

    #comandos dos botoes da tela princinpal
    Tela_Principal.Sair.clicked.connect(Sair)
    Tela_Principal.Mostrar.clicked.connect(Mostrar_Dados)
    Tela_Principal.Excluir.clicked.connect(Excluir_Dados)
    Tela_Principal.Criar.clicked.connect(Abrir_TelaCriarPersonagem)
    Tela_Principal.Editar_personagem.clicked.connect(Mostrar_Dados_Ficha)
    Tela_Principal.Editar_Status.clicked.connect(Mostrar_Dados_Status)
    Tela_Principal.Editar_bolsa.clicked.connect(Mostrar_Dados_Bolsa)

    #Comandos dos botoes da tela de criacao de persoagens
    Tela_CriarPersonagem.Salva.clicked.connect(Cria_Personagem)

    #Comandos das telas de edicao
    Tela_Ficha_personagem.Salvar.clicked.connect(Atualizar_dados_Personagem)
    Tela_Status_Personagem.Salvar.clicked.connect(Atualizar_Dados_Status)
    Tela_Bolsa_Personagem.Salvar.clicked.connect(Atualizar_Dados_Bolsa)

    #Comandos das telas da comunidade
    Tela_da_comunidade.Mostrar.clicked.connect(Mostrar_Dados_comunidade)
    Tela_da_comunidade.Sair.clicked.connect(Sair_Tela_Comunidade)
    Tela_da_comunidade.Criar.clicked.connect(Abrir_TelaCriarPersonagem)

    Tela_login.show()
    '''Tela_CriarPersonagem.show()'''
    '''Tela_Principal.show()'''
    '''Tela_excluir_personagem.show()'''
    '''Tela_da_comunidade.show()'''
    app.exec()
except:
 print('erro no codigo todo')