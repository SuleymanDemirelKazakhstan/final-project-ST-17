@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow, nice photo!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to website", url="https://sdu.edu.kz/ru/suleyman-demirel-university-ru/"))
    bot.send_message(message.chat.id, '''You've reached the main menu.
What do you want to know more about?''', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Help desk', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, 'Hi dude', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Your id: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('New_logo_SDU.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I do not understand you', parse_mode='html')