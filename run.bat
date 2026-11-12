@echo off
chcp 65001 > nul
echo Запуск веб-сайту "Розклад руху потягів"...

cd /d %~dp0


call env\Scripts\activate.bat


start http://127.0.0.1:8000/


python manage.py runserver

pause