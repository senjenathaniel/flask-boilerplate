import os

# Get current path

# Get application name from user
project_name = input("Project name: ")
app_name = input("Enter app name: ")
# Get the user to name the python files to put in app dir
py_files = []
# Get the user to name hmtl files to put templates
template_files = []


def createApp():
    global app_name
    # System commmand to create app with Poetry
    poetry_command = "poetry new " + project_name + " --name application"
    os.system(poetry_command)

    # Create root app files
    os.system("touch config.py start.sh wsgi.py")
    return


def createPyFiles():
    os.chdir(project_name + "/application")
    print(os.getcwd() + " :start CPY")

    # Create files
    os.system('touch auth.py forms.py models.py routes.py')

    # return to root folder
    os.chdir('..')
    print(os.getcwd() + " :end CPY")
    return


def createStaticFolder():
    # Change into the application dir
    global app_name
    
    os.chdir("application")

    print(os.getcwd() + " :start CSF")

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


createApp()
createPyFiles()
createStaticFolder()

"""
    Write default code in python and html files
    to include things like bootstrap or skeleton css
"""
