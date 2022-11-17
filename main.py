from noticias import ultimas_noticias_g1, ultimas_noticias_uol
from valores_atualizados import get_valor_btc_atual, get_valor_dolar_atual
from my_token import token
import discord
import os


def saudacoes(mensagem:str):
    lista_saudacoes = ['oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']
    for palavra in lista_saudacoes:
        if palavra in mensagem.lower():
            return True
    return False


def verifica_g1(mensagem:str) -> bool:
    lista_g1 = ['últimas notícias do g1', 'ultimas noticias do g1',
                'noticias atualizadas do g1', 'notícias atualizadas do g1'
                'notícias g1', 'noticias g1', '!g1']
    for palavra in lista_g1:
        if palavra in mensagem.lower():
            return True
    return False


def verifica_uol(mensagem:str) -> bool:
    lista_uol = ['últimas notícias do uol', 'ultimas noticias do uol',
                 'noticias atualizadas do uol', 'notícias atualizadas do uol'
                 'notícias uol', 'noticias uol', '!uol']
    for palavra in lista_uol:
        if palavra in mensagem.lower():
            return True
    return False


def verifica_btc(mensagem:str):
    lista_btc = ['bitcoin', '!btc']
    for palavra in lista_btc:
        if palavra in mensagem.lower():
            return True
    return False


def verifica_dolar(mensagem:str):
    lista_btc = ['dolar', 'dólar', '!usd']
    for palavra in lista_btc:
        if palavra in mensagem.lower():
            return True
    return False


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        mensagem = message.content.lower()
        if message.author.name != 'AS':
            if 'help' in mensagem or 'ajuda' in mensagem:
                await message.channel.send(f'{message.author.name}, posso te oferecer algumas informações atualizadas! Como por exemplo:{os.linesep}{os.linesep}- Mostrar as últimas notícias do G1{os.linesep}- Mostra as últimas notícias do UOL{os.linesep}- Mostra o valor atualizado do dólar{os.linesep}- Mostra o valor atualizado do bitcoin{os.linesep}{os.linesep}Tente esse comando (Olá, gostaria de saber o valor atualizado do dólar!)')
            elif verifica_g1(mensagem):
                noticias = ultimas_noticias_g1()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)  
                    else:
                        await message.channel.send('‎ \n')  

            elif verifica_uol(mensagem):
                noticias = ultimas_noticias_uol()
                for i in noticias.split('\n'):
                    if i:
                        await message.channel.send(i)  
                    else:
                        await message.channel.send('‎ \n')  
            elif verifica_dolar(mensagem):
                await message.channel.send(f'R$ {get_valor_dolar_atual()}')
            elif verifica_btc(mensagem):
                await message.channel.send(f'R$ {get_valor_btc_atual()}')
            elif saudacoes(mensagem):
                await message.channel.send(f'{mensagem}, caso tenha dúvidas do que posso fazer, use o comando !help')
            else:
                await message.channel.send('Desculpe, não entendi. Veja !help')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
