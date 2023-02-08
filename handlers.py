from aiogram import Dispatcher, types
import commands
import model
import view
from bot import bot, dp
from keyboards import Kb_main_menu


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_game, commands=['game'])
    dp.register_message_handler(commands.player_turn)


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer('Приветствую тебя! Ты на конфетном поле боя!', reply_markup=Kb_main_menu)


@dp.message_handler(commands=['exit'])
async def mes_exit(message: types.Message):
    await bot.send_message(message.from_user.id, f'Конец!')
    await model.set_game()
    exit()


@dp.message_handler(commands=['rule'])
async def mes_rule(message: types.Message):
    await bot.send_message(message.from_user.id, f'Правила:\n\
        На столе лежит N конфет.\n\
        Играет человек против бота делая ход друг после друга.\n\
        Первый ход определяется жеребьёвкой.\n\
        За один ход можно забрать не более чем 28 конфет.\n\
        Все конфеты оппонента достаются сделавшему последний ход.')