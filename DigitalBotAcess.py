import undetected_chromedriver as uc
import random
import time
import pyautogui

if __name__ == '__main__':

    opcao = int(input("SELECIONE A OPÇÃO DESEJADA: \n >> 1-Brasil \n >> 2-Singapura: "))
    acesso = int(input("Digite a quantidade de acessos: "))

    if opcao == 1:
        print('Utilizando IPs do Brasil')

        keybr = [
        'Recuperar Pen Drive',
        'Recuperar PenDrive Digital Recovery',
        'Recuperar Ransomware',
        'Recuperar Banco de Dados',
        'Recuperar Fitas Magneticas',
        'Recuperar Storage',
        ]

        keyword = random.choice(keybr)
        print('Utilizando a Palavra-chave: {}'.format(keyword))

        if keyword == 'Recuperar Pen Drive':
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

                driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(keybr)
                pyautogui.press('enter')
                time.sleep(5)

                driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3').click()
                time.sleep(30) 

                pyautogui.scroll(-1000)
                time.sleep(5)

                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(15)
                i = i + 1

        if keyword == 'Recuperar PenDrive Digital Recovery':
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

                i = i + 1

        if keyword == 'Recuperar Ransomware':
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


    elif opcao == 2:
        print('Utilizando IPs de Singapura')
