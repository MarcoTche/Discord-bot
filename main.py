from noticias import ultimas_noticias_g1, ultimas_noticias_uol
from valores_atualizados import get_valor_btc_atual, get_valor_dolar_atual
import discord
import os

def saudacoes(mensagem):
    lista_saudacoes = ['Oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']
    for palavra in lista_saudacoes:
        if palavra in mensagem:
            return True
    return False


def verifica_g1(mensagem) -> bool:
    lista_g1 = ['últimas notícias do g1', 'ultimas noticias do g1',
                'notícias g1', 'noticias g1', '!g1']
    for palavra in lista_g1:
        if palavra in mensagem:
            return True
    return False


def verifica_uol(mensagem) -> bool:
    lista_uol = ['últimas notícias do uol', 'ultimas noticias do uol',
                 'notícias uol', 'noticias uol', '!uol']
    for palavra in lista_uol:
        if palavra in mensagem:
            return True
    return False


def verifica_btc(mensagem):
    lista_btc = ['bitcoin', '!btc']
    for palavra in lista_btc:
        if palavra in mensagem:
            return True
    return False


def verifica_dolar(mensagem):
    lista_btc = ['dolar', 'dólar', '!usd']
    for palavra in lista_btc:
        if palavra in mensagem:
            return True
    return False


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        mensagem = message.content.lower()
        if message.author.name != 'AS':
            if 'help' in mensagem or 'ajuda' in mensagem:
                await message.channel.send(f'{message.author.name} os comandos são:{os.linesep}1 - (ultimas noticias g1?) ou (!g1): Mostra as últimas noticias do g1 {os.linesep}2 - (ultimas noticias uol?) ou (!uol): Mostra as últimas noticias do UOL{os.linesep}3 - (dolar?) ou (!USD): Mostra o valor atualizado do dólar{os.linesep}4 - (bitcoin?) ou (!BTC): Mostra o valor atualizado do bitcoin')
            elif saudacoes():
                await message.channel.send('Olá, caso tenha dúvidas do que posso fazer, use o comando !help')
            elif verifica_g1(mensagem):
                await message.channel.send(ultimas_noticias_g1())
            elif verifica_uol(mensagem):
                await message.channel.send(ultimas_noticias_uol())
            elif verifica_dolar(mensagem):
                await message.channel.send(f'R$ {get_valor_dolar_atual()}')
            elif verifica_btc(mensagem):
                await message.channel.send(f'R$ {get_valor_btc_atual()}')
            else:
                await message.channel.send('Desculpe, não entendi. Veja !help')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(
    'MTA0MTg4MjUwNTAzODUzMjY3OQ.GKnLqT.MCqbtCLrdI-vXy1cLPALZtTIjeJB-AG0_ozl14'
)
