from noticias import ultimas_noticias_g1, ultimas_noticias_uol, ultimas_noticias_g1_com_link, ultimas_noticias_uol_com_link
from valores_atualizados import get_valor_btc_atual, get_valor_dolar_atual
from my_token import token
import discord
import re


def verifica_ajuda(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de ajuda.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de ajuda.
    """
    lista_ajuda = ['ajuda', 'help', '!help']
    verifica = re.search('|'.join(lista_ajuda), mensagem)

    return verifica != None


def verifica_saudacoes(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma saudação/cumprimento.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma saudação.
    """

    lista_saudacoes = [r'\boi.', r'\bolá.', 'bom dia', 'boa tarde', 'boa noite']
    verifica = re.search('|'.join(lista_saudacoes), mensagem)

    return verifica != None


def verifica_g1(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de noticias do G1.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do G1.
    """

    verifica = re.search(r'\bg1.', mensagem)
    return verifica != None


def verifica_g1_com_link(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento solicita noticias do G1 com links.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do G1 com links.
    """

    verifica = re.search(r'\blink.', mensagem)
    return verifica != None and verifica_g1


def verifica_uol(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação de noticias do UOL.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do UOL.
    """

    verifica = re.search(r'\buol.', mensagem)
    return verifica != None


def verifica_uol_com_link(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento solicita noticias do UOL com links.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação de noticias do UOL com links.
    """

    verifica = re.search(r'\blink.', mensagem)
    return verifica != None and verifica_uol


def verifica_btc(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação do valor atual do bitcoin.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação do valor atual do bitcoin.
    """

    lista_btc = ['bitcoin', 'btc']
    verifica = re.search('|'.join(lista_btc), mensagem)

    return verifica != None


def verifica_dolar(mensagem: str) -> bool:
    """função usada para verificar se a mensagem passada como argumento contém algum elemento da lista, ou seja, alguma solicitação do valor atual do dólar.

    Args:
        mensagem (str): mensagem captada pelo bot.

    Returns:
        bool: retorna verdadeiro se a mensagem passada pelo usuário conter alguma solicitação do valor atual do dólar.
    """

    lista_btc = ['dolar', 'dólar', 'usd']
    verifica = re.search('|'.join(lista_btc), mensagem)

    return verifica != None


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        mensagem = message.content.lower()

        if message.author.name != 'AS':  # caso a mensagem lida não seja do próprio bot
            flagMensagem = False
            flagSaudacao = False

            if verifica_ajuda(mensagem):
                flagMensagem = True
                flagSaudacao = True
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

            if verifica_g1_com_link(mensagem):
                flagMensagem = True
                flagSaudacao = True
                noticias = ultimas_noticias_g1_com_link()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)
                    else:
                        await message.channel.send('‎ \n')

            elif verifica_g1(mensagem):
                flagMensagem = True
                flagSaudacao = True
                await message.channel.send(ultimas_noticias_g1())

            if verifica_uol_com_link(mensagem):
                flagMensagem = True
                flagSaudacao = True
                noticias = ultimas_noticias_uol_com_link()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)
                    else:
                        await message.channel.send('‎ \n')

            elif verifica_uol(mensagem):
                flagMensagem = True
                flagSaudacao = True
                await message.channel.send(ultimas_noticias_uol())

            if verifica_dolar(mensagem):
                flagMensagem = True
                flagSaudacao = True
                await message.channel.send(f'\nCotação do Dólar: R$ {get_valor_dolar_atual()}')

            if verifica_btc(mensagem):
                flagMensagem = True
                flagSaudacao = True
                await message.channel.send(f'\nCotação do Bitcoin: R$ {get_valor_btc_atual()}')

            if not flagSaudacao and verifica_saudacoes(mensagem):
                flagMensagem = True
                await message.channel.send(f'\n{message.author.name}, caso tenha dúvidas do que posso fazer, digite ajuda')

            if not flagMensagem:
                await message.channel.send('\nDesculpe, não entendi. Digite ajuda e veja como posso te ajudar')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
