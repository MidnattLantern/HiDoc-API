HiDoc API was created from a preset model provided by Code Institute: https://github.com/Code-Institute-Org/ci-full-template

HIdoc-API is a Django REST Framework ("DRF") Application Programming Interface ("API").

The setup followed a step by step guide created by Code Institute. Source: https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn


Django and Rest:
---
In terminal:
`pip3 install 'django<4'`
Please ignore the notice message from the terminal that ask you to update.
- Why?
django<4 install a long term supported version of Django that is recomended over the newer version.

In terminal:
`pip3 install djangorestframework`
- Add to installed apps list


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


JWT token:
---
- The JTW token make HiDoc API more secure.
- In terminal:
`pip3 install dj-rest-auth==2.1.9`
- In settings.py, add in the installed apps:
`est_framework.authtoken`
`dj_rest_aut`
- in urls.py, add the link:
`path('dj-rest-auth/', include('dj_rest_auth.urls'))`
- migrate


Allauth:
---
- Django all-auth enable the user from the front-end to register.
- In terminal:
`pip3 install 'dj-rest-auth[with_social]'`
- add these apps:
django.contrib.sites
allauth
allauth.account
allauth.socialaccount
dj_rest_auth.registration
- beneath installed apps, add:
`SITE_ID = 1`
- inside urls.py, add:
`path('dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),`


Token
---
- In terminal:
´pip3 install djangorestframework-simplejwt´


Filter
---
The filter will be used in the front-end when browsing trough user projects and watch list.
- In terminal:
`pip3 install django-filter` (without an S at the end)
- Add `django-filters` to installed apps (with an S at the end)

Deployment (ElephantSQL)
---
1. HiDoc API is set up to store data on ElephantSQL. These are the steps taken for HiDoc API:
- On dashboard, click on "Create new instance" at the top right corner,
- The name given was "HiDoc-API", the plan for now remains as "tiny turtle", then click "Select Region",
- The region set for HiDoc is Stockholm. Click "Review",
- CLick "Create Instance",
- On the dashboard, click the name for HiDoc-API,
- There's a button that copy the URL link.
- From here, move on to Deployment (Heroku) from step 2.
4. Following steps should be taken after steps taken in Heroku and the IDE.
- In the database, click "browser",
- Click "Table queries", scroll down to "auth_user" (may have info within parantheses),
- Click execute,
- From here, move on to Deployment (IDE) from step 5.


Deployment (Heroku)
---
2. HiDoc API is hosted by Heroku. These are the steps taken for HiDoc API:
- On the dashboard, click "New", then "Create new app" at the top right corner,
- give-it-a-name-like-this, then click "create app",
- Inside the app, click "settings" at the nav-bar, then "reveal confog vars",
- Add the key "DATABASE_URL", and the value is what PostgrSQL copied from the copy URL step earlier. The value should begin with "postgres:/",
- From here, move on to Deployment (IDE) from step 3.
6. Following steps should be taken after steps taken in IDE.
- Ad these to the config vars:
Key: SECRET_KEY, Value: anything,
Key: CLOUDINARY_URL, Value: the cloudinary url used to host images,
Key: DISABLE_COLLECTSTATIC, Value: 1,
- Click deploy in the navbar, Github as deployment method, search for the repository name, then deploy.
- HiDoc is being deployed manually.
- Since this API will be used for a seperate front-end app, inside config vars, add this:
Key: "ALLOWED_HOST", value: the link to the Heroku app.
- Then replace the heroku app in allowed host with:
`os.environ.get('ALLOWED_HOST'),` This shouldn't result in a 400 error.
- 



Deployment (IDE)
---
3. These are steps taken in the IDE:
- In terminal:
` pip3 install dj_database_url==0.5.0 psycopg2`
- Inside settings.py, underneath `import os`, import:
`import dj_database_url`
- There was a block that needed to be replaced, please find `ref-1: updating database` in settings.py to see what that replacement looks like. This block will connect to ElephantSQL.
- From here, move on to Deployment (ElephantSQL) step 4.
5. Following steps should be taken after steps taken in ElephantSQL.
- In terminal, run:
`pip3 install gunicorn django-cors-headers`
- Add a profcile, so that Heroku can read it.
- Add the URL for Heroku to the list of allowed hosts inside settings.py,
- Add corsheaders to installed apps,
- Add to the top of the middleware list:
`'corsheaders.middleware.CorsMiddleware',`,
- Added client origin block, please see `ref-2: client origin` in settings.py, this help with communication between backend and frontend. And cookies.
- add this underneath the other JWT_AUTH:
`JWT_AUTH_SAMESITE = 'None'`,
- Change DEBUG to:
`'DEV' in os.environ`
- Reminder: freeze, in terminal:
`pip freeze --local > requirements.txt`
- form here, move on to Deployment (Heroku) from step 6.

