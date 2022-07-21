# WebPyDj Project
Simple Python/Django based project, learning features/documentation of this framework


# Common Django Commands
#### Create a Django project
```
django-admin startproject my_project
```

#### Run Django server
```
python manage.py runserver
```

#### Docker Python/Django interactive mode
```
docker exec -it webpydj-python-1 python  
```
#### Docker Python Bash interactive mode
```
docker exec -it webpydj-python-1 bash    
```

#### Create new Django application named 'coreapp'
```
python manage.py startapp coreapp
```

#### Register 'coreapp' in webpydj project
1. Open webpydj->settings.py  
2. Add to list 'INSTALLED_APPS' next:  
```
'coreapp.apps.CoreappConfig',
```
'coreapp' is an application name (realized as a package)  
'apps' is the file 'apps.py' located in 'coreapp'  
'CoreappConfig' is the name of auto-generated class in file 'apps.py'  

#### Connect to database:  
1. Create database my_db  
2. Open [project_name]->settings.py  
3. Add next:  
```
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django', 
        'NAME': 'my_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'db',
        'PORT': '3306',
    }
}
```

#### Make migration file:
```
docker exec -it webpydj-python-1 bash    
```
```
python manage.py makemigrations  
``` 
#### Check sql going to be executed for app 'coreapp':
```
python manage.py sqlmigrate coreapp 0001
```

#### Migrate to database:
```
python manage.py migrate
```
#### Django shell session
```
python manage.py shell
```
#### Create new record
1. Import [class] from [application].models  
```
from coreapp.models import Languages
```
2. Create new object of record  
```
new_record = Languages(title='Python', content='A high-level, interpreted, general-purpose programming language.')
```
3. Save new record  
```
new_record.save()
```
#### Get primary key of new record
```
new_record.pk
```
#### Check executed queries
```
from django.db import connection
```
```
connection.queries
```
#### Record object methods
```
Languages.objects # <django.db.models.manager.Manager object at 0x7f0dc2d467a0>
```
#### Create without 'save()' method: 
```
Languages.objects.create(title='C++', content='A general-purpose programming language created by Danish computer scientist Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".')
```
#### Read all records from database:
```
Languages.objects.all()
```
#### Read all records from database with id=1 :
```
Languages.objects.filter(id=1)
```
#### Read all records from database with id 1 :
```
Languages.objects.filter(id=1)
```
