import requests, time, serviceping
vms_info_file = open('test.csv')
data_of_vms_info_file = vms_info_file.read()
#list_of_vms_info = data_of_vms_info_file.split('\n'); #list_of_vms_info.sort(); #del list_of_ips[0:3];
ips_text = data_of_vms_info_file[data_of_vms_info_file.find("ipAddress"):data_of_vms_info_file.rfind("ipAddress") + 33]
ips_list = ips_text.split('\n')
print(len(ips_list))
temp_stroka_ip = ''
ready_list_of_ips = list()
def ping_vm_for_available(list_of_ips):
    vm_ready_for_this_shag = list()
    # text_of_ip = '\n'.join(ready_list_of_ips)
    # return text_of_ip
    for i in range(len(list_of_ips)):
        status_vm = serviceping.scan(list_of_ips[i], '22')
        if status_vm['state'] == 'open':
            vm_ready_for_this_shag.append(list_of_ips[i])
    converter_list_to_text = '\n'.join(vm_ready_for_this_shag)
    return converter_list_to_text
#####===============
def from_vm_to_tg(ips):
    TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
    chat_id = '506640934'
    message = 'RDP IP_ADRESS: ' + ip_address_vm + '\n[' + 'LINUX NO SHAG' + ']\n' + '=================\n' + ips
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение
#####==================
###==================
response = requests.get('https://api.ipify.org')
ip_address_vm = response.text
#=====================
try:
    for i in range(len(ips_list)):
        if "ipAddress" in ips_list[i]:
            for j in range(len(ips_list[i])):
                if ips_list[i][j].isdigit() or ips_list[i][j] == '.':
                    temp_stroka_ip += ips_list[i][j]
            ready_list_of_ips.append(temp_stroka_ip)
            temp_stroka_ip = ''
    print(ready_list_of_ips); print(len(ready_list_of_ips))
    text_of_pinged_ip = ping_vm_for_available(ready_list_of_ips)
    if text_of_pinged_ip == '':
        from_vm_to_tg('НЕТ АКТИВНЫХ ВМОК ИЛИ ЧЕТ СЛОМАЛОСЬ. ЗАЙДИ И ГЛЯНЬ')
    else:
        from_vm_to_tg(text_of_pinged_ip)
except:
    TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
    chat_id = '506640934'
    message = 'LINUX VM IP_ADRESS: ' + ip_address_vm + '\n[' 'АККАУНТ ВО ФРОДЕ / ЛИБО ДРУГАЯ ОШИБКА' + ']\n' + '=================\n'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
