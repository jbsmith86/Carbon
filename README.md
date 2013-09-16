Titan
=========

Django blogging platform

##Installation
best used on a Debian Linux server
**install in /var/www/titan**

create django database:
```
cd /var/www/titan
python manage.py syncdb
```

**install nginx and uwsgi**

configure nginx and start uwsgi:
```
ls /var/www/titan/nginx.conf /etc/nginx/sites-enabled
/etc/init.d/nginx restart
uwsgi --socket :8000 --wsgi-file /var/www/titan/american/wsgi.py --chdir /var/www/titan
```
