import telebot
from telebot import types

bot = telebot.TeleBot('5941463029:AAGjycDegxAvLuiSNUa1Lxbm0s27vhDfu_s')

#Main Menu - Student life
def main_menu_student_life(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    student_life_events = types.InlineKeyboardButton("Events", callback_data="student_life_events")
    student_life_clubs = types.InlineKeyboardButton("Clubs", callback_data="student_life_clubs")
    back_menu = types.InlineKeyboardButton("Go back", callback_data="back_menu")
    markup.add(student_life_clubs,student_life_events,back_menu)
    bot.send_message(message.chat.id, '''Suleyman Demirel University is literally full of active student life - join us!

Find out what students at SDU are up to:''', reply_markup=markup)

#Main Menu - Student life - Clubs
def main_menu_student_life_clubs(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_student_life = types.InlineKeyboardButton("Go back", callback_data="back_student_life")
    markup.add(back_student_life)
    bot.send_message(message.chat.id, '''About 35 clubs are active at our university. There are clubs with a variety of directions, every student can find and join a club that he or she likes. There is never a dull moment with our clubs :)

Also you can find more information on Sdu Life instagram page: <a href="https://www.instagram.com/sdulife/">https://www.instagram.com/sdulife/</a>''', reply_markup=markup, parse_mode='html')

#Main Menu - Student life - Events
def main_menu_student_life_events(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    back_student_life = types.InlineKeyboardButton("Go back", callback_data="back_student_life")
    markup.add(back_student_life)
    bot.send_message(message.chat.id, '''Every month we have different events organized by student organizations. Here is the program schedule for this semester''', reply_markup=markup)