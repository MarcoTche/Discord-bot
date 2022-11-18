<h1>Bot para discord</h1>

> Status: Em desenvolvimento

<h3 style="text-align: justify; margin: 1.3em 0">Esse projeto é uma aplicação criada como resposta à uma atividade da matéria de Linguagens Formais e Teoria da Computação, ministrada pelo professor <a href="https://github.com/jacksongomesbr">Jackson Gomes</a>, com o intuito de fazer um bot do discord que responde à comandos específicos.</h3>

<h3>Recursos a serem desenvolvidos:</h3>

- Funcionalidades que visam a comunicação/interação menos robótica.

<h3 style="margin: 1.1em 0">Como rodar a aplicação:</h3>

Crie e habilite um ambiente virtual

```console
  python -m venv venv
```

```console
  venv\Scripts\activate | windows
  .venv/bin/activate | linux e macOs
```

Instale as dependências do projeto

```console
  pip install -r requirements.txt
```

Defina o token solicitado pelo arquivo main.py

```
  Copie o arquivo exemplo_my_token.py e renomeie-o para my_token.py
  Após, substitua a string 'token' da variável para uma string com o seu token
```

[Link de auxílio para criação do seu próprio token]('https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token/')

## Uso

Inicialize o bot:

```console
python main.py
 > verifique se o bot ficou online no servidor 
```

Comandos implementados:

```console
'!help' ou 'ajuda' - Bot vai retornar algumas funcionalidades que ele entende
...
```
