import telebot
from telebot import types

bot = telebot.TeleBot('5941463029:AAGjycDegxAvLuiSNUa1Lxbm0s27vhDfu_s')

#Main Menu - Dormitory
def main_menu_dormitory(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    can_live = types.InlineKeyboardButton("Who can live in a dormitory", callback_data="can_live")
    dormitory_photos = types.InlineKeyboardButton("Dormitory photos", callback_data="dormitory_photos")
    back_menu = types.InlineKeyboardButton("Go back", callback_data="back_menu")
    document_dormitory = types.InlineKeyboardButton("Documents for the dormitory", callback_data="document_dormitory")
    markup.add(can_live,document_dormitory,dormitory_photos,back_menu)
    bot.send_message(message.chat.id, '''Suleyman Demirel University has its own campus. SDU Student House is located on the territory of the Smart Campus in the immediate vicinity of the university building (30 meters). For students and guests of the university Next to Student House is a football field, volleyball and basketball courts. 24-hour security protects the campus ensuring the safety of all students and visitors. Moreover, for VIP guests in block “A” there are two VIP rooms with amenities. Is built for 1280 people in 4 blocks

Just choose the section you want:''', reply_markup=markup)

#Main Menu - Dormitory - Can live
def main_menu_dormitory_can_live(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_dormitory = types.InlineKeyboardButton("Go back", callback_data="back_dormitory")
    markup.add(back_dormitory)
    bot.send_message(message.chat.id, '''In the dormitory move in if you do not have a local registration. A student who lives in the city is not allowed to move into the dormitory.''', reply_markup=markup)


#Main Menu - Dormitory - Document dormitory
def main_menu_dormitory_document_dormitory(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_dormitory = types.InlineKeyboardButton("Go back", callback_data="back_dormitory")
    markup.add(back_dormitory)
    bot.send_message(message.chat.id, '''Docs required

4 photos 3x4
Copy of medical report 075 (obtainable from any Kazakh clinic)
Copy of identity card
Copy of payment receipt''', reply_markup=markup)

#Main Menu - Dormitory - Dorm photos
def main_menu_dormitory_dorm_photos(message):
    bot.send_message(message.chat.id, '''For the convenience of students, all photos of the dorm are sent here.''')