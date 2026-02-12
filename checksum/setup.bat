@ECHO OFF
REM setup.bat template

REM Set the PYTHONDIR to path for python.exe (must end in \)
SET PYTHONDIR=C:\Programs\Python\
IF NOT EXIST %PYTHONDIR%python.exe (
  ECHO No python.exe in %PYTHONDIR%
  ECHO Patch line 4 in %~f0
  EXIT /b
)

ECHO Creating virtual Python environment
REM Create new private "virtual python environment"
%PYTHONDIR%python.exe -m venv env
REM Activate the new environment
CALL env\Scripts\activate.bat
REM From new Python env, upgrade pip, quietly
ECHO Upgrading pip
python -m pip install -q --upgrade pip setuptools wheel
REM Add python packages to new environment
ECHO Adding packages
IF EXIST requirements.txt (
   pip install -q -r requirements.txt
)

ECHO.Setup done, now use run

