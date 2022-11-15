import requests


def get_valor_btc_atual() -> float:
    """Retorna o valor de compra atualizado do bitcoin

    Returns:
        float: Valor de compra atualizado do bitcoin
    """

    response = requests.get(
        "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
    )

    if response.status_code == 200:
        valor_btc = response.json()
        valor = str(round(float(valor_btc["BTCBRL"]["bid"]) * 1000, 2))
        return valor.replace('.', ',')

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )


def get_valor_dolar_atual() -> float:
    """Retorna o valor de compra atualizado do dólar

    Returns:
        float: Valor de compra atualizado do dólar
    """

    response = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL"
    )

    if response.status_code == 200:
        valor_btc = response.json()
        valor = str(round(float(valor_btc["USDBRL"]["bid"]), 2))
        return valor.replace('.', ',')

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )
