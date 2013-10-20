Carbon
=========

Django blogging platform

##Installation
best used on a Debian Linux server
**install in /var/www/carbon**

create django database:
```
cd /var/www/Carbon
python manage.py syncdb
```

install nginx and uwsgi
```
apt-get install nginx
pip install uwsgi
```

set folders to chmod 755 and files to chmod 644

configure nginx and start uwsgi:
```
ln -s /var/www/Carbon/nginx.conf /etc/nginx/sites-enabled
/etc/init.d/nginx restart
uwsgi --socket :8000 --wsgi-file /var/www/Carbon/carbon/wsgi.py --chdir /var/www/Carbon
```
