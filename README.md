HiDoc API was created from a preset model provided by Code Institute: https://github.com/Code-Institute-Org/ci-full-template

HIdoc-API is a Django REST Framework ("DRF") Application Programming Interface ("API").

The setup followed a step-by-step guide created by Code Institute. Source: https://docs.google.com/document/d/1LCLxWhmW_4VTE4GXsnHgmPUwSPKNT4KyMxSH8agbVqU/edit#heading=h.mpopj7v69qqn

Frontend repository: https://github.com/MidnattLantern/hidoc.git


Setup
===

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
`rest_framework.authtoken`
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


Deployment
===

There will be some jumping back and forward between ElephantSQL, Heroku, and IDE during the process of deployment.


ElephantSQL: The HiDoc API is set up to store data on ElephantSQL. These are the steps taken for HiDoc API:
- The website for ElephantSQL is below, create an account if you haven’t already:
https://www.elephantsql.com/

- On the dashboard, click on "Create new instance" at the top right corner,
![API-deployment-1](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-1.png)

- The name given was "HiDoc-API", the plan for now remains as "tiny turtle", then click "Select Region" at the bottom right corner,
![API-deployment-2](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-2.png)

- The region set for HiDoc is Stockholm. Click "Review",
![API-deployment-3](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-3.png)

- Click "Create Instance in “the bottom right corner,
![API-deployment-4](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-4.png)

- On the dashboard, click the name for HiDoc-API,
![API-deployment-5](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-5.png)

- There's a button that copies the URL link.
![API-deployment-6](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-6.png)

Heroku: HiDoc API is hosted by Heroku. These are the steps taken for HiDoc API:
- The website for Heroku is below, create an account if you haven’t already:
https://www.heroku.com/home

- On the dashboard, click "New", then "Create new app" at the top right corner,
![API-deployment-7](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-7.png)

- give-it-a-name-like-this, choose Europe, then click "create app",
![API-deployment-8](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-8.png)

- Inside the app, click "settings" at the nav bar, then "reveal config vars",
![API-deployment-9](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-9.png)

- Add the key "DATABASE_URL", and the value is what PostgreSQL copied from the copy URL step earlier. The value should begin with "postgres:/",
![API-deployment-10](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-10.png)

IDE: These are the steps taken in the IDE:

- Create a `Procfile` in the root directory, so that the API can be read by Heroku. Then add the following inside that file:
`
release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn drf_api.wsgi
`
![API-deployment-procfile](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-procfile.png)
![API-deployment-16](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-16.png)

- Install psycopg3 in the terminal:
` pip3 install dj_database_url==0.5.0 psycopg2`

- Inside settings.py, underneath `import os`, import:
`import dj_database_url`
![API-deployment-11](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-11.png)

- There was a block that needed to be replaced, please find `ref-1: updating database` in settings.py to see what that replacement looks like. This block will connect to ElephantSQL.
![API-deployment-12](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-12.png)

ElephantSQL:
- In the database, click "browser",
![API-deployment-13](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-13.png)

- Click "Table queries", scroll down to "auth_user" (may have info within parentheses),
![API-deployment-14](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-14.png)

- Click execute,
![API-deployment-15](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-15.png)

IDE: following steps:
- Install Gunicorn Django Cors headers. In the terminal, run:
`pip3 install gunicorn django-cors-headers`

- Add the URL for Heroku to the list of allowed hosts inside settings.py,

- Add corsheaders to installed apps,
![API-deployment-17](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-17.png)

- Add to the top of the middleware list:
`'corsheaders.middleware.CorsMiddleware',`,
![API-deployment-18](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-18.png)

- Added client origin block, please see `ref-2: client origin` in settings.py, this helps with communication between the backend, front end, and cookies.
![API-deployment-19](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-19.png)

- add this line underneath the other JWT_AUTH:
`JWT_AUTH_SAMESITE = 'None'`,
![API-deployment-20](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-20.png)

- Change DEBUG to:
`'DEV' in os.environ`

- Reminder: freeze, in terminal:
`pip freeze --local > requirements.txt`

