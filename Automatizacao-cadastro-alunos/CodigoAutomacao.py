#Importar as bibliotecas necessárias
import pandas as pd
import pyautogui
import time


#Iniciando a automação
pyautogui.PAUSE = 0.5
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link 
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login
# selecionar o campo de login
pyautogui.click(x=519, y=260)
# escrever o usuário na posição capturada
pyautogui.write("admin")
pyautogui.press("tab") # passando para o próximo campo
#escrever a senha na posição capturada
pyautogui.write("SimplificaPython")
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("enter")

# Passo 3: Importar a base de alunos para cadastrar
tabela = pd.read_csv("alunos.csv")
time.sleep(2)

# Passo 4: Cadastrar aluno
for linha in tabela.index:
    
    # clicar no campo de aluno
    pyautogui.click(x=481, y=334)
    # pegar da tabela o valor do campo que quer preencher
    nome = tabela.loc[linha, "Nome"]
    # preencher o campo
    pyautogui.write(str(nome))
    # passar para o proximo campo
    pyautogui.press("tab")

    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(endereco)
    pyautogui.press("tab")

    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")

    time.sleep(1)
    pyautogui.press("enter") # cadastra o aluno (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
    