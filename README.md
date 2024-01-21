HiDoc API was created from a preset model provided by Code Institute: https://github.com/Code-Institute-Org/ci-full-template

HIdoc-API is a Django REST Framework ("DRF") Application Programming Interface ("API").

Most features will be explained with the question of "why?" since that question invite the best explainations.

The setup followed a step by step guide created by Code Institute. Source: https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn


Django:
---
In terminal:
`pip3 install 'django<4'`
Please ignore the notice message from the terminal that ask you to update.
- Why?
django<4 install a long term supported version of Django that is recomended over the newer version.


Images:
---
Images are hosted by Cloudinary.
Images are used for Artists profile picture, documentation, and project thumbnail.

Cloudinary will add a hash to prevent duplicat errors if any user uploads an image with generic name such s image.PNG
In terminal:
`pip3 install django-cloudinary-storage`

Images are processed with Pillow.
In terminal:
`pip3 install Pillow`
- Why?
Cloudinary alone serve to store images and videos, it does not provide serivce to update and proccess them.

The settings are: CLOUDINARY_STORAGE, MEDIA_URL, and DEFAULT_FILE_STORAGE


env.py:
---
The environment file (env.py) is only available to the developmer(s). The env.py file access sensitive enviroments, such as Cloudinary.
The contents are:
`
import os
os.environ['CLOUDINARY_URL'] = '(cloudinary API adress)'
`

These lines must exist in settings.py:
`
import os
is os.path.exists('env.py'):
    import env
`
- Why?
During development: settings.py need to link up env.py so that it can be read and used.


Project:
---
In terminal:
`django-admin startproject drf_api .`


Apps:
---
- To create an app, run in terminal:
`python3 manage.py startapp (app_name)`
- HiDoc API created these apps:
"art_acc" (artists account)


Artits account:
---
The model for artist account follow a similar structure to Code Institute's Moments tutorial model for profiles.


Run server:
---
To test the app, run this in the terminal:
`python3 manage.py runserver`
During development, it's neccessary to add an adress to allowed hosts inside settings


Django signals:
---
- Signals can notify actions.
- In any models.py, import:
`from django.db.models.signals import (signal_name)`
- In the admin.py, import:
`form .models import (ModelName)`
- The structure of the block will vary.
- Migrate


Dependencies
---
- To skip the long list of installed dependencies, each dependency are frozed.
- In terminal:
`pip3 freeze > requirements.txt`
- To retrieve the requirements, in terminal: