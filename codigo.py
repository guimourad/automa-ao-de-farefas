# passo a passo do projeto

# 1. Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time


pyautogui.PAUSE = 0.5
#pyautogui.click #clicar em algum lugar da tela
#pyautogui.write #escrever um texto
#pyautogui.press #pressionar 1 tecla do teclado

#combinaçao de teclas: pyautogui.hotkey('ctrl', 'c')

#abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')


link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# dar uma pausa um pouco maior (3 seg)
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=741, y=541)
pyautogui.write('mouradpython@gmail.com')

#escrever a senha
pyautogui.press('tab')
pyautogui.write('senha')

#cliclar no botao de logar
pyautogui.click(x=944, y=792)
time.sleep(5)
 

# 3. Importar a base de dados
#pandas
import pandas
tabela = pandas.read_csv('produtos (1).csv')

print(tabela)

# 4. Cadastrar um produto

#repetir esse processo para todos os itens da tabela

for linha in tabela.index:  

    #clicar no primeiro campo
    pyautogui.click(x=547, y=382)

    #codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab') 

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    # transformar nas colunas de numeros em string
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna:    #isna = informaçoes vazias
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') 
    pyautogui.scroll(5000)

# 5. Repetir o processo de cadastro até acabar

  
