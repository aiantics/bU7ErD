import os, subprocess, ctypes, random
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDEN = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDEN)
def get_motherb():
	command = "wmic baseboard get serialnumber"
	result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
	return result.stdout.strip()
def get_smbios():
	command = "wmic csproduct get uuid"
	result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
	return result.stdout.strip()
stock_motherb = get_motherb()
stock_smbios = get_smbios()
usernamereal = os.path.basename(os.path.normpath(os.path.expanduser("~")))
file_path = f"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSAS\\x1.txt"
file_path2 = f"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSAS\\x2.txt"
try:
	if os.path.exists(file_path):
		with open(file_path, "r") as file:
			serial_number = file.read().strip()
			if not serial_number:
				first_digit = '230'
				remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(12))
				serial_number = first_digit + remaining_digits
	else:
		first_digit = '230'
		remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(12))
		serial_number = first_digit + remaining_digits
except Exception as e:
	print(f'Error: {e}')
	first_digit = '230'
	remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(12))
	serial_number = first_digit + remaining_digits
try:
	if os.path.exists(file_path2):
		with open(file_path2, "r") as file:
			uuid_number = file.read().strip()
			if len(uuid_number) != 32 or any(char not in '0123456789AaBbCcDdEeFf' for char in uuid_number):
				uuid_number = 'AUTO'
	else:
		uuid_number = 'AUTO'
except Exception as e:
	print(f'Error: {e}')
	uuid_number = 'AUTO'

cmdD10 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSA\\MSUTIL.EXE" /BS \"{serial_number}\"'
cmdD11 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSA\\MSUTIL.EXE" /SU \"{uuid_number}\"'
cmdD20 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSB\\MSUTIL.EXE" /BS \"{serial_number}\"'
cmdD21 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSB\\MSUTIL.EXE" /SU \"{uuid_number}\"'
cmdD30 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSC\\MSUTIL.EXE" /BS \"{serial_number}\"'
cmdD31 = f'"C:\\Users\\{usernamereal}\\AppData\\Local\\pip\\cache\\http\\MSC\\MSUTIL.EXE" /SU \"{uuid_number}\"'
def check_and_run_commands(cmd1, cmd2):
	try:
		subprocess.run(cmd1, shell=True)
		subprocess.run(cmd2, shell=True)
		os.system("net stop winmgmt /y")
		os.system("net start winmgmt /y")
		os.system("sc stop winmgmt")
		os.system("sc start winmgmt")
		new_smbios = get_smbios()
		new_motherb = get_motherb()
		if new_smbios != stock_smbios and new_motherb != stock_motherb:
			return True
	except Exception as e:
		print(f'Error: {e}')
	return False
if not check_and_run_commands(cmdD10, cmdD11):
	if not check_and_run_commands(cmdD20, cmdD21):
		if not check_and_run_commands(cmdD30, cmdD31):
			pass
os.system("net stop winmgmt /y")
os.system("net start winmgmt /y")
os.system("sc stop winmgmt")
os.system("sc start winmgmt")
os.system("exit")