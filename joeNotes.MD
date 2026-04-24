# ######################## .\.venv\Scripts\Activate.ps1

now this is very important, when working with venv to get the script to be recgonzied by the interpeter,
I need to open the command palette crtl + shift + p : search Python: Select Interperter select Enter interpreter path..    then give the path of the .venv the vm is in. 

.\.venv\Scripts\Activate.ps1

pip freeze > requirements.txt



a little bit of confusion on .venv with docker

it would appear I will use one .venv for the entire project and a Dockerfile for each service