Heroku: following steps:
- Add these to the config vars:
Key: SECRET_KEY, Value: anything of choice,
Key: CLOUDINARY_URL, Value: the Cloudinary URL used to host images,
Key: DISABLE_COLLECTSTATIC, Value: 1,
![API-deployment-21](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-21.png)

- Click deploy in the navbar, Github as the deployment method, search for the repository name, and then deploy.
![API-deployment-22](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-22.png)
![API-deployment-23](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-23.png)

- HiDoc is being deployed manually.
- Since this API will be used for a separate front-end app, inside config vars, add this:
Key: "ALLOWED_HOST", value: the link to the Heroku app.
![API-deployment-24](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-24.png)

IDE: following steps:
replace the Heroku app in the allowed host with:
`os.environ.get('ALLOWED_HOST'),` This shouldn't result in a 400 error.
![API-deployment-25](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/api_heroku_deployment/api-deployment-25.png)

Whitenoise:
---
During deployment for Heroku, the API may look different. Although its function isn't lost, it may be nice to have the API look nice when you visit. Whitenoise attempted to fix that.
whitnoise `pip3 install whitenoise`.


Agile:
===
- HiDoc was developed about a training project by Code Institute: "Moments". That reference plays a big role in the agile approach to HiDoc.
- To ensure that all the features were confident during development, some features are referenced and follow a similar structure to Moments. It's worth pointing out that although there are many parallels, HiDoc didn't copy-paste its reference.
- Some features, such as search projects or artists were left behind in the first phase. HiDoc is functional without those features and had to be compromised due to time constrain.


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
Serializers convert data between JSON and Python.


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


Testing
===

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
The following can also be found inside manual testing.md with screenshots.
tested the following features manually


authentication
===
Can sign in to a superuser account:
---
- This was tested by creating a superuser. Run in terminal:
`python3 manage.py createsuperuser` and create a user.
- Run the server. The devloplemt Rest framework has a sign in button at the top right. Sign in with the credentials.

Can sign out from a superuser account.
---
The development Rest framework sign in button is replaced with a dropdown menu if the developer is already signed in.


Watch project:
===

Can retrieve existing watch-projects.
---
- by adding `/watch-project/` to the url, the development Rest framework will render data of watching projects.

Can watch an existing project.
---
- When authenticated, scrolling down to the bottom will reveal a drop down menu of all projects you can watch.
- Picking one and click "POST" will make a post request.

If already watching a project, cannot submit it again until it is unwatched.
- The dropdown menu show all projects, including projects the user is already watching. By picking the same project twice, there will be a message displaying "detail": "risk of project 'double-watching'"


Can retrieve a watching project.
---
- By adding `/watch-project/{id}` to the url, with an existing index in place of {id}, in this test case 17, a single watching project is rendered.

If authenticated, can unwatch the project.
---
- The test user in this test case "owns" the url `/watch-projects/17` but not `/watch-projects/16`.
- Inside `/watch-projects/17` a delete button is present, but absent in /16.


Watch artist (unused/ future feature):
===

/watch-artists/
---
Can retrieve existing watch-artists.
Can watch an artist.
If already watching an artist, cannot submit it again until unwatched.

/watch-artists/{id}
---
Can retrieve an artist.
If authenticated, can unwatch the artist.


User comment (unused/ future feature):
===

/user-comments/ 
---
Can retrieve all the comments on the API.
Can create a comment.
! Cannot filter to a project.

user-comments/{id}
---
If the owner can edit and delete a comment.


project:
===

Can retrieve all projects view.
---
- By adding `/projects/` to the URL, a list of all existing projects are rendered.

Can create a new item with all fields empty, and the image will default to a placeholder.
---
- Being authenticated, and scrolling down to the bottom, there's a form field.
- Clicking "POST" will create a new project item according to given data.

Can filter projects belonging to an artist account.
---
- Inside the url `/projects/`, there's a "Filters" button next to "OPTIONS".
- Clicking the Filters button reveal a window with filtering options. Field filters have a top and a bottom dropdown menu.
- The bottom dropdown menu display all test superusers. Picking one superuser, then clicking Submit will render all projects only belonging to that test superuser.

