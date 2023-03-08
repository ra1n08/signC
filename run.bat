@echo off
echo activating virtual enviroment...
call ./signC/Scripts/activate
echo activated virtual enviroment (signC)
@REM timeout 1
echo installing requirements lib for application
python -m pip install -r ./requirements.txt
echo installed!
@REM timeout 1
echo running application...
echo application debug in here!
python main.py
