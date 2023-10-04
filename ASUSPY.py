import os, subprocess, ctypes, time
username = os.path.basename(os.path.normpath(os.path.expanduser("~")))
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDEN = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDEN)
with open(f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\ASUSX1.txt", "r") as file:
    serial_number = file.read().strip()
with open(f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\ASUSY2.txt", "r") as file:
    uuid_number = file.read().strip()
command1 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-VR90EX\\dx11.exe /BS \"{serial_number}\""
command2 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-VR90EX\\dx11.exe /SU \"{uuid_number}\""
command3 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-MP120G\\dx11.exe /BS \"{serial_number}\""
command4 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-MP120G\\dx11.exe /SU \"{uuid_number}\""
command5 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-LOP19J\\dx11.exe /BS \"{serial_number}\""
command6 = f"C:\\Users\\{username}\\AppData\\Local\\XHEN\\D-LOP19J\\dx11.exe /SU \"{uuid_number}\""
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
subprocess.run(command3, shell=True)
subprocess.run(command4, shell=True)
subprocess.run(command5, shell=True)
subprocess.run(command6, shell=True)
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
time.sleep(3)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
os.system("exit")
