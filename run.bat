echo Activating virtual environment...
call venv\Scripts\activate.bat

python run.py

del /Q src\*.*

timeout /t 1

START build\

echo  END!

timeout /t 3

exit