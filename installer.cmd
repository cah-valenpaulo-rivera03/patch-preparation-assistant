python -m pip install virtualenv --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
python -m virtualenv .venv
call .venv\Scripts\activate
python -m pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
mkdir output