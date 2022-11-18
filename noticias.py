import requests
import re


def ultimas_noticias_uol() -> list:
    """Retorna apenas o título das últimas notícias do UOL (sem link)

    Returns:
        list: lista com o título das últimas notícias do UOL
    """

    try:
        url_uol = "https://noticias.uol.com.br/ultimas/"

        html_uol = requests.get(url_uol).text

        noticias_uol = re.findall(
            r'<h3 class="thumb-title title-xsmall title-lg-small"[^>]*>(.*?)</h3>', html_uol
        )

        retorno = "-----------------------------------NOTÍCIAS UOL-----------------------------------\n\n"
        for noticia in noticias_uol:
            retorno += f"{noticia}\n"

        return retorno

    except:
        raise Exception('Erro ao consultar notícias!')


def ultimas_noticias_g1() -> list:
    """Retorna apenas o título das últimas notícias do G1 (sem link)

    Returns:
        list: lista com o título das últimas notícias do G1
    """

    try:
        url_g1 = "https://g1.globo.com/"

        html_g1 = requests.get(url_g1).text

        noticias_g1 = re.findall(
            r'<a[^>]*class="feed-post-link gui-color-primary gui-color-hover"[^>]*>(.*?)</a>', html_g1
        )

        retorno = "-----------------------------------NOTÍCIAS G1-----------------------------------\n\n"
        for noticia in noticias_g1:
            retorno += f"{noticia}\n"

        return retorno

    except:
        raise Exception('Erro ao consultar notícias!')


def ultimas_noticias_uol_com_link() -> list:
    """Retorna o título e o link das últimas notícias do UOL

    Returns:
        list: lista com o título e link das últimas notícias do UOL
    """
    try:
        url_uol = "https://noticias.uol.com.br/ultimas/"

        html_uol = requests.get(url_uol).text

        noticias_uol = re.findall(
            r'<a href="([^"]*)".*?<h3 class="thumb-title title-xsmall title-lg-small"[^>]*>(.*?)</h3>', html_uol
        )

        retorno = "-----------------------------------NOTÍCIAS UOL-----------------------------------\n\n"
        for noticia in noticias_uol:
            retorno += f"- **{noticia[1]}**\n*{noticia[0]}*\n\n"

        return retorno

    except:
        raise Exception('Erro ao consultar notícias!')


def ultimas_noticias_g1_com_link() -> list:
    """Retorna o título e link das últimas notícias do G1

    Returns:
        list: lista com o título e link das últimas notícias do G1
    """

    try:
        url_g1 = "https://g1.globo.com/"

        html_g1 = requests.get(url_g1).text

        noticias_g1 = re.findall(
            r'<a href="([^"]*)"[^>]*class="feed-post-link gui-color-primary gui-color-hover"[^>]*>(.*?)</a>', html_g1
        )

        retorno = "-----------------------------------NOTÍCIAS G1-----------------------------------\n\n"
        for noticia in noticias_g1:
            retorno += f"- **{noticia[1]}**\n*{noticia[0]}*\n\n"

        return retorno

    except:
        raise Exception('Erro ao consultar notícias!')
