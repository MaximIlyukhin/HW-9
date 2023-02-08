from bot import bot
import commands, model
from model import total_count

async def start_game(message):
    global total_count
    await bot.send_message(message.from_user.id, f'{message.from_user.full_name} играет против супер бота\n\
        На столе лежит {total_count} конфет.\n\
        За один ход можно забрать не более чем 28 конфет.\n\
        Все конфеты оппонента достаются сделавшему последний ход.')


async def player_take(message):
    await bot.send_message(message.from_user.id, f'Возьми конфеты, но не больше 28: ')


async def table_info(message, name1, take, total_count, name2):
    await bot.send_message(message.from_user.id, f'{name1} взял {take} конфет,\n на столе осталось {total_count} конфет.\n Ходит {name2}')


async def win(message, name, take, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {take} конфет,\n на столе осталось {total_count} конфет.\n {name} победил!')


async def wrong_take(message):
    new_take = await bot.send_message(message.from_user.id, f'Вы взяли слишком много конфет,\n попробуйте снова!')
    await commands.player_turn(new_take)

async def take_no_digit(message):
    new_take_1 = await bot.send_message(message.from_user.id, 'Введите число ')
    await commands.player_turn(new_take_1)
            