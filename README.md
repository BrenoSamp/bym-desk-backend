# BYM-DESK-BACKEND DOCUMENTATION

## Depêndencias Locais

- Python3


## Depêndencias a serem instaladas com o venv (Tutorial)

### Gerando ambiente virtual

- 1º Na pasta raíz criar ambiente Virtual

```bash
python3 -m venv ./venv
```

- 2º Pegar o caminho do projeto

```bash
pwd
```

(O resultado será o caminho local até o projeto)

- 3º  Na pasta raiz executar o ambiente virtual executando o seguinte comando com as informações obtidas no passo anterior

```bash
source {caminho/de/exemplo/anterior}/venv/bin/activate
```

- 4º Após a execução desses comandos vocÊ estará dentro do ambiente virtual

*Exemplo:*

```bash
(venv) ➜  bym-desk-backend git:(master) ✗
```

### Instalando dependêndencias dentro do ambiente virtual

- Django

```
pip install django
```

- Django Rest Framework

```
pip install djangorestframework
```

- Pika

```
pip install pika
```


## Subindo Servidor

- Executar seguinte comando

```
python3 manage.py runserver
```



