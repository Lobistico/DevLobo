import time
import function
import pyautogui
print("Ei... Testando... ")
time.sleep(1)
print("1...2...3...")
time.sleep(1)
try:
    name = function.name
    function.namer()
    function.escolher(name)
    time.sleep(2)
    if function.mochila[0] == 'Verdade':
        function.escolher2(name)
        if function.mochila[1] == 'Quantidade':
            print('Estou aqui')
            pyautogui.alert="Estou desenvolvendo aqui"

    elif function.mochila[0] == 'Mentira':
        print('Estou desenvolvendo a mentira')
        pyautogui.alert="Na verdade é tudo um sonho, e você acordou"
    else:
        print('Estou desenvolvendo ainda')

except:
    pass