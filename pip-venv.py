# Package Vs Module
# Both modules and packages organize and structure the code but serve different purposes. 
# Module - It is a single file containing Python code
# Package - It is a collection of modules that are organized in a directory hierarchy

# To see the list of packages visit:  https://pypi.org/

# PIP - Preferred Installer Program  or some say PIP Installs Packages
# It is used to install packages which are by default not included in Python like math, requests, etc.

# Commands

# $ pip install <package_name>

# If you do not have pip installed then try the following command where -m = package
# $ py -m pip install <package_name>


# If you get the error - 
# Could not install packages due to an OSError: [WinError 2] The system cannot find the file specified:
# $ pip install <package_name> --user

# This will install the package globally which means the package is available to all the python files you create

# To list all the packages installed by pip
# $ pip list

# To install a particular version
# $ pip install <package_name>==<version>

# Above command will unistall any other version and install the version you mentioned

# To update a package to a current release
# $ pip install -U <package_name>

# To uninstall a package
# $ pip uninstall <package_name>

# To see the dependencies of a package
# $ pip show <package_name>

# VENV - Virtual Environment
# It may happen that one app needs a different version of a package than what is needed by other apps
# for the same package. For these situations we can use VENV
# They are used for development but do not commit them to code repo
# Create a VENV

# $ py -m venv .<venv_name>         # This will create a .venv and few other folders

# Now we need to activate this everytime you need to work on your project
# $ .venv/Scripts/activate

# To come to the global environment you need deactivate your env. Use the command:
# $ deactivate

# To avoid pushing out venv to Git we need to create a requirements file which will contain all the dependencies
# $ pip freeze > requirements.txt

# requirements.txt file will tell other users what needs to be installed to run this project

