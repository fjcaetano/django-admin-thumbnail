django_admin_thumbnail
======================
This is a package developed to help you with ImageField visualization in your ModelAdmin. It automatically creates user friendly thumbnail for any ImageField you choose to put in your list_display.

All you have to do is to switch from *ModelAdmin* to *ThumbAdmin* subclass. It's super easy to use: 

The Looks
---------
This is how it looks when you hover your cursor over an ImageField column:

![The Looks](https://raw.github.com/fjcaetano/django-admin-thumbnail/master/thumb_image.png)

Usage
-----

Insert **admin_thumbnail** to the end of your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'admin_thumbnail',
        ...
    )

Now, your ModelAdmin must look like this::

    from models import ModelExample
    from admin_thumbnail import thumb_admin
    from django.contrib import admin

    class ModelExampleAdmin(thumb_admin.ThumbAdmin):
        list_display = ('an_image_field',)

    admin.register(ModelExample, ModelExampleAdmin)
    
After that you must create your DB table that manages the cached thumbnails:

    python manage.py syncdb

Yes! It's THAT simple!

Requirements
------------
* [Django 1.4+](http://pypi.python.org/pypi/Django/1.4)
* [sorl.thumbnail 11.12+](http://pypi.python.org/pypi/sorl-thumbnail/11.12)
* [PIL 1.1.6+](http://pypi.python.org/pypi/PIL/1.1.6)

Installation
------------
Please, first read the [sorl.thumbnail installation](http://sorl-thumbnail.readthedocs.org/en/latest/) to install it's requirements.

Install using pip::

    pip install django-admin-thumbnail
    
Or you can clone the project and install it via::

    python setup.py install
    
Localization
------------
django-admin-thumbnail is localizable, but currently, the only officially supported languages are pt_BR and en_US. But feel free to localize it the way you want and then, send me the .po file for it to be official.

Check This Out
--------------
1. [GitHub Repository](https://github.com/fjcaetano/django_admin_thumbnail)
2. [Owner's website](http://flaviocaetano.com)
3. [PyPi package](http://pypi.python.org/pypi/django_admin_thumbnail/0.1)


Contact
==============
If you have any comments, ideas questions, feedback, etcetera, email me and we'll be in touch. I'm [flavio@vieiracaetano.com](mailto:flavio@vieiracaetano.com)