Can filter watching projects unique to the signed-in artist account.
---
- This is tested the same way as for testing proejcts belonging to an artist, but by making a pick from the top dropdown field instead.

Can add a Project Title, Project Description, Feature Poster, and Deployed Link.
---
- This can be tested the same way as creating a new project with empty fields, but by filling all the forms instead of leaving them empty.

If the Deployed Link is invalid, a reject message will occur.
---
- This can be tested by entering a regular string, such as "youtube"

Can retrieve existing project ID.
---
- This can be tested by adding `/projects/{id}` to the URL, but with a valid index number in the place of {id}, such as 19.
- The page will render a single project.
![projects-render-single](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-render-single.png)

If not authenticated, the only option is to retrieve data.
---
- Unless the test superuser isn't the owner, it's neccessary to sign out, by clicking on the username at the top right, then sign out.

If authenticated, can delete the project item.
---
- In the example image, the signed in superuser is the owner of project 19, therefore the delete button is present.

If authenticated, can edit and save Project Title, Project Description, Feature Poster, and Deployed Link.
---
- For project example 19, the test superuser owning project 19 has to be signed in.
- At the bottom of the page, and at url `/projects/19/`, a form field is present if the test superuser is signed in.
- When editing the forms and clicking "PUT", the project item will save its changes.


Documentation:
===

Can retrieve every documentation.
---
- By adding `/documentations/` to the URL, the api will render all documentations.

Can select a project and optionally add a title, paragraph and image, then add documentation.
---
- By signing in to a test superuser, the bottom will display a form field.
- The drop down menu render all projects, in this test example, project 20.
- When clicking "POST", a new item is created according to the filled forms.

Can filter by a project and see documentation belonging to that project.
---
- Inside the `/documentaitons/` URL, there's a Filters button in the corner.
- The Filters button reveal a window with a dropdown menu that reveal all the projects.
- In this example, picking project 20 will render documentaitons belonging to that project.

Can retrieve a single documentation item
---
- By adding `/documentations/{id}` with an index number in the place of {id}, in this example 5, a single documentation item is rendered.
![]()

Can edit and delete documentation the user owns.
---
- In this example, the signed in superuser is the owner for documentation item 5. At the bottom, a delete button is present, as well as an edit form at the bottom.
- When editing the fields, then clicking "PUT", the documentation item is updated according to the updated forms.
- Clicking the Delete button, and confirming the decision deleted documentation item 5.
- The signed in superuser in this test case is not the owner for documentaiton item 4. The delete and edit form are absent.


Artist account:
===

Can retrieve all the artist accounts on API.
---
- Adding `/art-accounts/` to the url will render all artist accounts.

Can retrieve details of one artist account.
---
- Adding `/art-accounts/{id}` to the url with a valid index number such as 1 in the place of {id} will render a single artist account.



Struggles
---
- In case of a "Bad Request 400" error in Heroku deployment, the Heroku link is probably not properly added to the allowed host list. Deployment with Debug = True will reveal precisely how the allowed host link should be written.


Validation
===

The following can also be found inside validation.md

Validated using https://pep8ci.herokuapp.com/ 
The following files have been validated:
watch_proj > views.py
watch_proj > urls.py
watch_proj > tests.py
watch_proj > serializers.py
watch_proj > models.py
watch_art > views.py
watch_art > urls.py
watch_art > serializers.py
watch_art > models.py
usr_comm > views.py
usr_comm > urls.py
usr_comm > serializers.py
ust_comm > models.py
project > views.py
project > urls.py
project > tests.py
project > serializers.py
project > models.py
drf_api > views.py
drf_api > urls.py
drf_api > serializers.py
documentation > views.py
documentation > urls.py
documentation > serializers.py
documentation > models.py
documentation > views.py
documentation > urls.py
documentation > serializers.py
documentation > models.py


Credits:
---
- If you have access to Code Institute's (CI) advanced front-end drf_api project, you may spot similarities between this HiDoc's API and CI's API. However, CI's API project is a training project and has been referenced for research and training purposes in the development of HiDoc-API.
- Some icons are borrowed from Fond Awesome
- Some icons and graphical designs were designed by Alma Isaksson
- Developed by Alma Isaksson