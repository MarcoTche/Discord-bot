from noticias import ultimas_noticias_g1, ultimas_noticias_uol, ultimas_noticias_g1_com_link, ultimas_noticias_uol_com_link
from valores_atualizados import get_valor_btc_atual, get_valor_dolar_atual
from my_token import token
import discord


def verifica_ajuda(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de ajuda.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de ajuda.
    """
    mensagem = mensagem.split(' ')
    lista_ajuda = ['ajuda', 'help', '!help', ]

    for palavra in lista_ajuda:
        if palavra in mensagem:
            return True
    return False


def verifica_saudacoes(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma saudação/cumprimento.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma saudação.
    """

    mensagem = mensagem.split(' ')
    lista_saudacoes = ['oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']

    for palavra in lista_saudacoes:
        if palavra in mensagem:
            return True
    return False


def verifica_g1(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de noticias do G1.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do G1.
    """

    mensagem = mensagem.split(' ')
    if 'g1' in mensagem:
        return True
    return False


def verifica_g1_com_link(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento solicita noticias do G1 com links.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do G1 com links.
    """

    if 'link' in mensagem and verifica_g1(mensagem):
        return True
    return False


def verifica_uol(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de noticias do UOL.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do UOL.
    """

    mensagem = mensagem.split(' ')
    if 'uol' in mensagem:
        return True
    return False


def verifica_uol_com_link(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento solicita noticias do UOL com links.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do UOL com links.
    """

    if 'link' in mensagem and verifica_uol(mensagem):
        return True
    return False


def verifica_btc(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação do valor atual do bitcoin.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação do valor atual do bitcoin.
    """

    mensagem = mensagem.split(' ')
    lista_btc = ['bitcoin', 'btc']

    for palavra in lista_btc:
        if palavra in mensagem:
            return True
    return False


def verifica_dolar(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação do valor atual do dólar.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação do valor atual do dólar.
    """

    mensagem = mensagem.split(' ')
    lista_btc = ['dolar', 'dólar', 'usd']

    for palavra in lista_btc:
        if palavra in mensagem:
            return True
    return False


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        mensagem = message.content.lower()

        if message.author.name != 'AS':  # caso a mensagem lida não seja do próprio bot

            if verifica_ajuda(mensagem):
                await message.channel.send(f'''
{message.author.name}, posso te oferecer algumas informações atualizadas! Como por exemplo:     

- Mostrar o título das últimas notícias do G1 (use --link para obter o link das notícias)
- Mostrar o título das últimas notícias do UOL (use --link para obter o link das notícias)
- Mostrar o valor atualizado do dólar 
- Mostrar o valor atualizado do bitcoin     


Exemplos: 
    Olá, gostaria de saber o valor atualizado do dólar!
    Olá, gostaria de saber quais são as últimas notícias do UOL! --link
''')

            elif verifica_g1_com_link(mensagem):
                noticias = ultimas_noticias_g1_com_link()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)
                    else:
                        await message.channel.send('‎ \n')

            elif verifica_g1(mensagem):
                await message.channel.send(ultimas_noticias_g1())

            elif verifica_uol_com_link(mensagem):
                noticias = ultimas_noticias_uol_com_link()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)
                    else:
                        await message.channel.send('‎ \n')

            elif verifica_uol(mensagem):
                await message.channel.send(ultimas_noticias_uol())

            elif verifica_dolar(mensagem):
                await message.channel.send(f'R$ {get_valor_dolar_atual()}')

            elif verifica_btc(mensagem):
                await message.channel.send(f'R$ {get_valor_btc_atual()}')

            elif verifica_saudacoes(mensagem):
                await message.channel.send(f'{mensagem}, caso tenha dúvidas do que posso fazer, use o comando !help')

            else:
                await message.channel.send('Desculpe, não entendi. Veja !help')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
