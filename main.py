import telebot
from telebot import types

import admission, dormitory, student_life, contact

bot = telebot.TeleBot('5941463029:AAGjycDegxAvLuiSNUa1Lxbm0s27vhDfu_s')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'''Hello, <b>{message.from_user.first_name}</b>! 

<b>I'm Alibek the digital assistant 🖐</b>! 

I help SDU students and applicants find the information they need quickly. Choose a section <b>Main Menu</b> - I know a lot of interesting things about the university!'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    menu = types.KeyboardButton('Main Menu')
    markup.add(menu)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Main Menu':
        main_menu(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        menu = types.KeyboardButton('Main Menu')
        markup.add(menu)
        bot.send_message(message.chat.id, message.text + '''Sorry, I didn't understand you.
 :( 
Try again! Press "Main Menu."''', parse_mode='html',reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'back_menu':
        main_menu(call.message)


    elif call.data == 'admission':
        admission.main_menu_admission(call.message)
    elif call.data == 'admissions_committee':
        admission.main_menu_admission_committee(call.message)
    elif call.data == 'online_consultation':
        admission.main_menu_admission_committee_online_consultation(call.message)
    elif call.data == 'document_deadline':
        admission.main_menu_admission_committee_document_deadline(call.message)
    elif call.data == 'document_required':
        admission.main_menu_admission_committee_document_required(call.message)
    elif call.data == 'admission_rules':
        admission.main_menu_admission_committee_admission_rules(call.message)
    elif call.data == 'admissions_master_degree':
        admission.main_menu_admission_master(call.message)
    elif call.data == 'document_deadline_master':
        admission.main_menu_admission_master_document_deadline_master(call.message)
    elif call.data == 'document_required_master':
        admission.main_menu_admission_master_document_required_master(call.message)
    elif call.data == 'admission_rules_master':
        admission.main_menu_admission_master_admission_rules_master(call.message)
    elif call.data == 'back_admission':
        admission.main_menu_admission(call.message)
    elif call.data == 'back_admission_committee':
        admission.main_menu_admission_committee(call.message)
    elif call.data == 'back_master':
        admission.main_menu_admission_master(call.message)


    elif call.data == 'dormitory':
        dormitory.main_menu_dormitory(call.message)
    elif call.data == 'can_live':
        dormitory.main_menu_dormitory_can_live(call.message)
    elif call.data == 'document_dormitory':
        dormitory.main_menu_dormitory_document_dormitory(call.message)
    elif call.data == 'dormitory_photos':
        photo1 = open('photos/canteen.jpg','rb')
        photo2 = open('photos/BASKETBALL-COURT.jpg','rb')
        photo3 = open('photos/Billiard.jpg','rb')
        photo4 = open('photos/Canteen-1.jpg','rb')
        photo5 = open('photos/Chees.jpg','rb')
        photo6 = open('photos/VOLLEYBALL-COURT.jpg','rb')
        bot.send_photo(call.message.chat.id, photo1)
        bot.send_photo(call.message.chat.id, photo2)
        bot.send_photo(call.message.chat.id, photo3)
        bot.send_photo(call.message.chat.id, photo4)
        bot.send_photo(call.message.chat.id, photo5)
        bot.send_photo(call.message.chat.id, photo6)
        dormitory.main_menu_dormitory_dorm_photos(call.message)
        dormitory.main_menu_dormitory(call.message)
    elif call.data == 'back_dormitory':
        dormitory.main_menu_dormitory(call.message)


    elif call.data == 'student_life':
        student_life.main_menu_student_life(call.message)
    elif call.data == 'student_life_clubs':
        photo7 = open('photos/Stud_Life.jpg','rb')
        bot.send_photo(call.message.chat.id, photo7)
        student_life.main_menu_student_life_clubs(call.message)
    elif call.data == 'student_life_events':
        photo8 = open('photos/photo8.jpg','rb')
        photo9 = open('photos/photo9.jpg','rb')
        photo10 = open('photos/photo10.jpg','rb')
        bot.send_photo(call.message.chat.id, photo8)
        bot.send_photo(call.message.chat.id, photo9)
        bot.send_photo(call.message.chat.id, photo10)
        student_life.main_menu_student_life_events(call.message)
    elif call.data == 'back_student_life':
        student_life.main_menu_student_life(call.message)

    elif call.data == 'contact':
        contact.main_menu_contact(call.message)
    elif call.data == 'get_there':
        contact.main_menu_contact_get_there(call.message)
    elif call.data == 'working_hours':
        contact.main_menu_contact_working_hours(call.message)
    elif call.data == 'contact_telephone':
        contact.main_menu_contact_telephone(call.message)
    elif call.data == 'address_campus':
        contact.main_menu_contact_address_campus(call.message)
    elif call.data == 'back_contact':
        contact.main_menu_contact(call.message)

    else:
        bot.send_message(call.message.chat.id, 'nooo')



#Main Menu
def main_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    admission = types.InlineKeyboardButton("Admission", callback_data="admission")
    dormitory = types.InlineKeyboardButton("Dormitory", callback_data="dormitory")
    student_life = types.InlineKeyboardButton("Student Life", callback_data="student_life")
    contact = types.InlineKeyboardButton("Contact", callback_data="contact")
    document = types.InlineKeyboardButton("Submit your documents now!", url="https://sdu.edu.kz/admission-3-2/")
    markup.add(admission,dormitory,student_life,contact,document)
    bot.send_message(message.chat.id, '''You've reached the main menu.
What do you want to know more about?''', reply_markup=markup)



bot.polling(non_stop=True)