# Provide app name context to the 500 error page

This repo was produced as an answer to [this question](https://stackoverflow.com/questions/48560250/django-context-processors-for-error-pages-or-request-in-simple-tag) on stack overflow.

## Installation

```shell
git clone git@github.com:Asday/django-custom-error-handler.git
cd django-custom-error-handler
mkvirtualenv --python=$(which python3.6) django-custom-error-handler
python manage.py runserver 0.0.0.0:8000
```

Then visit [/app_1/](http://127.0.0.1:8000/app_1/) or [/app_2/](http://127.0.0.1:8000/app_2/).
