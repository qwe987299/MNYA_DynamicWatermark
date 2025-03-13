REM 啟動虛擬環境
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM 執行程式
python run.py

REM 刪除 src 目錄內所有檔案
del /Q src\*.*