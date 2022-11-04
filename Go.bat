@echo off
rem echo hello my name is yongwon
cls
cd > locatio.txt
set /p pwd=<locatio.txt

call conda activate base
call python %pwd%\attend.py
exit