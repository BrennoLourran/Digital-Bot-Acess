import undetected_chromedriver as uc
import random
import time
import pyautogui

if __name__ == '__main__':

    pais = int(input("SELECIONE A OPÇÃO DESEJADA: \n >> 1-Brasil \n >> 2-Singapura: "))
    acesso = int(input("Digite a quantidade de acessos: "))
    opcao = int(input('Digite 1 para paginas de Single e 2 para Datacenter \n >>'))


    if pais == 1:
        print('-----Utilizando IPs do Brasil-----')

        if opcao == 1:
            links = [
            'https://digitalrecovery.com/pt-br/recuperar-hd-notebook/',
            'https://digitalrecovery.com/pt-br/recuperar-hd-externo/',
            'https://digitalrecovery.com/pt-br/recuperacao-de-pen-drive/',
            'https://digitalrecovery.com/pt-br/recuperar-cartao-de-memoria/',
            ]

            url = random.choice(links)
            print('Acessando a URL: {}'.format(url))

        
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

                driver.get(url)
                time.sleep(5)
                
                driver.find_element_by_xpath('//*[@id="rso"]/div[5]/div/div[1]/div/a/h3').click()
                time.sleep(30) 

                pyautogui.scroll(-1000)
                time.sleep(5)

                driver.find_element_by_xpath('/html/body/div[1]/header[1]/div/div/div/section/div/div[1]/div/div/div/a/img').click()
                time.sleep(15)
                i = i + 1


    elif pais == 2:
        print('Utilizando IPs de Singapura')
