import undetected_chromedriver as uc
import random
import time
import pyautogui

if __name__ == '__main__':

    pais = int(input("SELECIONE A OPÇÃO DESEJADA: \n >> 1-Brasil \n >> 2-Singapura: \n >> "))
    acesso = int(input("Digite a quantidade de acessos: "))
    opcao = int(input('Digite 1 para paginas de Single e 2 para Datacenter \n >>'))

    #ESCOLHA DE PAIS
    if pais == 1:
        print('-----Utilizando IPs do Brasil-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            links = [
            'https://digitalrecovery.com/pt-br/recuperar-hd-notebook/',
            'https://digitalrecovery.com/pt-br/recuperar-hd-externo/',
            'https://digitalrecovery.com/pt-br/recuperacao-de-pen-drive/',
            'https://digitalrecovery.com/pt-br/recuperar-cartao-de-memoria/',
            ]

            url = random.choice(links)
            print('Acessando a URL: {}'.format(url))
            
            #Tempo Aleatorio
            randomtimeone = random.randint(900, 1900)
            timing = randomtimeone - (randomtimeone * 2)

            randomtimetwo = random.randint(500, 1800)
            timing2 = randomtimetwo - (randomtimetwo * 2)

            #Sleep Aleatorio
            sleeping = random.randint(10, 15)
            sleeping2 = random.randint(10, 20)
            sleeping3 = random.randint(10, 25)

            i = 0
            while i < acesso:
                driver = uc.Chrome()

                driver.get(url)
                time.sleep(sleeping)

                pyautogui.scroll(timing)
                time.sleep(sleeping2)

                pyautogui.scroll(timing)
                time.sleep(sleeping3)

                pyautogui.scroll(timing2)
                time.sleep(sleeping2)

                #CLIQUE NA LOGO
                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(sleeping3)
                pyautogui.scroll(timing)
                i = i + 1
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:
            links = [
            'https://digitalrecovery.com/pt-br/recuperar-ransomware/',
            'https://digitalrecovery.com/pt-br/recuperar-raid/',
            'https://digitalrecovery.com/pt-br/recuperar-storage-nas-das-san/',
            'https://digitalrecovery.com/pt-br/recuperar-banco-de-dados/',
            'https://digitalrecovery.com/pt-br/recuperar-maquina-virtual/',
            'https://digitalrecovery.com/pt-br/recuperar-fitas-magneticas/',
            ]
            
            #ESCOLHA DE URL ALEATORIA
            url = random.choice(links)
            print('Acessando a URL: {}'.format(url))
            
            #TEMPO ALEATORIO
            randomtimeone = random.randint(900, 1900)
            timing = randomtimeone - (randomtimeone * 2)

            randomtimetwo = random.randint(500, 1800)
            timing2 = randomtimetwo - (randomtimetwo * 2)

            #SLEEP ALEATORIO
            sleeping = random.randint(10, 15)
            sleeping2 = random.randint(10, 20)
            sleeping3 = random.randint(10, 25)

            i = 0
            while i < acesso:
                driver = uc.Chrome()

                driver.get(url)
                time.sleep(sleeping)

                pyautogui.scroll(timing)
                time.sleep(sleeping2)

                pyautogui.scroll(timing)
                time.sleep(sleeping3)

                pyautogui.scroll(timing2)
                time.sleep(sleeping2)

                #CLIQUE NA LOGO
                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(sleeping3)
                pyautogui.scroll(timing)
                i = i + 1

    
    elif pais == 2:
        print('Utilizando IPs de Singapura')

    #ESCOLHA DE PAIS
    elif pais == 3:
        print('-----Utilizando IPs do EUA-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE nos Estados Unidos.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:
            links = [
            'https://digitalrecovery.com/en/ransomware-recovery/',
            'https://digitalrecovery.com/en/recover-raid/',
            'https://digitalrecovery.com/en/recover-database/',
            'https://digitalrecovery.com/en/recover-storage-nas-das-san/',
            'https://digitalrecovery.com/en/recover-virtual-machine/',
            'https://digitalrecovery.com/en/recover-magnetic-tapes/',
            ]
            
            #ESCOLHA DE URL ALEATORIA
            url = random.choice(links)
            print('Acessando a URL: {}'.format(url))
            
            #TEMPO ALEATORIO
            randomtimeone = random.randint(900, 1900)
            timing = randomtimeone - (randomtimeone * 2)

            randomtimetwo = random.randint(500, 1800)
            timing2 = randomtimetwo - (randomtimetwo * 2)

            #SLEEP ALEATORIO
            sleeping = random.randint(10, 15)
            sleeping2 = random.randint(10, 20)
            sleeping3 = random.randint(10, 25)

            i = 0
            while i < acesso:
                driver = uc.Chrome()

                driver.get(url)
                time.sleep(sleeping)

                pyautogui.scroll(timing)
                time.sleep(sleeping2)

                pyautogui.scroll(timing)
                time.sleep(sleeping3)

                pyautogui.scroll(timing2)
                time.sleep(sleeping2)

                #CLIQUE NA LOGO
                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(sleeping3)
                pyautogui.scroll(timing)
                i = i + 1