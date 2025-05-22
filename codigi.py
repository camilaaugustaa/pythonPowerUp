import pyautogui
import pandas as pd
import time

tabela =pd.read_csv("produtos.csv")
print(tabela)

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Google")   
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter") 

time.sleep(5)

pyautogui.click(x=868, y=466)
pyautogui.write("camila.dev@outlook.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=958, y=675)

time.sleep(5)

for linha in tabela.index:
    pyautogui.click(x=776, y=311)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab") 
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")   
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab") 
    obs=tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    