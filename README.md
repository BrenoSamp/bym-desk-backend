# Documentação

Documentação e passo a passo do projeto
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

- 4º Após a execução desses comandos você estará dentro do ambiente virtual

*Exemplo:*

```bash
(venv) ➜  bym-desk-backend git:(master) ✗
```

### Instalando dependêndencias dentro do ambiente virtual

- Python

```bash
pip install python
```

(Após isso apertar CTRL+SHIFT+P e buscar por `select interpreter` e selecionar o interpretador do ambiente virtual)

- Django

```bash
pip install django
```

- Django Rest Framework

```bash
pip install djangorestframework
```

- Markdown

```bash
pip install markdown
```

- Pika

```
pip install pika
```

## Executando migrações

Executar seguinte comando (Ambiente virtual):

```bash
python manage.py runserver
```


## Subindo Servidor

- Executar seguinte comando

```bash
python manage.py makemigrations
```

## Referências

https://www.djangoproject.com/
https://www.django-rest-framework.org/


