import os, subprocess, ctypes, time, random
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDEN = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDEN)
first_digit = '2'
remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(14))
serial_number = first_digit + remaining_digits
time.sleep(0.1)
command1 = f"C:\\Windows\\SystemApps\\XHEN\\dx11.exe /BS \"{serial_number}\""
command2 = f"C:\\Windows\\SystemApps\\XHEN\\dx11.exe /SU AUTO"
time.sleep(0.1)
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
time.sleep(0.4)
subprocess.run(command1, shell=True)
subprocess.run(command2, shell=True)
time.sleep(1.0)
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
time.sleep(0.1)
os.system("exit")