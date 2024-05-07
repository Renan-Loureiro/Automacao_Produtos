import pyautogui
from time import sleep
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

sleep(3)

pyautogui.click(x=729, y=357)
pyautogui.write('pythonimpressionador@gmail.com')

pyautogui.press('tab')
pyautogui.write('sua senha aqui')

pyautogui.press('tab')
pyautogui.press('enter')

sleep(1)

import pandas as pd

tabela = pd.read_csv('produtos.csv')

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=740, y=239)

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(1500)