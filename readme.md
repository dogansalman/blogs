# Django ve Python Kurulumu ve Ornek Uygulama  
Django Python ile yazılmış python ile web uygulama geliştirebileceğiniz bir kütüphanedir.
MTV(Model Template View) mantığı ile kurgulanmıştır.


### Python & Pip & Django Kurulum
Win işletim sistemi kullandığınızı varsayıyoruz. Öncelikle [Python](https://www.python.org/downloads/) kurulumunu gerçekleştiriniz.
Komut satırıdan python versiyonunu sorarak kurulumun gerçekleştiğiniz kontrol edebiliriz. Eğer sorun yaşıyorsanız [makaledeki](https://geek-university.com/python/add-python-to-the-windows-path/) adımları uygulayabilirsiniz.
```sh
$ python -V
```


### Pip 
pip Python ile yazılmış yazılım paketlerini kurmak ve yönetmek için kullanılan bir paket yönetim sistemidir.
```sh
$ python -m pip install -U pip
```
### Django 
```sh
$ pip install Django
Kurulumu kontrol etmek için ise django-admin komutunu kullanabilirisiniz.
$ django-admin
```

### Django New Project
```sh
$ django-admin startproject {appName}
```
### Development Server
```sh
$ python manage.py runserver {ip}:{port}
```
### Create Polls
Artık - bir “proje” - kurulmuş, işe başlamak için hazırsınız.
```sh
$ python manage.py startapp polls
```
Yukarıdaki komut ile polls dizinin oluştuğunu göreceksiniz. Burda model view ve migration konfigurasyonlarını sağlayabilirsiniz.  ancak ana settings.py içerisine aşağıdaki şekilde kullanacağınız Polls'i tanımlamalısınız.
### Settings.py
```sh
INSTALLED_APPS = [
    'blogs.polls.PollsConfig',
    ...
    ...
    ...
    ...
]
```
