# django

> Framework em python para a criação de aplicações web

- Criar um projeto:

`django-admin startproject {{nome-projeto}} .`

- Criar uma aplicação (app):

`python3 manage.py startapp {{nome-app}}`

- Criar uma lista de coisas que queremos migrar para o banco:

`python3 manage.py makemigrations`

- Inserir os arquivos do migrations no banco de dados:

`python3 manage.py migrate`

Carregar arquivos estáticos:

`python3 manage.py collectstatic`

Criar usuário admin:

`python3 manage.py createsuperuser`

Iniciar o servidor de desenvolimento:

`python3 manage.py runserver`
