# Django ve Python Kurulumu ve Ornek Uygulama  
Django Python ile yazılmış python ile web uygulama geliştirebileceğiniz bir kütüphanedir.
MTV(Model Template View) mantığı ile kurgulanmıştır.


## Python & Pip & Django Kurulum
Win işletim sistemi kullandığınızı varsayıyoruz. Öncelikle [Python](https://www.python.org/downloads/) kurulumunu gerçekleştiriniz.
Komut satırıdan python versiyonunu sorarak kurulumun gerçekleştiğiniz kontrol edebiliriz. Eğer sorun yaşıyorsanız [makaledeki](https://geek-university.com/python/add-python-to-the-windows-path/) adımları uygulayabilirsiniz.
```sh
$ python -V
```


## Pip 
pip Python ile yazılmış yazılım paketlerini kurmak ve yönetmek için kullanılan bir paket yönetim sistemidir.
```sh
$ python -m pip install -U pip
```
## Django 
```sh
$ pip install Django
Kurulumu kontrol etmek için ise django-admin komutunu kullanabilirisiniz.
$ django-admin
```

## Django New Project
```sh
$ django-admin startproject {appName}
```
### Development Server
```sh
$ python manage.py runserver {ip}:{port}
```
## Create Polls
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

## Template View Url Yapısı
.....................

## Css & JS vb Static Dosya Yapılandırması
Settings.py içerisinde aşağıdaki şekilde yapılandırma ayarlarını tamamlayalım.
```sh
# site.domain/assets şeklinde static dosyalara erişim sağlanabileceğini tanımlıyoruz.
STATIC_URL = '/assets/'
# Static dosyaların hangi dizine kopyalanacağının yolunu belirtiyoruz.
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# static dosya kaynağını belirtiyoruz. Burada kaynağın yolunu doğru seçmeye dikkat edin. 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR + '\\blogs\\', 'static'),
)
```
urls.py içerisinde aşağıdaki şekilde yapılandırma ayarlarını tamamlayalım.
```sh
# staticfiles_urlpatterns import edelim ve urlpatterns e static dosyaları tanımlayalım aksi halde erişilmek istenen kaynak 404 dönebilir.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

```



```sh
# Aşağıdaki komut ile static dosyaları static_URL ile belirttiğimiz dizine çıktısını alalım.
python manage.py collecstatic

```