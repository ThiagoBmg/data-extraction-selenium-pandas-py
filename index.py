from selenium.webdriver import Firefox
import pandas as pd
import time

nomes = [] # responsavel por guardar os nomes 
valores = [] # responsavel por guardar os valores
centavoss = [] # responsavel por guardar os centavos
simbolos = [] # responsavel por guardar o simbolo da moeda

def main(): 
    try:
        driver = Firefox()
        driver.get('https://www.amazon.com.br/')
        time.sleep(3)
        driver.find_element_by_name('field-keywords').send_keys('iphone')
        time.sleep(3)
        driver.find_element_by_id('nav-search-submit-button').click()
        time.sleep(3)
        nome = driver.find_elements_by_class_name('a-size-base-plus.a-color-base.a-text-normal') # buscando os nomes dos produtos
        simbolo = driver.find_elements_by_class_name('a-price-symbol') # buscando o simbolo da moeda
        valor = driver.find_elements_by_class_name('a-price-whole') # buscando valor
        centavos = driver.find_elements_by_class_name('a-price-fraction') # buscando centavos 

        for n in valor:
            valores.append(n.text)
        for f in centavos:
            centavoss.append(f.text)
        for g in simbolo:
            simbolos.append(g.text) 
        for h in nome:
            nomes.append(h.text)
        driver.close()

        data = {'NOMES': nomes, 'MOEDA': simbolos ,'VALORES': valores, 'CENTAVOS': centavoss}
        dados  = pd.DataFrame.from_dict(data, orient='index')
        dados = dados.transpose()
        dados.to_excel('dados.xls', index=False)
    except Exception:
        print('Erro')
        driver.close()

main()