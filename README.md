HiDoc API was created from a preset model provided by Code Institute: https://github.com/Code-Institute-Org/ci-full-template

HIdoc-API is a Django REST Framework ("DRF") Application Programming Interface ("API").

The setup followed a step-by-step guide created by Code Institute. Source: https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn


Django and Rest:
---
In terminal:
`pip3 install 'django<4'`
Please ignore the notice message from the terminal that asks you to update.
- Why?
django<4 Install a long-term supported version of Django that is recommended over the newer version.

In terminal:
`pip3 install djangorestframework`
- Add to the installed apps list


Images:
---
Images are hosted by Cloudinary.
Images are used for the Artist's profile picture, documentation, and project thumbnail.

Cloudinary will add a hash to prevent duplication errors if any user uploads an image with a generic name such as image.PNG
In terminal:
`pip3 install django-cloudinary-storage`

Images are processed with Pillow.
In terminal:
`pip3 install Pillow`
- Why?
Cloudinary alone serve to store images and videos, it does not provide services to update and process them.

The settings are: CLOUDINARY_STORAGE, MEDIA_URL, and DEFAULT_FILE_STORAGE


JWT token:
---
- The JTW token makes HiDoc API more secure.
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
- Django all-auth enable the user from the front end to register.
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
The filter will be used in the front end when browsing through user projects and watch lists.
- In terminal:
`pip3 install django-filter` (without an S at the end)
- Add `django-filters` to installed apps (with an S at the end)

Deployment (ElephantSQL)
---
1. HiDoc API is set up to store data on ElephantSQL. These are the steps taken for HiDoc API:
- On the dashboard, click on "Create new instance" at the top right corner,
- The name given was "HiDoc-API", the plan for now remains as "tiny turtle", then click "Select Region",
- The region set for HiDoc is Stockholm. Click "Review",
- Click "Create Instance",
- On the dashboard, click the name for HiDoc-API,
- There's a button that copies the URL link.
- From here, move on to Deployment (Heroku) from step 2.
4. The following steps should be taken after steps taken in Heroku and the IDE.
- In the database, click "browser",
- Click "Table queries", scroll down to "auth_user" (may have info within parentheses),
- Click execute,
- From here, move on to Deployment (IDE) from step 5.


Deployment (Heroku)
---
2. HiDoc API is hosted by Heroku. These are the steps taken for HiDoc API:
- On the dashboard, click "New", then "Create new app" at the top right corner,
- give-it-a-name-like-this, then click "create app",
- Inside the app, click "settings" at the nav bar, then "reveal config vars",
- Add the key "DATABASE_URL", and the value is what PostgreSQL copied from the copy URL step earlier. The value should begin with "postgres:/",
- From here, move on to Deployment (IDE) from step 3.
6. The following steps should be taken after steps taken in IDE.
- Add these to the config vars:
Key: SECRET_KEY, Value: anything,
Key: CLOUDINARY_URL, Value: the Cloudinary URL used to host images,
Key: DISABLE_COLLECTSTATIC, Value: 1,
- Click deploy in the navbar, Github as the deployment method, search for the repository name, and then deploy.
- HiDoc is being deployed manually.
- Since this API will be used for a separate front-end app, inside config vars, add this:
Key: "ALLOWED_HOST", value: the link to the Heroku app.
- Then replace the Heroku app in the allowed host with:
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
5. The following steps should be taken after the steps taken in ElephantSQL.
- In the terminal, run:
`pip3 install gunicorn django-cors-headers`
- Add a profcile, so that Heroku can read it.
- Add the URL for Heroku to the list of allowed hosts inside settings.py,
- Add corsheaders to installed apps,
- Add to the top of the middleware list:
`'corsheaders.middleware.CorsMiddleware',`,
- Added client origin block, please see `ref-2: client origin` in settings.py, this helps with communication between the backend and frontend. And cookies.
- add this underneath the other JWT_AUTH:
`JWT_AUTH_SAMESITE = 'None'`,
- Change DEBUG to:
`'DEV' in os.environ`
- Reminder: freeze, in terminal:
`pip freeze --local > requirements.txt`
- from here, move on to Deployment (Heroku) from step 6.

Whitenoise:
---
During deployment for Heroku, the API may look different. Although its function isn't lost, it may be nice to have the API look nice when you visit. Whitenoise attempted to fix that.
whitnoise `pip3 install whitenoise`


Agile:
===
- HiDoc was developed about a training project by Code Institute: "Moments". That reference plays a big role in the agile approach to HiDoc.
- To ensure that all the features were confident during development, some features are referenced and follow a similar structure to Moments. It's worth pointing out that although there are many parallels, HiDoc didn't copy-paste its reference.
- Some features, such as search projects or artists were left behind in the first phase. HiDoc is functional without those features and had to be compromised due to time constrain.

