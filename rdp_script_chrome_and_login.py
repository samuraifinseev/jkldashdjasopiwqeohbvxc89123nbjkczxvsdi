import keyboard, random
from pyautogui import*
from tqdm import tqdm
import requests, time
from keyboard import*
print('На данный момент использовать только под почту "Microsoft" ! \n'
      'Также убедись, что подгрузил файл с акками и айпишками в "accs_gruzit_pod_rdp.txt"')
accs_file_inf = open('accs_gruzit_pod_rdp.txt')
data_of_accs_inf = accs_file_inf.read()
list_of_accs_inf = data_of_accs_inf.split('\n')

response = requests.get('https://api.ipify.org')
ip_address = response.text
print(f'Your IP Address is {ip_address}')
for i in range(len(list_of_accs_inf)):
    if ip_address in list_of_accs_inf[i]:
        account_email = list_of_accs_inf[i][:list_of_accs_inf[i].find('\t')]
        account_password = list_of_accs_inf[i][list_of_accs_inf[i].find('\t') + 1:list_of_accs_inf[i].rfind('\t')]
        print('Аккаунт найден:', list_of_accs_inf[i], ' - положение в таблице || \n')
        print('Текущая выдача данных: ', account_email, account_password, ip_address, '|| Сверка пройдена!')
        print('Даю время на валидацию и начинаю... (30 seconds)');
        break
for i in tqdm(range(100)):
    time.sleep(0.3)
click(1018, 770, 1, 0, 'left'); sleep(1); click(1018, 770, 1, 0, 'left'); sleep(1); click(693, 714, 1, 0, 'left'); sleep(1) # завершаем настройку хрома
click(981, 27, 1, 0, 'left'); sleep(2) # хром на полный экран
click(172, 58, 1, 0, 'left'); keyboard.write('azure.microsoft.com', 0,1); keyboard.send('enter'); sleep(5) # ввод azure.microsoft.com
click(1153, 184, 1, 0, 'left'); sleep(10) # sign in
click(475, 414, 1, 0, 'left'); keyboard.write(account_email, delay=0.2); sleep(1); click(720, 538, 1, 0, 'left'); sleep(3) # email input
click(475, 482, 1, 0, 'left'); keyboard.write(account_password, delay=0.2); sleep(1); click(717, 606, 1, 0, 'left'); sleep(3) # password input
click(945, 363, 1, 0, 'left'); sleep(2); click(719, 596, 1, 0, 'left'); sleep(2) # password save and stay sign in