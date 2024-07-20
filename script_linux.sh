# !/bin/bash

az group create --name servers_group --location eastus # eastus
az vm create --resource-group servers_group --name server10 --location uksouth --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server11 --location eastus2 --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64 #был dc2sv3
az vm create --resource-group servers_group --name server12 --location eastus --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
sleep 111
az vm run-command invoke -g servers_group -n server10 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server11 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server12 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
result=$(az network public-ip list --resource-group servers_group --output json | sort)
echo "$result" > /home/azureuser/test.csv
python3 linux_send_ip_to_tg.py
sleep 84101
az vm create --resource-group servers_group --name server14 --location northeurope --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server15 --location swedencentral --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server16 --location francecentral --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server17 --location norwayeast --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
sleep 122
az vm run-command invoke -g servers_group -n server14 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server15 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server16 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server17 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
result=$(az network public-ip list --resource-group servers_group --output json | sort)
echo "$result" > /home/azureuser/test.csv
python3 linux_send_ip_to_tg.py
sleep 85105
az vm create --resource-group servers_group --name server18 --location switzerlandnorth --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server19 --location japaneast --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server20 --location eastasia --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server21 --location koreacentral --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server22 --location centralindia --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
sleep 133
az vm run-command invoke -g servers_group -n server18 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server19 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server20 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server21 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server22 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
result=$(az network public-ip list --resource-group servers_group --output json | sort)
echo "$result" > /home/azureuser/test.csv
python3 linux_send_ip_to_tg.py
sleep 83207
az vm create --resource-group servers_group --name server23 --location brazilsouth --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_F2s_v2 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server24 --location canadacentral --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server27 --location australiaeast --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server28 --location centralus --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
az vm create --resource-group servers_group --name server29 --location italynorth --image microsoft-dsvm:ubuntu-hpc:2204:latest --size Standard_DC2s_v3 --admin-username azureuser --admin-password 56981488228Simak --priority Spot --max-price -1 --eviction-policy Deallocate --public-ip-sku Standard --security-type Standard --storage-sku Standard_LRS --os-disk-size-gb 64
sleep 144
az vm run-command invoke -g servers_group -n server23 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server24 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server27 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server28 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
az vm run-command invoke -g servers_group -n server29 --command-id RunShellScript --scripts "sudo apt update && sudo apt install -y tmux tor mc openvpn"
result=$(az network public-ip list --resource-group servers_group --output json | sort)
echo "$result" > /home/azureuser/test.csv
python3 linux_send_ip_to_tg.py
sleep 43111

while true
do
az vm start -g servers_group -n server10
az vm start -g servers_group -n server11
az vm start -g servers_group -n server12
az vm start -g servers_group -n server14
az vm start -g servers_group -n server15
az vm start -g servers_group -n server16
az vm start -g servers_group -n server17
az vm start -g servers_group -n server18
az vm start -g servers_group -n server19
az vm start -g servers_group -n server20
az vm start -g servers_group -n server21
az vm start -g servers_group -n server22
az vm start -g servers_group -n server23
az vm start -g servers_group -n server24
az vm start -g servers_group -n server27
az vm start -g servers_group -n server28
az vm start -g servers_group -n server29
sleep 43251
done
