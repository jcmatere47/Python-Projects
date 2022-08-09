import requests
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/ ')
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep(01001000'')