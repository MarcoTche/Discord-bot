import requests
import locale


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
        valor = round(float(valor_btc["BTCBRL"]["bid"]) * 1000, 2)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(valor, grouping=True, symbol=None)

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
        valor = round(float(valor_btc["USDBRL"]["bid"]), 2)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(valor, grouping=True, symbol=None)

    raise Exception(
        "Ocorreu um erro inesperado!!! Status Code: {}".format(
            response.status_code)
    )
