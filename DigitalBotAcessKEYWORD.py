import undetected_chromedriver as uc
import random
import time
import pyautogui

if __name__ == '__main__':

    pais = int(input("SELECIONE A OPÇÃO DESEJADA: \n >> 1-Brasil \n >> 2-Singapura: \n >> "))
    acesso = int(input("Digite a quantidade de acessos: "))


    if pais == 1:
        print('###### UTILIZANDO IPS DO BRASIL ######')
        campanha = int(input("SELECIONE O NUMERO DA CAMPANHA DESEJADA: \n >> 1-Recuperar Ransomware \n >> 2- Recuperar Dados Encriptados \n >> 3-Recuperar Arquivos Encriptados \n >> 4-LockBit 3.0 \n >> 5-LockBit 2.0 \n >> 6-Recuperar Ransomware LockBit 2.0 \n >> 7-Recuperar Ransomware LockBit 3.0 \n >> 8-Recuperar RAID \n >> 9-Recuperar RAID 5 \n >> 10-Recuperar RAID 6 \n >> 11-Recuperar RAID 0 \n >> 12-Recuperar RAID 1 \n >> 13-Recuperar Sistemas RAID \n >> 14-Recuperação de dados RAID \n >> 15-Recuperação de Dados \n >>"))

        if campanha == 1:
            print('Utilizando a Palavra-chave: Recuperar Ransomware')

            i = 0
            while i < acesso:
                lista = [
                'IPS BRASILEIROS',
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

                driver.get("https://google.com/")
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Recuperar Ransomware')
                pyautogui.press('enter')
                time.sleep(5)

                driver.find_element_by_xpath('//*[@id="rso"]/div[5]/div/div[1]/div/a/h3').click()
                time.sleep(30) 

                pyautogui.scroll(-1000)
                time.sleep(5)

                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(15)
                i = i + 1

        if campanha == 2:
            i = 0
            while i < acesso:
                lista = [
                'IPS BRASILeirus',
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

                driver.get("https://google.com/")
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(keyword)
                pyautogui.press('enter')
                time.sleep(5)

                driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()
                time.sleep(30) 

                pyautogui.scroll(-1000)
                time.sleep(5)

                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(15)

                i = i + 1

        if keyword == 'Recuperar Arquivos Encriptados':
            i = 0
            while i < acesso:
                lista = [
                'IPS BRASIL',
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

                driver.get("https://google.com/")
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(keybr)
                pyautogui.press('enter')
                time.sleep(5)

                driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()
                time.sleep(30) 

                pyautogui.scroll(-1000)
                time.sleep(5)

                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(15)

                print('FEITO')
                i = i + 1


    elif pais == 2:
        print('Utilizando IPs de Singapura')
