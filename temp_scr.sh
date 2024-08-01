# !/bin/bash
cd /home/azureuser
az vm restart -g servers_group -n server10
az vm restart -g servers_group -n server11
az vm restart -g servers_group -n server12
az vm restart -g servers_group -n server14
az vm restart -g servers_group -n server15
az vm restart -g servers_group -n server16
az vm restart -g servers_group -n server17
az vm restart -g servers_group -n server18
az vm restart -g servers_group -n server19
az vm restart -g servers_group -n server20
az vm restart -g servers_group -n server21
az vm restart -g servers_group -n server22
az vm restart -g servers_group -n server23
az vm restart -g servers_group -n server24
az vm restart -g servers_group -n server27
az vm restart -g servers_group -n server28
az vm restart -g servers_group -n server29
# sleep 30
# az vm start -g servers_group -n server10
# az vm start -g servers_group -n server11
# az vm start -g servers_group -n server12
# az vm start -g servers_group -n server14
# az vm start -g servers_group -n server15
# az vm start -g servers_group -n server16
# az vm start -g servers_group -n server17
# az vm start -g servers_group -n server18
# az vm start -g servers_group -n server19
# az vm start -g servers_group -n server20
# az vm start -g servers_group -n server21
# az vm start -g servers_group -n server22
# az vm start -g servers_group -n server23
# az vm start -g servers_group -n server24
# az vm start -g servers_group -n server27
# az vm start -g servers_group -n server28
# az vm start -g servers_group -n server29
sleep30
python3 linux_send_ip_to_tg.py
