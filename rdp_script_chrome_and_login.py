import keyboard, random
from pyautogui import*
from tqdm import tqdm
import requests, time
from keyboard import*
import time
from mailtm import*
def listener(message):
    global subject; global text
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
    security_code = "Content: " + message['text'] if message['text'] else message['html']
    subject = "\nSubject: " + message['subject']
    text = message['text']
    print('это сек код тест', text) #api почта функция
subject = str();
text = str()
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
#(945, 363, 1, 0, 'left');
sleep(2); click(719, 596, 1, 0, 'left'); sleep(15) # password save and stay sign in
click(1076, 107, 1, 0, 'left'); sleep(8); click(1058, 249, 1, 0, 'left'); sleep(12); click(713, 768, 1, 0, 'left'); sleep(12); # переходим в настройки акка из
# панели азура
click(880, 313, 1, 0, 'left'); sleep(7) # нажимаем изменить пасс кнопку
click(454, 567, 1, 0, 'left'); sleep(1);
# Get Domains # НАЧИНАЕМ ЮЗАТЬ ПОЧТУ ПОД АКК
test = Email()
print("\nDomain: " + test.domain)
# Make new email address
test.register(username=None, password='1534589', domain=None)
print("\nEmail Adress: " + str(test.address))
email_reserve = test.address; sleep(3)
keyboard.write(email_reserve, delay=0.1); sleep(2); click(722, 674, 1, 0, 'left'); # вводим резерв почту и нажимаем ок
# Start listening
test.start(listener, interval=3)
print("\nWaiting for new emails...")
time.sleep(65)
print(text, 'проверка на наличие кода')
test.stop()
list_of_text = text.split('\n')
for i in range(len(list_of_text)):
    if 'Security code' in list_of_text[i]:
            security_code = list_of_text[i]
security_code_ready = str()
for i in range(len(security_code)):
    if security_code[i].isdigit():
        security_code_ready += security_code[i]
print(security_code_ready)
sleep(5); click(440, 480, 1, 0, 'left'); keyboard.write(security_code_ready, delay=0.2); click(714, 586, 1, 0, 'left'); sleep(15) # вводим секьюрити код 1
click(505, 505, 1, 0, 'left'); keyboard.write(email_reserve, delay=0.1); click(718, 594, 1, 0, 'left'); sleep(4) # вводим почту 2ой раз
security_code = ''; security_code_ready = ''; text = ''; subject = ''
# Start listening ПОЛУЧАЕМ КОД
test.start(listener, interval=3)
print("\nWaiting for new emails...")
time.sleep(65)
print(text, 'проверка на наличие кода')
test.stop()
list_of_text = text.split('\n')
for i in range(len(list_of_text)):
    if 'Security code' in list_of_text[i]:
            security_code = list_of_text[i]
security_code_ready = str()
for i in range(len(security_code)):
    if security_code[i].isdigit():
        security_code_ready += security_code[i]

click(444, 504, 1, 0, 'left'); keyboard.write(security_code_ready, delay=0.2); click(711, 598, 1, 0, 'left'); sleep(10) # вводим секьюрити код 2
click(447, 605, 1, 0, 'left'); sleep(8) # отказываемся от доп защиты с пассом
click(97, 297, 1, 0, 'left'); keyboard.write(account_password, delay=0.1); sleep(1.5) # вводим старый пасс
click(88, 388, 1, 0, 'left'); keyboard.write('56981488228Simak', dela=0.1); sleep(1.5) # вводим новый пасс 1
click(102, 489, 1, 0, 'left'); keyboard.write('56981488228Simak', dela=0.1); sleep(1.5) # вводим новый пасс 2
click(110, 629, 1, 0, 'left'); sleep(20) # подтверждаем изменение пасса
click(518, 461, 1, 0, 'left'); keyboard.write('56981488228Simak', dela=0.1); sleep(1.5); click(712, 625, 1, 0, 'left'); sleep(15) # во время разлогина заходим снова под акк
click(1010, 362, 1, 0, 'left'); click(806, 142, 1, 0, 'left') # закрываем еще одно окно навязывания хуйни для защиты
