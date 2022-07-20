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
docker exec -it webpydj-python-1 sh
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