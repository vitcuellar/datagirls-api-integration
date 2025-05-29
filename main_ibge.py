import requests 
import json 
import pandas as pd 
import pprint 


url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

query_params = {
    'id_para' : 15, #Pará
    'id_sao_paulo' : 35  #São Paulo
}

request_url = f"{url}/{query_params['id_para']}|{query_params['id_sao_paulo']}"

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df = df[['id', 'sigla', 'nome']]
    df.columns = ['ID', 'Sigla', 'Nome']
    
    #Salvando dataframe em arquivo csv 
    df.to_csv('estados_brasil.csv', index=False)
    
    # Print do Dataframe
    pprint.pprint(df.to_dict(orient='records'))
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)

