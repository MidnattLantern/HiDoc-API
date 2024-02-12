tested the following features manually

authentication
---
Can sign in to a superuser account.
Can sign out from a superuser account.


Watch project:
===

/watch-project/
---
Can retrieve existing watch-projects.
Can watch an existing project.
If already watching a project, cannot submit it again until it is unwatched.

/watch-project/{id}
---
Can retrieve a watching project.
If authenticated, can unwatch the project.


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

/projects/
---
Can retrieve all projects view.
Can create a new item with all fields empty, and the image will default to a placeholder.
Can filter projects belonging to an artist account.
Can filter watching projects unique to the signed-in artist account.
Can add a Project Title, Project Description, Feature Poster, and Deployed Link.
If the Deployed Link is invalid, a reject message will occur.

/projects/{id}
---
Can retrieve existing project ID.
If not authenticated, the only option is to retrieve data.
If authenticated, can delete the project item.
If authenticated, can edit and save Project Title, Project Description, Feature Poster, and Deployed Link.
If the Deployed Link is invalid, a reject message will occur.
! If an image is too large, a reject message will occur.


Documentation:
===

/documentations/ :
---
Can retrieve every documentation.
Can select a project and optionally add a title, paragraph and image, then add documentation.
Can filter by a project and see documentation belonging to that project.

/documentations/{id} :
---
Can delete documentation the user owns.
Can edit documentation the user owns.


Artist account:
===

/art-accounts/
---
Can retrieve all the artist accounts on API.

/art-accounts/{id}
---
Can retrieve details of one artist account.