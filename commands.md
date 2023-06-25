**#Comands**

_-----------generation of SECRET_KEY-----------_
1. py manage.py shell
2. from django.core.management.utils import get_random_secret_key
3. print(get_random_secret_key())

_-----------generation Schema by drf-spectacular-----------_
1. py manage.py spectacular --file schema.yml

_-----------For testing project-----------_
coverage run -m pytest
coverage html  # for creating report in html
pytest --cov


**#Packages**

1. python-dotenv  
2. Django==4.2.2
3. djangorestframework==3.14.0
4. pytest==7.4.0
5. pytest-django
6. django-mptt
7. drf-spectacular
8. coverage
9. pytest-factoryboy  #factory for testing



**##Pytest**

pytest -h # prints options _and_ config file settings