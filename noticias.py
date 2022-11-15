import requests
import re


def ultimas_noticias_uol() -> list:
    """Retorna o título das últimas notícias do UOL

    Returns:
        list: lista com o título das últimas notícias do UOL
    """

    url_uol = "https://noticias.uol.com.br/ultimas/"

    html_uol = requests.get(url_uol).text

    noticias_uol = re.findall(
        r'<h3 class="thumb-title title-xsmall title-lg-small"[^>]*>(.*?)</h3>', html_uol
    )

    retorno = "-----------------------------------NOTÍCIAS UOL-----------------------------------\n\n"
    for noticia in noticias_uol:
        retorno += f"{noticia}\n"
        
    return retorno


def ultimas_noticias_g1() -> list:
    """Retorna o título das últimas notícias do G1

    Returns:
        list: lista com o título das últimas notícias do G1
    """

    url_g1 = "https://g1.globo.com/"

    html_g1 = requests.get(url_g1).text

    noticias_g1 = re.findall(
        r'<a[^>]*class="feed-post-link gui-color-primary gui-color-hover"[^>]*>(.*?)</a>', html_g1
    )

    retorno = "-----------------------------------NOTÍCIAS G1-----------------------------------\n\n"
    for noticia in noticias_g1:
        retorno += f"{noticia}\n"

    return retorno


def get_ultimas_noticias() -> str:
    """Retorna o título das últimas notícias do G1 e do UOL em uma única string

    Returns:
        str: string com o título das últimas notícias do G1 e do UOL
    """

    retorno = "-----------------------------------NOTÍCIAS G1-----------------------------------\n"
    for noticia in ultimas_noticias_g1():
        retorno += f"{noticia}\n"

    retorno += "\n-----------------------------------NOTÍCIAS UOL-----------------------------------\n"

    for noticia in ultimas_noticias_uol():
        retorno += f"{noticia}\n"

    return retorno
