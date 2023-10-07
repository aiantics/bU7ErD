import os, subprocess, ctypes, time, random
username = os.path.basename(os.path.normpath(os.path.expanduser("~")))
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDEN = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDEN)
first_digit = '2'
remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(14))
serial_number = first_digit + remaining_digits
command1 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-VR90EX\\dx11.exe" /BS \"{serial_number}\"'
command2 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-VR90EX\\dx11.exe" /SU AUTO'
command3 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-MP120G\\dx11.exe" /BS \"{serial_number}\"'
command4 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-MP120G\\dx11.exe" /SU AUTO'
command5 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-LOP19J\\dx11.exe" /BS \"{serial_number}\"'
command6 = f'"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-LOP19J\\dx11.exe" /SU AUTO'
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
subprocess.run(command3, shell=True)
subprocess.run(command4, shell=True)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
subprocess.run(command5, shell=True)
subprocess.run(command6, shell=True)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
time.sleep(3)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
os.system("exit")
