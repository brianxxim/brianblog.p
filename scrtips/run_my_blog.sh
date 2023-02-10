#! /bin/bash
# shellcheck disable=SC1090
source ~/.bash_profile
workon brianblog
export DJANGO_SETTINGS_MODULE=my_blog.settings.production
cd /web/projects/brianblog || echo "brianblog project non-existent"
exec gunicorn -c ./gunicorn.conf.py my_blog.wsgi
