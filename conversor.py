import requests
from config import api_key

def obter_taxas_de_cambio(moeda_base):

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_base}"

    try:
        # Pedido para a API
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se tudo deu certo

        # Extrair os dados da resposta em formato JSON
        dados = resposta.json()

        # Retornar apenas o dicionário com as taxas de conversão
        return dados['conversion_rates']

    # Diferentes tipos de erro
    except requests.exceptions.HTTPError as err:
        print(f"Erro de HTTP: Verifique o código da moeda ou a sua chave da API. Detalhes: {err}")
        return None
    except requests.exceptions.ConnectionError as err:
        print(f"Erro de Conexão: Verifique a sua ligação à internet. Detalhes: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Ocorreu um erro inesperado: {err}")
        return None



if __name__ == "__main__":

    # a. Apresentação e recolha de dados do utilizador
    print("=" * 38)
    print("   Bem-vindo ao Conversor de Moedas   ")
    print("=" * 38)

    # Lista das moedas dispoíveis
    # As moedas ARS, LYD, SSP, SYP, VES, YER, ZWL apresentam alta volatilidades e diferenças em relação à taxas reais
    moedas_disponiveis = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]

    # Exibição da Lista
    linhas_formatadas = []
    linha_atual = []
    for moeda in moedas_disponiveis:
        linha_atual.append(moeda)
        if len(linha_atual) == 10:
            texto_da_linha = ", ".join(linha_atual)
            linhas_formatadas.append(texto_da_linha)
            linha_atual = []
    if linha_atual:
        texto_da_linha = ", ".join(linha_atual)
        linhas_formatadas.append(texto_da_linha)
    moedas_formatadas = '\n'.join(linhas_formatadas)

    print("Digite os códigos das moedas (ex: USD, BRL, EUR).")
    print("(Digite 'LISTA' a qualquer momento para ver todos os códigos disponíveis)")

    # Loop para garantir que o utilizador insere uma moeda de origem válida
    while True:
        moeda_origem = input("\nDigite a moeda de ORIGEM: ").upper()
        if moeda_origem == 'LISTA':
            print(f"\n{'-' * 14} Moedas Disponíveis {'-' * 15}\n{moedas_formatadas}\n{'-' * 49}")
            continue
        if moeda_origem in moedas_disponiveis:
            break
        print("Moeda inválida. Por favor, tente novamente ou digite 'LISTA'.")

    # Loop para garantir que o utilizador insere uma moeda de destino válida
    while True:
        moeda_destino = input("Digite a moeda de DESTINO: ").upper()
        if moeda_destino == 'LISTA':
            print(f"\n{'-' * 14} Moedas Disponíveis {'-' * 15}\n{moedas_formatadas}\n{'-' * 49}")
            continue
        if moeda_destino in moedas_disponiveis:
            break
        print("Moeda inválida. Por favor, tente novamente ou digite 'LISTA'.")

    valor_a_converter = float(input(f"Digite o valor em {moeda_origem} a ser convertido: "))
    print("\nA obter as taxas de câmbio em tempo real...")
    taxas = obter_taxas_de_cambio(moeda_origem)

    if taxas:
        taxa_de_conversao = taxas.get(moeda_destino)
        if taxa_de_conversao:
            valor_convertido = valor_a_converter * taxa_de_conversao
            print("\n" + "-" * 11, " RESULTADO ", "-" * 11)
            print(f"{valor_a_converter} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}")
            print("-" * 35)
        else:
            print(f"Erro: A moeda de destino '{moeda_destino}' não foi encontrada.")
    else:
        print("\nNão foi possível realizar a conversão. Verifique os erros acima.")

    # Valor que será convertido
    valor_a_converter = float(input(f"Digite o valor em {moeda_origem} a ser convertido: "))

    # b. Chamar a função para obter as taxas
    print("\nA obter as taxas de câmbio em tempo real...")
    taxas = obter_taxas_de_cambio(moeda_origem)

    # c. Calcular e mostrar o resultado
    if taxas:
        taxa_de_conversao = taxas.get(moeda_destino)
        if taxa_de_conversao:
            valor_convertido = valor_a_converter * taxa_de_conversao

            print("\n" + "-" * 11, " RESULTADO ", "-"*11)
            print(f"{valor_a_converter} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}")
            print("-" * 35)
        else:
            print(f"Erro: A moeda de destino '{moeda_destino}' não foi encontrada.")
    else:
        print("\nNão foi possível realizar a conversão. Verifique os erros acima.")