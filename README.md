<b> Django-Projects <b>

How to run project

1. Install Python (https://www.python.org/downloads/)
2. Download and install Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. Open Terminal or Command Prompt
4. Navigate to the location where you want to store your projects (e.g., "cd C:\Users\Your_Username")
5. Clone this repository by running command: git clone <a href = ""> </a>
6. After cloning, navigate into the folder containing the files from step 5 (e.g., "cd django-projects")
7. Make sure you have pip installed in your system. If not, download it from here https://pip.pypa.io/en/stable/installation/.
8. Make sure you have pip installed in your system. If not, download it from here https://pip.pypa.io/en/stable/installing/.
9. Run the server using python manage.py runserver in the terminal
10. Open a web browser and go to http://localhost:8000/ to see the application in action or http://127.0.0.1:8000/index
    Download Project or Clone Repository, extract files and move inside project folder, and type the following commands.

- Make sure you have activated the virtual environment(venv). If not use the following commands :
  virtualenv "virtual_environment_name"
  and then
  source "virtual_environment_name"/bin/activate or C:\Users\admin\your_path\virtual_env\Scripts\activate
  Run Command "pip install -r requirements.txt" (upgrade to the latest versions of packages)
  Run Command "python manage.py runserver / py manage.py runserver"
  For Calculator App
  "\*\*Change in settings.py 'DIRS': [os.path.join(BASE_DIR,'templates/calculatorapp')]"
