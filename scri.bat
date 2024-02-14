@echo off

PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""C:\Users\tamer\Desktop\scr.ps1""' -Verb RunAs}"

pause