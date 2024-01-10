@echo off

:loop

net stop wuauserv
timeout /t 2

goto loop

