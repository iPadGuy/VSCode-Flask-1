**README**

# Visual Studio Code Tutorial for Flask

### References
- https://code.visualstudio.com/docs/python/tutorial-flask
- https://code.visualstudio.com/docs/editor/userdefinedsnippets
- https://code.visualstudio.com/docs/containers/quickstart-python


##### Saturday, October 24, 2020
- This tutorial is much like the one for Django

##### Sunday, October 25, 2020
- I played with the Jinja2 templating subsystem quite a bit, putting links on the home page.
    - I downloaded the latest Bootstrap, for future-use
- One big difference I notice between Flask and Django is that Django supports DateTime objects in the template
- I am not wild about the naming conventions used in this tutorial--I much prefer Miguel's, which are very similar to those used in Django.
- I finished the main part of the tutorial, and will finish the extra parts for future development (this is something that wasn't in the Django tutorial).


##### Monday, October 26, 2020
- TODO: Finish the "Refactor" and Docker parts of the tutorial
- Already, I am wondering which of the following is the better way to go:
    1. Entry point at the top (ie. `./microblog.py`)
    2. Entry point in the app folder (ie. `app/webapp.py`)
- Refactoring was fairly easy, but I used `app` instead of `hello_app` for the app directory name.
- Going through the Docker tutorial again, this time using Flask, instead of Django.
    1. Create Dockerfile from the Command Palette
        a. In the Dockerfile, I changed `FROM python:3.8-slim-buster` to `FROM python:3.9-slim-buster` (After checking that the Docker image exists)
    2. From the Debug pane, choose "Dockerfile: Python - Flask"
    3. Run in the debugger (everything works)
- TODO: Need to try this in PyCharm Pro, since it has Dockerfile support

