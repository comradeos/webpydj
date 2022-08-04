# WebPyDj Project
Simple Python/Django based project, learning features/documentation of this framework


# Основні Django команди
#### Створити новий проект my_project
```
django-admin startproject my_project
```

#### Запустити сервер
```
python manage.py runserver
```

#### Docker: інтерактивний режим Python
```
docker exec -it webpydj-python-1 python  
```
#### Docker: інтерактивний режим Bash
```
docker exec -it webpydj-python-1 bash    
```

#### Створити новий додаток з ім'ям 'coreapp'
```
python manage.py startapp coreapp
```

#### Зареєструвати додаток 'coreapp' в проекті
1. Відкрити webpydj->settings.py  
2. Додати у список 'INSTALLED_APPS' наступне:  
```
'coreapp.apps.CoreappConfig',
```
'coreapp' це назва додатку (додатки реалізовані як пакети)  
'apps' це файл 'apps.py' який знаходиться у 'coreapp'  
'CoreappConfig' це згенерована назва класу у файлі 'apps.py'  

#### Підключення MySQL бази даних:  
1. Створити нову базу з іменем my_db  
2. Відкрити [назва_проекту]->settings.py  
3. Додати наступне:  
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

#### Створити файли міграцій:
```
docker exec -it webpydj-python-1 bash    
```
```
python manage.py makemigrations  
``` 
#### Подивитись який саме SQL запит має виконатись для додатки 'coreapp':
```
python manage.py sqlmigrate coreapp 0001
```

#### Мігрувати в базу даних:
```
python manage.py migrate
```
#### Відкрити Django shell сесія
```
python manage.py shell
```
#### Створити новій запис
1. Імпортувати [клас] з [додаток].models  
```
from coreapp.models import Languages
```
2. Створити новий об'єкт запису  
```
new_record = Languages(title='Python', content='A high-level, interpreted, general-purpose programming language.')
```
3. Зберегти    
```
new_record.save()
```
#### Отримати ключ нового запису  
```
new_record.pk
```
#### Подивитись виконані запити  
```
from django.db import connection
```
```
connection.queries
```
#### Методи об'єкту записів 
```
Languages.objects # <django.db.models.manager.Manager object at 0x7f0dc2d467a0>
```
#### Створити без використання 'save()' методу: 
```
Languages.objects.create(title='C++', content='A general-purpose programming language created by Danish computer scientist Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".')
```
#### Отримати всі записи з таблиці coreapp_languages:
```
Languages.objects.all()
```
#### Всі записи з таблиці coreapp_languages де  id==1 :
```
Languages.objects.filter(id=1)
```
or  
```
Languages.objects.filter(pk=1)
```
#### Всі записи з таблиці coreapp_languages де id>=2 :
```
Languages.objects.filter(id__gte=2)
```
or  
```
Languages.objects.filter(pk__gte=2)
```
#### Всі записи з таблиці coreapp_languages де id<=2 :
```
Languages.objects.filter(id__lte=2)
```
or  
```
Languages.objects.filter(pk__lte=2)
```
#### Всі записи з таблиці coreapp_languages де id!=2 :
```
Languages.objects.exclude(id=2)
```
#### Тільки один запис де  id=1:
```
Languages.objects.get(id=1)
```
#### Сортування результатів від 0-9
```
Languages.objects.filter(id__lte=4).order_by('title')
```
#### Сортування результатів від 9-0
```
Languages.objects.filter(id__lte=4).order_by('-title')
```

#### Змінити title запису
```
item = Languages.objects.get(title='C++')
```
```
item.title = 'C+++'
```
```
item.save()
```
#### Видалити title запису
```
item = Languages.objects.get(title='JavaScript')
```
```
item.delete()
```
#### Створити супер користувача

```
python manage.py createsuperuser
```
#### Paginator
```
from django.core.paginator import Paginator
```
#### Список для прикладу
plist = ['a','b','c','d','e','f']
#### Створення екземпляру
```
p = Paginator(plist, 3)
```
#### Кількість елементів 
```
p.count
```
#### Кількість сторінок
```
p.num_pages
```

#### Показати об'єкти першої сторінки 
```
p.page(1).object_list
```