@ECHO OFF

REM If Python is not in your PATH set the PYTHONDIR manually (must end in \)
SET PYTHONDIR=C:\Programs\Python\

ECHO Found Python; creating virtual env
%PYTHONDIR%python.exe -m venv env
CALL env\Scripts\activate.bat
env\Scripts\python -m pip install --upgrade pip setuptools wheel
IF EXIST requirements.txt (
   pip install -r requirements.txt
)
ECHO 'setup' done, now 'run'
