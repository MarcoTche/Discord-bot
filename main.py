from noticias import ultimas_noticias_g1, ultimas_noticias_uol
from valores_atualizados import get_valor_btc_atual, get_valor_dolar_atual
import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        mensagem = message.content.lower()
        match mensagem:
            case '!help' | '!h' | 'help' | 'ajuda':
                await message.channel.send(f'{message.author.name} os comandos são:{os.linesep}1 - (ultimas noticias g1?) ou (!g1): Mostra as últimas noticias do g1 {os.linesep}2 - (ultimas noticias uol?) ou (!uol): Mostra as últimas noticias do UOL{os.linesep}3 - (dolar?) ou (!USD): Mostra o valor atualizado do dólar{os.linesep}4 - (bitcoin?) ou (!BTC): Mostra o valor atualizado do bitcoin')
            case 'ultimas noticias g1?' | '!g1':
                await message.channel.send(ultimas_noticias_g1())
            case 'ultimas noticias uol?' | '!uol':
                await message.channel.send(ultimas_noticias_uol())
            case 'dolar?' | '!usd':
                await message.channel.send(f'R$ {get_valor_dolar_atual()}')
            case 'bitcoin?' | '!btc':
                await message.channel.send(f'R$ {get_valor_btc_atual()}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(
    'MTA0MTg4MjUwNTAzODUzMjY3OQ.GKnLqT.MCqbtCLrdI-vXy1cLPALZtTIjeJB-AG0_ozl14')
