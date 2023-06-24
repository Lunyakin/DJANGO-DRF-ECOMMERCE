#Comands

-----------generation of SECRET_KEY-----------
py manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

#Packages

python-dotenv  
Django==4.2.2
djangorestframework==3.14.0
pytest==7.4.0
pytest-django

##Pytest

pytest -h # prints options _and_ config file settings