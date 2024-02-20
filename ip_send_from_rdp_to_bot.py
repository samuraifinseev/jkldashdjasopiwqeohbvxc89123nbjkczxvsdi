import requests, time
vms_info_file = open('test.csv')
data_of_vms_info_file = vms_info_file.read()
list_of_vms_info = data_of_vms_info_file.split('\n'); #list_of_vms_info.sort(); #del list_of_ips[0:3];
ready_list_of_ips = []
try:
    response = requests.get('https://api.ipify.org')
    ip_address_rdp = response.text
except:
    ip_address_rdp = 'NONE_FAILED'
try:
    del list_of_vms_info[0]; del list_of_vms_info[len(list_of_vms_info) - 1]
    for i in range(len(list_of_vms_info)):
        list_of_vms_info[i] = list_of_vms_info[i][list_of_vms_info[i].find('IPAddresses'):]
    list_of_vms_info.sort() # ОТСОРТИРОВАЛИ
    text_serv_group = 'server_group'
    def sort_ips_from_file(list_of_vms, start_vms, number_of_vms):
        ips_str = ''
        for i in range(start_vms, number_of_vms):
            if text_serv_group in list_of_vms[i] or text_serv_group.upper() in list_of_vms[i]:
                temp_stroka_ip = list_of_vms_info[i][list_of_vms[i].find('PublicIP') + 15:]
                temp_stroka_ip = temp_stroka_ip[:temp_stroka_ip.find('"')]
                ready_list_of_ips.append(temp_stroka_ip)
                ips_str += temp_stroka_ip + '\n'
        if ips_str == '':
            ips_str = 'Не удалось получить инфу о вмках / перепроверь сам.'
        return ips_str
        #return ready_list_of_ips
    def from_rdp_to_tg(ips, shag):
        TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
        chat_id = '506640934'
        message = 'RDP IP_ADRESS: ' + ip_address_rdp + '\n[' + str(shag) + ']\n' + '=================\n' + ips
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение
    if len(list_of_vms_info) == 3:
        ips_serv_group = sort_ips_from_file(list_of_vms_info, 0, 3)
        from_rdp_to_tg(ips_serv_group, 1)
        print(ips_serv_group)
    if len(list_of_vms_info) == 8:
        ips_serv_group = sort_ips_from_file(list_of_vms_info, 3, 8)
        from_rdp_to_tg(ips_serv_group, 2)
        print(ips_serv_group)
    if len(list_of_vms_info) == 13:
        ips_serv_group = sort_ips_from_file(list_of_vms_info, 8, 13)
        from_rdp_to_tg(ips_serv_group, 3)
        print(ips_serv_group)
    if len(list_of_vms_info) == 17:
        ips_serv_group = sort_ips_from_file(list_of_vms_info, 13, 17)
        from_rdp_to_tg(ips_serv_group, 4)
        print(ips_serv_group)
    if len(list_of_vms_info) == 16:
        ips_serv_group = sort_ips_from_file(list_of_vms_info, 13, 16)
        from_rdp_to_tg(ips_serv_group, 4)
        print(ips_serv_group)
    if len(list_of_vms_info) != 17 and len(list_of_vms_info) != 13 and len(list_of_vms_info) != 8 and len(list_of_vms_info) != 3 and len(list_of_vms_info) != 16:
        ips_serv_group = 'Некорректно подсчитались строки в файле. \n значения, которые могут быть - [3], [8], [13], [17] \n Текущее значение:' + str(len(list_of_vms_info))
        from_rdp_to_tg(ips_serv_group, 0)
        print(ips_serv_group)
except:
    TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
    chat_id = '506640934'
    message = 'RDP IP_ADRESS: ' + ip_address_rdp + '\n[' 'АККАУНТ ВО ФРОДЕ / ЛИБО ДРУГАЯ ОШИБКА' + ']\n' + '=================\n'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
