tested the following features manually


authentication
===
Can sign in to a superuser account:
---
- This was tested by creating a superuser. Run in terminal:
`python3 manage.py createsuperuser` and create a user.
- Run the server. The devloplemt Rest framework has a sign in button at the top right. Sign in with the credentials.
![authentication-signin](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/authentication-signin.png)
![authentication-signin-form](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/authentication-signin-form.png)

Can sign out from a superuser account.
---
The development Rest framework sign in button is replaced with a dropdown menu if the developer is already signed in.
![authentication-signout](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/authentication-signout.png)


Watch project:
===

Can retrieve existing watch-projects.
---
- by adding `/watch-project/` to the url, the development Rest framework will render data of watching projects.
![watch-project-retrieve]()

Can watch an existing project.
---
- When authenticated, scrolling down to the bottom will reveal a drop down menu of all projects you can watch.
- Picking one and click "POST" will make a post request.
![watch-project-watch](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/watch-project-watch.png)

If already watching a project, cannot submit it again until it is unwatched.
- The dropdown menu show all projects, including projects the user is already watching. By picking the same project twice, there will be a message displaying "detail": "risk of project 'double-watching'"
![watch-project-already-watching](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/watch-project-already-watching.png)


Can retrieve a watching project.
---
- By adding `/watch-project/{id}` to the url, with an existing index in place of {id}, in this test case 17, a single watching project is rendered.
![watch-project-detail]()

If authenticated, can unwatch the project.
---
- The test user in this test case "owns" the url `/watch-projects/17` but not `/watch-projects/16`.
- Inside `/watch-projects/17` a delete button is present, but absent in /16.
![watch-project-owner](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/watch-project-owner.png)
![watch-project-not-owner](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/watch-project-not-owner.png)


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
![projects-render](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-render.png)

Can create a new item with all fields empty, and the image will default to a placeholder.
---
- Being authenticated, and scrolling down to the bottom, there's a form field.
- Clicking "POST" will create a new project item according to given data.
![projects-create-form](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-create-form.png)
![projects-created](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-created.png)

Can filter projects belonging to an artist account.
---
- Inside the url `/projects/`, there's a "Filters" button next to "OPTIONS".
- Clicking the Filters button reveal a window with filtering options. Field filters have a top and a bottom dropdown menu.
- The bottom dropdown menu display all test superusers. Picking one superuser, then clicking Submit will render all projects only belonging to that test superuser.
![projects-filter-projects-window](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-filter-projects-window.png)
![projects-filter-projects-render](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-filter-projects-render.png)

Can filter watching projects unique to the signed-in artist account.
---
- This is tested the same way as for testing proejcts belonging to an artist, but by making a pick from the top dropdown field instead.
![projects-filter-watching-projects-window](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-filter-watching-projects-window.png)

Can add a Project Title, Project Description, Feature Poster, and Deployed Link.
---
- This can be tested the same way as creating a new project with empty fields, but by filling all the forms instead of leaving them empty.
![projects-create-form-filled](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-create-form-filled.png)
![projects-created-filled](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-created-filled.png)

If the Deployed Link is invalid, a reject message will occur.
---
- This can be tested by entering a regular string, such as "youtube"
![projects-create-invalid-link](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-create-invalid-link.png)

Can retrieve existing project ID.
---
- This can be tested by adding `/projects/{id}` to the URL, but with a valid index number in the place of {id}, such as 19.
- The page will render a single project.
![projects-render-single](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-render-single.png)

If not authenticated, the only option is to retrieve data.
---
- Unless the test superuser isn't the owner, it's neccessary to sign out, by clicking on the username at the top right, then sign out.
![projects-render-single-not-authenticated]()

If authenticated, can delete the project item.
---
- In the example image, the signed in superuser is the owner of project 19, therefore the delete button is present.
![projects-render-single](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-render-single.png)

If authenticated, can edit and save Project Title, Project Description, Feature Poster, and Deployed Link.
---
- For project example 19, the test superuser owning project 19 has to be signed in.
- At the bottom of the page, and at url `/projects/19/`, a form field is present if the test superuser is signed in.
- When editing the forms and clicking "PUT", the project item will save its changes.
![projects-edit](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-edit.png)
![projects-edited](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/projects-edited.png)


Documentation:
===

Can retrieve every documentation.
---
- By adding `/documentations/` to the URL, the api will render all documentations.
![documentaitons-render](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentaitons-render.png)

Can select a project and optionally add a title, paragraph and image, then add documentation.
---
- By signing in to a test superuser, the bottom will display a form field.
- The drop down menu render all projects, in this test example, project 20.
- When clicking "POST", a new item is created according to the filled forms.
![documentation-creating](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-creating.png)
![documentation-created](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-created.png)

Can filter by a project and see documentation belonging to that project.
---
- Inside the `/documentaitons/` URL, there's a Filters button in the corner.
- The Filters button reveal a window with a dropdown menu that reveal all the projects.
- In this example, picking project 20 will render documentaitons belonging to that project.
![documentation-filter-menu](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-filter-menu.png)
![documentation-filter](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-filter.png)

Can retrieve a single documentation item
---
- By adding `/documentations/{id}` with an index number in the place of {id}, in this example 5, a single documentation item is rendered.
![]()

Can edit and delete documentation the user owns.
---
- In this example, the signed in superuser is the owner for documentation item 5. At the bottom, a delete button is present, as well as an edit form at the bottom.
![documentation-owner](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-owner.png)
- When editing the fields, then clicking "PUT", the documentation item is updated according to the updated forms.
![documentation-editing](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-editing.png)
![documentation-edited](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-edited.png)
- Clicking the Delete button, and confirming the decision deleted documentation item 5.
![documentation-deleted](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-deleted.png)
- The signed in superuser in this test case is not the owner for documentaiton item 4. The delete and edit form are absent.
![documentation-not-owner](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/documentation-not-owner.png)


Artist account:
===

Can retrieve all the artist accounts on API.
---
- Adding `/art-accounts/` to the url will render all artist accounts.
![artist-account-render](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/artist-account-render.png)

Can retrieve details of one artist account.
---
- Adding `/art-accounts/{id}` to the url with a valid index number such as 1 in the place of {id} will render a single artist account.
![artist-account-render-single](https://raw.githubusercontent.com/MidnattLantern/HiDoc-API/main/readme_images/manual_test_api/artist-account-render-single.png)
