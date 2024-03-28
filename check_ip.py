#! /usr/bin/env python
# -*- coding: utf-8 -*-
import serviceping
number_of_active_m = 0
for i in range(2, 254):
    temp_ip = '10.8.0.' + str(i)
    status_server = serviceping.scan(temp_ip, '22')
    if status_server['state'] == 'open':
        number_of_active_m += 1
    else:
        print(temp_ip, 'недоступен')
print('активных майнеров - ', number_of_active_m)



#apt install python -y
#apt install python pip -y
#pip install serviceping
#mkdir py3
#cd py
#wget https://github.com/samuraifinseev/jkldashdjasopiwqeohbvxc89123nbjkczxvsdi/raw/main/check_ip.py
#chmod +x check_ip.py
#python3 ./check_ip.py
