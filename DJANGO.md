
# Command lines
    django-admin startproject mysite
    
    cd mysite
    ./manage.py startapp itaiching
    
    ./manage.py makemigrations
    ./manage.py migrate
    
    ./manage.py createsuperuser
    
    ./manage.py runserver $IP:$PORT
    
    
    
# mysite settings

    INSTALLED_APPS = [
        'itaijing',
    
    TIME_ZONE = 'Asia/Taipei'