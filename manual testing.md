authenticatino
---
Can sign in to a superuser account.
Can sign out from a superuser account.

/projects/
---
Can retrieve all projects view.
Can create new item with all fields empty, the image will default to a placeholder.
Can filter projects belonging to an artist account.
Can filter watching projects uniqure to the signed in artist account.
Can add Project Title, Project Description, Feature Poster, Deployed Link.
If Deployed Link is invalid, a reject message will occur.

/projects/{id}
---
Can retrieve existing project id.
If not authenticated, the only option is to retrieve data.
If authenticated, can delete project item.
If authenticated, can edit and save Project Title, Project Description, Feature Poster, Deployed Link.
If Deployed Link is invalid, a reject message will occur.
! If an image is too large, a reject message will occur.

/watch-artists/
---
Can retrieve existing watch-artists.
Can watch an artist.
If aleady watching an artist, cannot submit again until unwatched.

/watch-artists/{id}
---
Can retrieve an artist.
If authenticated, can unwatch artist.

/watch-project/
---
Can retrieve existing watch-projects.
Can watch an existing project.
If already watching a project, cannot submit again until unwatched.

/watch-project/{id}
---
Can retrieve a watching project.
If authenticated, can unwatch project.