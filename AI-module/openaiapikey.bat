@echo off
setlocal

set "API_KEY_FILE=.myapikey"

REM Проверка наличия файла .myapikey
if not exist "%API_KEY_FILE%" (
    echo Файл .myapikey не найден.
    pause
    exit /b
)

REM Чтение содержимого файла и присвоение значения переменной
set /p OPENAI_API_KEY=<"%API_KEY_FILE%"

REM Вывод значения переменной OPENAI_API_KEY
echo OPENAI_API_KEY=%OPENAI_API_KEY%

endlocal
cmd.exe /k
