import telebot
from telebot import types

bot = telebot.TeleBot('5941463029:AAGjycDegxAvLuiSNUa1Lxbm0s27vhDfu_s')

#Main Menu - Contact
def main_menu_contact(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    get_there = types.InlineKeyboardButton("How to get there?", callback_data="get_there")
    working_hours = types.InlineKeyboardButton("Working hours", callback_data="working_hours")
    contact_telephone = types.InlineKeyboardButton("Contact telephone", callback_data="contact_telephone")
    address_campus = types.InlineKeyboardButton("Address of the campus", callback_data="address_campus")
    back_menu = types.InlineKeyboardButton("Go back", callback_data="back_menu")
    markup.add(get_there,working_hours,contact_telephone,address_campus,back_menu)
    bot.send_message(message.chat.id, '''You can always contact our admissions office, just pick a section:''', reply_markup=markup)

#Main Menu - Contact - Get there
def main_menu_contact_get_there(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_contact = types.InlineKeyboardButton("Go back",callback_data="back_contact")
    markup.add(back_contact)
    bot.send_message(message.chat.id, "The address of the Admissions Office of Suleyman Demirel University: 1/1 Abylaykhan Street, Kaskelen, Kazakhstan.", reply_markup=markup)

#Main Menu - Contact - Working hours
def main_menu_contact_working_hours(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_contact = types.InlineKeyboardButton("Go back",callback_data="back_contact")
    markup.add(back_contact)
    bot.send_message(message.chat.id, '''The Admissions Committee of Suleyman Demirel University accepts applicants from Monday to Friday.

⏰ Mon-Fri: 08.00 - 17.00
⏰ Fri: 08.00 - 16.00

Lunch: from 12.00 to 13.00''', reply_markup=markup)

#Main Menu - Contact - Contact telephone
def main_menu_contact_telephone(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_contact = types.InlineKeyboardButton("Go back",callback_data="back_contact")
    markup.add(back_contact)
    bot.send_message(message.chat.id, '''Contact us

📞 +7 (727) 307 95 65
🟢 + 7 702 000 11 33
✉️ info@sdu.edu.kz​''', reply_markup=markup)

#Main Menu - Contact - Address campus
def main_menu_contact_address_campus(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_contact = types.InlineKeyboardButton("Go back",callback_data="back_contact")
    markup.add(back_contact)
    bot.send_message(message.chat.id, '''Campus's address

📍 Almaty region, Karasay area 040900, Kaskelen city, Abylai khan street, 1/1''', reply_markup=markup)