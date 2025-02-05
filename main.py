import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

BOT_TOKEN = '7923159442:AAHSTM3XUMKtgt8LuBp6yWX_2IChuuKQPJY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
router = Router()

button_yes = InlineKeyboardButton(text='Да ✅', callback_data='yes')
button_no = InlineKeyboardButton(text='Нет ❌', callback_data='no')

button_q1 = InlineKeyboardButton(text='1', callback_data='q1')
button_q2 = InlineKeyboardButton(text='3', callback_data='q2')
button_q3 = InlineKeyboardButton(text='5', callback_data='q3')

button_len1 = InlineKeyboardButton(text='10', callback_data='len1')
button_len2 = InlineKeyboardButton(text='12', callback_data='len2')
button_len3 = InlineKeyboardButton(text='15', callback_data='len3')


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes, button_no]
])

keyboard_quantity = InlineKeyboardMarkup(inline_keyboard=[
    [button_q1, button_q2, button_q3]
])

keyboard_len = InlineKeyboardMarkup(inline_keyboard=[
    [button_len1, button_len2, button_len3]
])


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''
quantity = 0

@router.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer('Привет! Это бот - генератор паролей, ответь на несколько вопросов и я пришлю тебе ответ.')
    await message.answer('Количество паролей для генерации: ', reply_markup=keyboard_quantity)
    
@router.callback_query(F.data == 'q1')
async def handler_1_quantity(callback: CallbackQuery):
    quantity = 1
    await callback.message.delete()
    await callback.message.answer(f'Кол-во паролей = {quantity}')
    await callback.message.answer('Введите длину пароля:', reply_markup=keyboard_len)
    await callback.answer()

@router.callback_query(F.data == 'q2')
async def handler_2_quantity(callback: CallbackQuery):
    quantity = 3
    await callback.message.delete()
    await callback.message.answer(f'Кол-во паролей = {quantity}')
    await callback.message.answer('Введите длину пароля:', reply_markup=keyboard_len)
    await callback.answer()

@router.callback_query(F.data == 'q3')
async def handler_3_quantity(callback: CallbackQuery):
    quantity = 5
    await callback.message.delete()
    await callback.message.answer(f'Кол-во паролей = {quantity}')
    await callback.message.answer('Введите длину пароля:', reply_markup=keyboard_len)
    await callback.answer()


dp.include_router(router)

if __name__ == '__main__':
    dp.run_polling(bot)