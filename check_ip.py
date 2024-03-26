#! /usr/bin/env python
# -*- coding: utf-8 -*-
import serviceping
number_of_active_m = 0
for i in range(2, 254):
    temp_ip = '10.8.0.' + str(i)
    status_server = serviceping.scan(temp_ip, '22')
    if status_server['state'] == 'open':
        number_of_active_m += 1
    print(temp_ip, 'недоступен')
print('активных майнеров - ', number_of_active_m)
