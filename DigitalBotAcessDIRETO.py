import undetected_chromedriver as uc
import random
import time
import pyautogui

if __name__ == '__main__':

    pais = int(input("SELECIONE A OPÇÃO DESEJADA: \n >> 1-Brasil \n >> 2-Italía: \n >> 3-Estados Unidos: \n >> 4-Alemanha \n >> 5-França \n >> 6-Reino Unido \n >> 7-Espanha \n >> 8-Portugal \n >> 9-Mundo para Mundo \n >>"))
    acesso = int(input("Digite a quantidade de acessos: "))
    opcao = int(input('Digite 1 para paginas de Single e 2 para Datacenter \n >>'))

    #ESCOLHA DE PAIS
    if pais == 1:
        print('-----Utilizando IPs do Brasil-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            i = 0
            while i < acesso:
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
                
                #LISTA DE PROXYS
                lista = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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
            
            i = 0
            while i < acesso:
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
                
                #LISTA DE PROXYS
                lista = [
                '44.206.234.75:13019',
                '44.206.234.75:13018',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

                #ENTRA NA URL
                driver.get(url)
                time.sleep(sleeping)

                #PRIMEIRO SCROLL
                pyautogui.scroll(timing)
                time.sleep(sleeping2)

                #SEGUNDO SCROLL
                pyautogui.scroll(timing)
                time.sleep(sleeping3)
                
                #TERCEIRO SCROLL
                pyautogui.scroll(timing2)
                time.sleep(sleeping2)

                #CLIQUE NA LOGO
                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(sleeping3)
                pyautogui.scroll(timing)
                i = i + 1

    
    elif pais == 2:
        print('Utilizando IPs da Italía')
    #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE na Italía.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                'https://digitalrecovery.com/it/recuperare-ransomware/',
                'https://digitalrecovery.com/it/recupero-raid/',
                'https://digitalrecovery.com/it/recuperare-storage-nas-das-san/',
                'https://digitalrecovery.com/it/recuperare-database/',
                'https://digitalrecovery.com/it/recuperare-virtual-machine/',
                'https://digitalrecovery.com/it/recuperare-nastri-magnetici/',
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

                #LISTA DE PROXYS
                lista = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar a Itália: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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


    #ESCOLHA DE PAIS
    elif pais == 3:
        print('-----Utilizando IPs do EUA-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE nos Estados Unidos.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
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

                #LISTA DE PROXYS
                listaEUA = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(listaEUA)
                print('Utilizando o IP: {} para Acessar o Estados Unidos: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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

    elif pais == 4:
        print('-----Utilizando IPs da Alemanha-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE na Alemenha.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                'https://www.digitalrecoverycenter.de/ransomware-datenrettung/',
                'https://www.digitalrecoverycenter.de/server-datenrettung-server-recovery/',
                'https://www.digitalrecoverycenter.de/raid-datenrettung/',
                'https://www.digitalrecoverycenter.de/datenrettung-virtualisierung/',
                'https://www.digitalrecoverycenter.de/datenbank-datenrettung/',
                'https://www.digitalrecoverycenter.de/datenrettung-von-tapes/',
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

                #LISTA DE PROXYS
                listaAL = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(listaAL)
                print('Utilizando o IP: {} para Acessar da Alemanha: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

                driver.get(url)
                time.sleep(sleeping)

                pyautogui.scroll(timing)
                time.sleep(sleeping2)

                pyautogui.scroll(timing)
                time.sleep(sleeping3)

                pyautogui.scroll(timing2)
                time.sleep(sleeping2)

                #CLIQUE NA LOGO
                driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div/div/span/a/img').click()
                time.sleep(sleeping3)
                pyautogui.scroll(timing)

    elif pais == 5:
        print('-----Utilizando IPs da França-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE na França.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                'https://digitalrecovery.com/fr/ransomware-recuperation/',
                'https://digitalrecovery.com/fr/recuperer-raid/',
                'https://digitalrecovery.com/fr/recuperation-stockage-nas-das-san/',
                'https://digitalrecovery.com/fr/recuperer-base-de-donnees/',
                'https://digitalrecovery.com/fr/recuperer-machine-virtuelle/',
                'https://digitalrecovery.com/fr/recuperer-bandes-magnetiques/',
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

                #LISTA DE PROXYS
                lista = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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

    elif pais == 6:
        print('-----Utilizando IPs de UK-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE no Reino Unido.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                'https://digitalrecovery.com/uk/ransomware-recovery/',
                'https://digitalrecovery.com/uk/recover-raid/',
                'https://digitalrecovery.com/uk/recover-storage-nas-das-san/',
                'https://digitalrecovery.com/uk/recover-database/',
                'https://digitalrecovery.com/uk/recover-virtual-machine/',
                'https://digitalrecovery.com/uk/recover-magnetic-tapes/',
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

                #LISTA DE PROXYS
                listaUK = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(listaUK)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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

    elif pais == 7:
        print('-----Utilizando IPs da Espanha-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE na Espanha.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                'https://digitalrecovery.com/es/recuperacion-ransomware/',
                'https://digitalrecovery.com/es/recuperacion-raid/',
                'https://digitalrecovery.com/es/recuperacion-storage-nas-das-san/',
                'https://digitalrecovery.com/es/recuperar-base-de-datos/',
                'https://digitalrecovery.com/es/recuperacion-maquinas-virtuales/',
                'https://digitalrecovery.com/es/recuperacion-cintas-magneticas/',
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

                #LISTA DE PROXYS
                lista = [
                '13.250.112.45:17985',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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

    elif pais == 8:



            print('-----Utilizando IPs de Portugal-----')
            
            #ESCOLHA DE SINGLE
            if opcao == 1:
                
                print('Não temos SINGLE em Portugal.')
            
            #ESCOLHA DE DATACENTER
            if opcao == 2:

                i = 0
                while i < acesso:
                    links = [
                    'https://digitalrecovery.com/pt/ransomware-recuperacao/',
                    'https://digitalrecovery.com/pt/recuperar-raid/',
                    'https://digitalrecovery.com/pt/recuperar-storage-nas-das-san/',
                    'https://digitalrecovery.com/pt/recupera-base-de-dados/',
                    'https://digitalrecovery.com/pt/recuperar-maquina-virtual/',
                    'https://digitalrecovery.com/pt/recuperar-fitas-magneticas/',
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

                    #LISTA DE PROXYS
                    lista = [
                    '13.250.112.45:17985',
                    ]

                    PROXY = random.choice(lista)
                    print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                    options = uc.ChromeOptions()
                    options.add_argument(f'--proxy-server={PROXY}')
                    driver = uc.Chrome(options=options)

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

    elif pais == 9:
        print('-----Utilizando IPs do Mundo para acessar pagina do mundo todo-----')
        
        #ESCOLHA DE SINGLE
        if opcao == 1:
            
            print('Não temos SINGLE no resto do mundo.')
        
        #ESCOLHA DE DATACENTER
        if opcao == 2:

            i = 0
            while i < acesso:
                links = [
                    'https://digitalrecovery.com/it/recuperare-ransomware/',
                    'https://digitalrecovery.com/it/recupero-raid/',
                    'https://digitalrecovery.com/it/recuperare-storage-nas-das-san/',
                    'https://digitalrecovery.com/it/recuperare-database/',
                    'https://digitalrecovery.com/it/recuperare-virtual-machine/',
                    'https://digitalrecovery.com/it/recuperare-nastri-magnetici/',
                    'https://digitalrecovery.com/en/ransomware-recovery/',
                    'https://digitalrecovery.com/en/recover-raid/',
                    'https://digitalrecovery.com/en/recover-database/',
                    'https://digitalrecovery.com/en/recover-storage-nas-das-san/',
                    'https://digitalrecovery.com/en/recover-virtual-machine/',
                    'https://digitalrecovery.com/en/recover-magnetic-tapes/',
                    'https://digitalrecovery.com/fr/ransomware-recuperation/',
                    'https://digitalrecovery.com/fr/recuperer-raid/',
                    'https://digitalrecovery.com/fr/recuperation-stockage-nas-das-san/',
                    'https://digitalrecovery.com/fr/recuperer-base-de-donnees/',
                    'https://digitalrecovery.com/fr/recuperer-machine-virtuelle/',
                    'https://digitalrecovery.com/fr/recuperer-bandes-magnetiques/',
                    'https://digitalrecovery.com/uk/ransomware-recovery/',
                    'https://digitalrecovery.com/uk/recover-raid/',
                    'https://digitalrecovery.com/uk/recover-storage-nas-das-san/',
                    'https://digitalrecovery.com/uk/recover-database/',
                    'https://digitalrecovery.com/uk/recover-virtual-machine/',
                    'https://digitalrecovery.com/uk/recover-magnetic-tapes/',
                    'https://digitalrecovery.com/es/recuperacion-ransomware/',
                    'https://digitalrecovery.com/es/recuperacion-raid/',
                    'https://digitalrecovery.com/es/recuperacion-storage-nas-das-san/',
                    'https://digitalrecovery.com/es/recuperar-base-de-datos/',
                    'https://digitalrecovery.com/es/recuperacion-maquinas-virtuales/',
                    'https://digitalrecovery.com/es/recuperacion-cintas-magneticas/',
                    'https://digitalrecovery.com/pt/ransomware-recuperacao/',
                    'https://digitalrecovery.com/pt/recuperar-raid/',
                    'https://digitalrecovery.com/pt/recuperar-storage-nas-das-san/',
                    'https://digitalrecovery.com/pt/recupera-base-de-dados/',
                    'https://digitalrecovery.com/pt/recuperar-maquina-virtual/',
                    'https://digitalrecovery.com/pt/recuperar-fitas-magneticas/',
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

                #LISTA DE PROXYS
                lista = [
                '44.206.234.75:11109',
                '44.206.234.75:11113',
                '44.206.234.75:11111',
                '44.206.234.75:11115',
                '44.206.234.75:11114',
                '44.206.234.75:11110',
                '44.206.234.75:11116',
                '44.206.234.75:11112',
                '44.206.234.75:11108',
                '44.206.234.75:11107',
                '3.69.30.73:10744',
                '3.69.30.73:10751',
                '3.69.30.73:10743',
                '3.69.30.73:10747',
                '3.69.30.73:10742',
                '3.69.30.73:10750',
                '3.69.30.73:10746',
                '3.69.30.73:10745',
                '3.69.30.73:10748',
                '3.69.30.73:10749',
                '3.69.30.73:13938',
                '3.69.30.73:13942',
                '3.69.30.73:13944',
                '3.69.30.73:13945',
                '3.69.30.73:13941',
                '3.69.30.73:13936',
                '3.69.30.73:13943',
                '3.69.30.73:13940',
                '3.69.30.73:13939',
                '3.69.30.73:13937',
                '3.69.30.73:11643',
                '3.69.30.73:11639',
                '3.69.30.73:11648',
                '3.69.30.73:11647',
                '3.69.30.73:11642',
                '3.69.30.73:11640',
                '3.69.30.73:11646',
                '3.69.30.73:11641',
                '3.69.30.73:11645',
                '3.69.30.73:11644',
                '3.69.30.73:10289',
                '3.69.30.73:10296',
                '3.69.30.73:10294',
                '3.69.30.73:10288',
                '3.69.30.73:10293',
                '3.69.30.73:10291',
                '3.69.30.73:10297',
                '3.69.30.73:10290',
                '3.69.30.73:10295',
                '3.69.30.73:10292',
                ]

                PROXY = random.choice(lista)
                print('Utilizando o IP: {} para Acessar o Brasil: '.format(PROXY))
                options = uc.ChromeOptions()
                options.add_argument(f'--proxy-server={PROXY}')
                driver = uc.Chrome(options=options)

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
                pyautogui.hotkey('ctrl','w');

                i = i + 1