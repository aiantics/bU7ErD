import os, subprocess, ctypes, time
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDEN = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDEN)
with open("C:\\Windows\\SystemApps\\XHEN\\ASUSX1.txt", "r") as file:
    serial_number = file.read().strip()
with open("C:\\Windows\\SystemApps\\XHEN\\ASUSY2.txt", "r") as file:
    uuid_number = file.read().strip()
time.sleep(0.1)
command1 = f"C:\\Windows\\SystemApps\\XHEN\\dx11.exe /BS \"{serial_number}\""
command2 = f"C:\\Windows\\SystemApps\\XHEN\\dx11.exe /SU \"{uuid_number}\""
time.sleep(0.1)
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
time.sleep(1.0)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
time.sleep(0.1)
os.system("exit")