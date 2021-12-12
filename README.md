Python virtual invironment



install- pip install virtualenv

create -virtualenv venv

virtual environment with install pakages-  virtualenv --system-site-packages venv



show directory - dir

active- venv/scripts/activate

deactive - deactivate

create django project - django-admin startproject weatherapp

previous dirctory - cd..

open with vscode- code .



see install python pakage- pip list

change execution policy from admin in virtual environment- set-executionpolicy remotesigned

//////////////////////////////////////////////////////

create note which pakage is installed in python- pip freeze > requirements.txt

install all file from requirements.txt- pip install -r .\requirements.txt



//////////////////////////////////mongo/////////////////

show location of database = db.adminCommand("getCmdLineOpts")

//////////////////////////git help/////////////////
https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line

//commands///
echo "# react_firebase_quiz_app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/maruf3684/react_firebase_quiz_app.git
git push -u origin main
