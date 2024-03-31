#! /usr/bin/env python
# -*- coding: utf-8 -*-
import serviceping, requests
number_of_active_m = 0
for i in range(2, 254):
    temp_ip = '10.8.0.' + str(i)
    status_server = serviceping.scan(temp_ip, '22')
    if status_server['state'] == 'open':
        number_of_active_m += 1
    else:
        print(temp_ip, 'недоступен')
print('активных майнеров - ', number_of_active_m)

response = requests.get('https://api.ipify.org')
ip_address = response.text
################# ОТПРАВЛЕНИЕ ДАННЫХ В ТГ БОТ BOTINOK
TOKEN = "5725759489:AAGHJghIdbSZhHglu7mi36p0G_0tvgz_MKM"
chat_id = '506640934'
message =f'Сервер: {ip_address} \n Кол-во активных позиций: {number_of_active_m}'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
##################



#apt install python pip -y
#pip install serviceping requests
#mkdir py3
#cd py
#wget https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/check_ip.py
#chmod +x check_ip.py
#python3 ./check_ip.py