large images
---
- The code suggests that there's a limit to the size of an image upload. As of writing this, large images pass the validation code. Passing large images could be a concern for the wallet if HiDoc were to become popular, but for my deadline, I have more important things to work on.
- It's worth putting a pin on this when HiDoc is maintained in the future. It's not free to store millions of images larger than 1 MB on Cloudinary.


Apps
===

views.py:
---
views.py imports APIView and Response, which makes API visible.
views.py import Http404, to serve the purpose of perceiving anything non-existing.
views.py import status, which enables the API to understand the result of a given form.
The edit form is automatically generated by using `serializer_class = ArtAccountSerializer`.


urls.py:
---
urls.py import path,
For optimal maintainability, each component is sliced into many smaller pieces, and the main urls.py inside the art_acc folder connects the pieces. The main urls.py import `include` which allows it to connect these smaller pieces. This is useful in case a component needs to exist but shouldn't be visible to the visitor.


serializers.py
---
Serializers convert data between JSON and Python


permissions.py
---
Stored inside drf_api, this file prevents non-owners from editing other's information.
permissions.py import `permissions`, to make sure only the owner can make edits to their properties.


env.py:
---
The environment file (env.py) is only available to the developer (s). The env.py file accesses sensitive environments, such as Cloudinary.
The contents are:
`
import os
os.environ['CLOUDINARY_URL'] = '(Cloudinary API adress)'
`

These lines must exist in settings.py:
`
import os
is os.path.exists('env.py'):
    import env
`
- Why?
During development: settings.py needs to link up env.py so that it can be read and used.


Project:
---
In terminal:
`django-admin startproject drf_api .`


Apps:
---
- To create an app, run in the terminal:
`python3 manage.py startapp (app_name)`
- HiDoc API created these apps:
"art_acc" (artist account)


Artists account app:
---
- The "art_acc" model is responsible for authentication with ownership, or authority to CRUD.
- The model for artist accounts follows a similar structure to Code Institute's Moments tutorial model for profiles.
- Models use import of `User`, which enables the API to perceive individuals, i.e. differentiate user-A from user-B.
- Models use the import of `Signals`, which is a part of making it possible to register new users from the front end.


Project app:
---
- The "project" model holds information about any user's project(s).
- The project model follows a similar structure to Code Institute's Moments tutorial model for post.
- The agile approach only includes a feature poster and description of the project. This is because the training reference doesn't include the more advanced features from the HiDoc user stories, and there's no certainty that they could be experimented with before the deadline.


Comment app (unused):
---
Potential future feature.
- The "usr_comm" app remains unused in the front-end HiDoc for the moment. The app was developed for training/ experimental purposes. However, being able to comment is such an expected feature in the modern day, this feature may or may not be implemented in the future.


Watch project:
---
- The "watch_proj" app is very similar to the conventional feature in modern apps. The purpose is different from a like however, instead of expressing positive affirmation to the project owner, it serves as a bookmark like in modern e-books.
- When the user clicks Watch Project, that project will be listed inside their watch view, allowing the user to easily find projects they think are interesting to stay updated for.
- There is a counter that shows how many users are watching the project.
- Watching is a yes or no state. The serializer.py import `IntegrityError`, that's being used to prevent 'double-watching'. 

Watch artist (unused):
---
Potential future feature
- The "watch_art" app is HiDoc's equivalent to follow profile. This app remains unused in the front-end HiDoc for the moment. The app was developed for training/ experimental purposes. 

Documentation
---
- The owner of a project can add content to, by the intention of HiDoc, document their process.
- Documentation is related to the Project.
- Technically, any artist COULD document another artist's project. This, obviously is restricted in the front end, where only the owner of a project can access this feature.



Run server:
---
To test the app, run this in the terminal:
`python3 manage.py runserver`
During development, it's necessary to add an address to allow hosts inside the settings


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
- To skip the long list of installed dependencies, each dependency is frozen.
- In terminal:
`pip3 freeze > requirements.txt`
- To retrieve the requirements, in the terminal:


(Manual) Testing
---
In the terminal, run:
`python3 manage.py test`
- Manual testing performed inside project > tests.py


Struggles
---
- In case of a "Bad Request 400" error in Heroku deployment, the Heroku link is probably not properly added to the allowed host list. Deployment with Debug = True will reveal precisely how the allowed host link should be written.


Unsolved:
---
- The individual view for artist accounts cannot show a counter for projects, watching, or being watched.


Credits:
---
- If you have access to Code Institute's (CI) advanced front-end drf_api project, you may spot similarities between this HiDoc's API and CI's API. However, CI's API project is a training project and has been referenced for research and training purposes in the development of HiDoc-API.
- Some icons are borrowed from Fond Awesome
- Some icons and graphical designs were designed by Alma Isaksson
- Developed by Alma Isaksson