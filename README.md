# Documentação

Documentação e passo a passo do projeto
## Depêndencias a serem instaladas

- [Python ^3.0](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

## Iniciando aplicação

- Inicializar os containers executando o comando:

```bash
docker-compose up --build
```

## Acessando container da aplicação

- Para acessar o container da aplicaçao e executar os comandos python executar seguinte comando:

```bash
docker exec -it bym_backend sh
```

- Para acessar o container do banco e executar os comandos sql executar seguinte comando:

```bash
docker exec -it bym_db sh -c "mysql -u root -p'root' bym"
```

## Executando Migrações

- No container `bym_backend` executar os seguintes comandos

```bash
python3 /app/manage.py makemigrations
python3 /app/manage.py migrate
```

## Criando super usuário para django admin

Executar comando para criar novo usuário:

```bash
python3 /app/manage.py createsuperuser
```


**(O resultado será o caminho local até o projeto)**

- Na pasta raiz executar o ambiente virtual executando o seguinte comando com as informações obtidas no passo anterior

```bash
source {caminho/de/exemplo/anterior}/venv/bin/activate
```

- Após a execução desses comandos você estará dentro do ambiente virtual

*Exemplo:*

```bash
(venv) ➜  bym-desk-backend git:(master) ✗
```

### Instalando dependêndencias dentro do ambiente virtual

- Python

```bash
pip install python
```

**(Após a instalação apertar CTRL+SHIFT+P e buscar por `select interpreter` e selecionar o interpretador do ambiente virtual)**

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

## Migrações

### Executando migrações

Executar seguinte comando (Ambiente virtual):

```bash
python manage.py makemigrations
```

### Rodando migrações existentes

Executar seguinte comando (Ambiente virtual):

```bash
python manage.py migrate
```

## Criando super usuário para django admin

Executar comando para criar novo usuário:

```bash
python manage.py createsuperuser
```
## Subindo Servidor

- Executar seguinte comando

```bash
python manage.py runserver
```

## Referências

- https://www.djangoproject.com/
- https://www.django-rest-framework.org/
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django


