# Usando o _Poetry_

Após instalar o **poetry** globalmente na máquina, inicie um novo projeto.
> poetry init

Adcione como dependência de desemvolvimento os seguintes pacotes:
- pytest
- factory-boy

Instale o Django: `poetry add django`  \
Inicie um novo projeto: `poetry run django-admin startproject [nome_do_projeto] .`
Teste se está ok: `poetry run python manage.py runserver`

Crie um novo app: `poetry run python manage.py startapp order`  \
Crie um novo app: `poetry run python manage.py startapp product`

Crie os modelos, registre no admin e nos app instalados:

Gere as migrações:  \
> `poetry run python manage.py makemigrations`  \
> `poetry run python manage.py migrate`