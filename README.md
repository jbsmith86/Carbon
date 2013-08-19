Ameriblog
=========

Django blogging platform best used on a Debian Linux server

##Installation
**install in /var/www/Ameriblog**

create django database:
```
cd /var/www/Ameriblog
python manage.py syncdb
```

**install nginx and uwsgi**

configure nginx and start uwsgi:
```
ls /var/www/Ameriblog/nginx.conf /etc/nginx/sites-enabled
/etc/init.d/nginx restart
uwsgi --socket :8000 --wsgi-file /var/www/Ameriblog/american/wsgi.py --chdir /var/www/Ameriblog
```
