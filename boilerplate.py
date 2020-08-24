import os
from time import sleep

# Get current path

# Get application name from user
app_name = input("App name: ")
# Get the user to name the python files to put in app dir
py_files = []
# Get the user to name hmtl files to put templates
template_files = []


def createApp():
    global app_name
    # System commmand to create app with Poetry
    poetry_command = "poetry new " + app_name + " --name application"
    os.system(poetry_command)
    print("Running Poetry command...\n")

    os.chdir(app_name)

    # Create root app files
    os.system("touch config.py start.sh wsgi.py")
    print("Creating core files...\n")
    return


def createPyFiles():
    os.chdir("application")

    os.system('touch auth.py forms.py models.py routes.py')
    print("Creating project files...\n")
    os.chdir('..')

    return


def createStaticFolder():
    os.chdir("application")

    print("Creating static directories and files...\n")
    os.system('mkdir static')
    os.chdir('static')

    # make static folders
    os.mkdir('css')
    os.mkdir('js')
    os.mkdir('img')

    # return to parent folder
    os.chdir('..')

    # Create Templates Folder
    os.system('mkdir templates')
    os.chdir('templates')

    # make template files
    os.system('touch layout.html index.html')

    return


def openProject():
    # global app_name
    print(os.getcwd())
    os.chdir("../..")
    print(os.getcwd())
    os.system("code .")
    sleep(3)
    os.system("exit")


createApp()
createPyFiles()
createStaticFolder()
openProject()

"""
    Write default code in python and html files
    to include things like bootstrap or skeleton css
"""