Whitenoise:
---
During deployment for Heroku, the API may look differently. Although its function isn't lost, it may be nice to have the API look nice when you visit. Whitenoise attempt to fix that.
whitnoise `pip3 install whitenoise`


Agile:
===
- HiDoc was developed in reference to a training project by Code Institute: "Moments". That reference play a big role in the agile approach to HiDoc.
- To ensure that all the features were confident during development, some features are referenced and follow a similar structure to Moments. It's worth pointing out that althought there are many parallels, HiDoc didn't copy-paste its reference.
- Some features, such as search projects or artists was left behind in the first phase. HiDoc is functional without those features, and had to be comprimised due to time constrain.


Apps
===

views.py:
---
views.py import APIView and Response, which makes API visible.
views.py import Http404, to serve the purpose of perceiving anything non-existing.
views.py import status, which enable the API to understand the result of a given form.
The edit form is automatically generated by using `serializer_class = ArtAccountSerializer`.


urls.py:
---
urls.py import path,
For optimal maintainability, each component are sliced into many smaller pieces, the main urls.py inside art_acc folder connect the pieces. The main urls.py import `include` which allow it to connect these smaller pieces. This is useful in case a component need to exist but shouldn't be visible by the visitor.


serializers.py
---
Serializers convert data between JSON and Python


permissions.py
---
Stored inside drf_api, this file prevent non-owners from editing other's informaiton.
permissions.py import `permissions`, to make sure only the owner can make edits to their properties.


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


Artits account app:
---
- The "art_acc" model is responsible for authentication with ownership, or authority to CRUD.
- The model for artist account follow a similar structure to Code Institute's Moments tutorial model for profiles.
- Models use import of `User`, which enable the API to percieve individuals, i.e differenciate user-A from user-B.
- Models use import of `Signals`, which is a part of making it possible to register new users from the front-end.


Project app:
---
- The "project" model hold information about any user's project(s).
- The model for project follow a similar structure to Code Institute's Moments tutorial model for post.
- The agile approach only include a feature poster and description about the project. This is because the training reference don't include the more advancded features from the HiDoc user stories, and there's no certanity that they could be experimented before the deadline.


Comment app (unused):
---
Potential future feature.
- The "usr_comm" app remain unused in the front-end HiDoc for the moment. The app was developed for traning/ experimental purposes. However, being able to comment is such an expected feature in the modern day, this feature may or may not be implimented in the future.


Watch project:
---
- The "watch_proj" app is very similar to the conventional like feature in modern apps. The purpose is different from a like however, instead of expressing positive affirmation to the project owner, it serves as a bookmark like in modern e-books.
- When the user click Watch Project, that project will be listed inside their watch view, allowing the user to easily and find projects they think are interesting to stay updated for.
- There is a counter that show how many users are watching the project.
- Watching is a yes or no state. The serializer.py import `IntegrityError`, that's being used to prevent 'double-watching'. 


Watch artist (unused):
---
Potential future feature
- The "watch_art" app is HiDoc's equivalent to follow profile. This app remain unused in the front-end HiDoc for the moment. The app was developed for training/ experimental purposes. 


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


(Manual) Testing
---
In terminal, run:
`python3 manage.py test`
- manual testing performed inside project > tests.py


Struggles
---
- In case of "Bad Request 400" error in Heroku deployment, the Heroku link is probably not properly added to the allowed host list. Deployment with Debug = True will reveal precisely how the allowed host link should be written.


Unsolved:
---
- The individual view for artist accounts cannot show a counter for projects, watching, or being watch.


Credits:
---
- If you have access to Code Institute's (CI) advanced front-end drf_api project, you may spot similarities between this HiDoc's API and CI's API. However, CI's API project is a training project, and have been referenced for research and training purposes in development of HiDoc-API.
- Some icons are borrowed from Fond Awesome
- Some icons and graphical designs were designed by Alma Isaksson
- Developed by Alma Isaksson