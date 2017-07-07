# Oauth 2 em Python

O extrator é feito em Python usando a versão 3.X, para definição de rotas foi usado o Framework [Bottle] na versão 0.12.13 que é usado para o OAuth2.0.

### Tecnologias

Varejo Online - Data Extractor usa as seguintes tecnologias:

* [Python 3.X] - Work quickly and integrate systems more effectively!
* [Bottle] - Bottle is a fast, simple and lightweight WSGI micro web-framework.

### Instalação

Precisa do [Python][python 3.X] na versão 3.X instalada para poder executar.

Instalar as dependencias que estão no arquivo requirements.txt

```sh
# pip install -r requirements.txt
```
### Execução

Para rodar o código é só executar o arquivo server.py

```sh
$ python3 server.py
```

O sistema vai responder avisando que o Bottle iniciou e está ouvindo a porta 8000

```sh
Bottle v0.12.13 server starting up (using WSGIRefServer())...
Listening on http://localhost:8000/
Hit Ctrl-C to quit.
```

   [python 3.X]: <https://www.python.org/>
   [bottle]: <https://bottlepy.org/docs/dev/>
