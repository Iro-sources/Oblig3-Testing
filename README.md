# Oblig3-Testing

## Here are the steps I went through
* I created a github repo "Oblig3-Testing" and created an empty folder in my pc called Oblig3.
* I opened the commandline in my pc and set up a working environment for my project and activated the virtual environment.  
* After that I opened the project in Pycharm and created Python file called *years.py* 
where I saved the function *isLeapYear* and the logic of the program.

### Installing dependencies to start testing
* I istalled ```pip install flake8 pytest pytest-cov``` and ```pip freeze > requirements.txt```
* When Intallations went well I created the test file *test_years.py* and run in the terminal ```pytest -v --cov```
to run my tests. 

### Setting up my continuous integration pipeline
I created a **circleci** folder and created inside it a configuration file called *config.yml*
At last I pushed all the files to git and sett up workflow. 
now everything is working as it's expected.


