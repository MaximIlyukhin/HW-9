from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Kb_main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)

btn_game = KeyboardButton('/game')
btn_rule = KeyboardButton('/rule')
btn_exit = KeyboardButton('/exit')

Kb_main_menu.add(btn_game, btn_rule, btn_exit)
