# Beginner's guide on using DRF

Install `djangorestframework`

```
pip install djangorestframework
```

OR

```
python3.7 -m pip install djangorestframework
```

OR

Install as a part of your Docker Package

---

## Get Coding


Create an app to test the framework

```
python .\manage.py startapp demo
```

Create models on which CRUD operations will take place

DRF allows serailization to visualize data in models textaully

- Create `serializers.py` in the demo app
- Make use of the `serializers` module in `rest_framework`


CRUD is handled by `viewsets` in `rest_framework`

- Code goes in `api_views.py` in the demo app


Make use of routers to create endpoints to be accessed by app URLs

- Code for routers goes in `app.py` in demo (main) app
- Add `path('api/v1/', include(router.urls))` to main app's `urls.py`


## To summarize

```
models -> app-level serializers (associate models) -> app-level api_views (viewsets to connect models and serializers) -> main-app api (routers to specify endpoints) -> runserver and test
```



## Initial migration example


```
PS C:\Users\Parth\Django\drf> python .\manage.py makemigrations
Migrations for 'demo':
  demo\migrations\0001_initial.py
    - Create model Basic
PS C:\Users\Parth\Django\drf> python .\manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, demo, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying demo.0001_initial... OK
  Applying sessions.0001_initial... OK
PS C:\Users\Django\drf> python .\manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 01, 2021 - 14:56:37
Django version 3.2, using settings 'drf.settings'    
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Not Found: /
[01/Jun/2021 14:56:44] "GET / HTTP/1.1" 404 2048
Not Found: /favicon.ico
[01/Jun/2021 14:56:45] "GET /favicon.ico HTTP/1.1" 404 2099
[01/Jun/2021 14:56:50] "GET /api/v1/ HTTP/1.1" 200 5315
[01/Jun/2021 14:56:50] "GET /static/rest_framework/css/prettify.css HTTP/1.1" 304 0        
[01/Jun/2021 14:56:50] "GET /static/rest_framework/css/bootstrap.min.css HTTP/1.1" 304 0   
[01/Jun/2021 14:56:50] "GET /static/rest_framework/css/default.css HTTP/1.1" 304 0
[01/Jun/2021 14:56:50] "GET /static/rest_framework/css/bootstrap-tweaks.css HTTP/1.1" 304 0
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/jquery-3.5.1.min.js HTTP/1.1" 304 0  
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/ajax-form.js HTTP/1.1" 304 0
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/bootstrap.min.js HTTP/1.1" 304 0     
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/csrf.js HTTP/1.1" 304 0
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/default.js HTTP/1.1" 304 0
[01/Jun/2021 14:56:50] "GET /static/rest_framework/js/prettify-min.js HTTP/1.1" 304 0      
[01/Jun/2021 14:56:50] "GET /static/rest_framework/img/grid.png HTTP/1.1" 304 0
[01/Jun/2021 14:56:53] "GET /api/v1/basic/ HTTP/1.1" 200 8575
[01/Jun/2021 14:56:58] "POST /api/v1/basic/ HTTP/1.1" 201 8650
[01/Jun/2021 14:57:00] "POST /api/v1/basic/ HTTP/1.1" 201 8650
[01/Jun/2021 14:57:02] "POST /api/v1/basic/ HTTP/1.1" 201 8650
[01/Jun/2021 14:57:04] "POST /api/v1/basic/ HTTP/1.1" 201 8650
[01/Jun/2021 14:57:57] "GET /api/v1/basic/ HTTP/1.1" 200 8911
```