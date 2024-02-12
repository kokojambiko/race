import telebot
import config
import random
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

pairs = {}  # Словарь для хранения пар пользователей


custom_commands = [
    types.BotCommand("start", "Начать диалог"),
    types.BotCommand("marry", "Начать процесс бракосочетания"),
    types.BotCommand("propose", "Пригласить пользователя в брак"),
    types.BotCommand("accept", "Принять приглашение в брак"),
    types.BotCommand("check_marriage", "Проверить список поженившихся пользователей"),

]
bot.set_my_commands(custom_commands)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('image/wel.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # Отправляем пустую клавиатуру
    markup = types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id,
                     "Приветики, {0.first_name}!\nЯ - <b>{1.first_name}</b>, я люблю пирожки!!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['marry'])
def start_marry(message):
    chat_id = message.chat.id
    if chat_id not in pairs:
        pairs[chat_id] = {}
    bot.send_message(chat_id, "Укажите, с кем вы хотите пожениться, напишите /propose @username")

@bot.message_handler(commands=['propose'])
def propose(message):
    chat_id = message.chat.id
    if chat_id not in pairs:
        bot.send_message(chat_id, "Сначала начните процесс бракосочетания с помощью команды /marry")
        return
    if message.reply_to_message is None or message.reply_to_message.from_user is None:
        bot.send_message(chat_id, "Ответьте на сообщение пользователя, которого вы хотите пригласить в брак")
        return
    user_id = message.from_user.id
    spouse_id = message.reply_to_message.from_user.id
    pairs[chat_id][user_id] = spouse_id
    pairs[chat_id][spouse_id] = user_id
    bot.send_message(chat_id, f"Пользователь @{message.reply_to_message.from_user.username} приглашен в брак. "
                               f"Если вы согласны, напишите /accept")

@bot.message_handler(commands=['accept'])
def accept_proposal(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id not in pairs or user_id not in pairs[chat_id]:
        bot.send_message(chat_id, "Нет приглашения в брак или вы не являетесь приглашенным пользователем")
    else:
        spouse_id = pairs[chat_id][user_id]
        user_username = bot.get_chat_member(chat_id, user_id).user.username
        spouse_username = bot.get_chat_member(chat_id, spouse_id).user.username
        bot.send_message(chat_id, f"Пользователь @{message.from_user.username} принял приглашение в брак! "
                                  f"Поздравляем с новой семейной жизнью! Ваша пара: @{spouse_username}")

@bot.message_handler(commands=['check_marriage'])
def check_marriage(message):
    chat_id = message.chat.id
    if chat_id not in pairs or not pairs[chat_id]:
        bot.send_message(chat_id, "В этой группе пока что никто не поженился")
    else:
        married_users = set()  # Создаем пустое множество для хранения уникальных пар

        for user_id, spouse_id in pairs[chat_id].items():
            user_username = bot.get_chat_member(chat_id, user_id).user.username
            spouse_username = bot.get_chat_member(chat_id, spouse_id).user.username

            # Добавляем кортеж (пару) в множество
            married_users.add((user_username, spouse_username))

        # Формируем сообщение с переносом строк для каждой уникальной пары
        response_message = "В этой группе поженились:\n" + "\n".join([f"@{user} и @{spouse}" for user, spouse in married_users])
        bot.send_message(chat_id, response_message)
import re

@bot.message_handler(func=lambda message: re.search(r'\bУдарить\b', message.text, re.IGNORECASE) is not None)
def hit_action(message):
    chat_id = message.chat.id
    # Проверяем, есть ли ответ на сообщение
    if message.reply_to_message is not None:
        target_user_id = message.reply_to_message.from_user.id
        bot.send_message(chat_id, f"Вы ударили пользователя @{message.reply_to_message.from_user.username}! Ouch🤜😵‍💫!")
    else:
        bot.send_message(chat_id, "Для выполнения действия 'ударить' ответьте на сообщение пользователя.")


@bot.message_handler(func=lambda message: re.search(r'\bОбнять\b', message.text, re.IGNORECASE) is not None)
def hug_action(message):
    chat_id = message.chat.id
    # Получаем информацию о том, кто отправил сообщение
    sender_user = message.from_user
    sender_username = f"@{sender_user.username}" if sender_user.username else sender_user.first_name

    # Проверяем, есть ли ответ на сообщение
    if message.reply_to_message is not None:
        target_user = message.reply_to_message.from_user
        target_username = f"@{target_user.username}" if target_user.username else target_user.first_name
        bot.send_message(chat_id, f"{sender_username} обнял пользователя {target_username}! 🤗❤️")
    else:
        bot.send_message(chat_id, "Для выполнения действия 'обнять' ответьте на сообщение пользователя.")


bot.polling()
