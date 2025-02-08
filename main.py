import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

BOT_TOKEN = '7923159442:AAHSTM3XUMKtgt8LuBp6yWX_2IChuuKQPJY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
router = Router()

#да/нет кнопки нужны ли цифры
button_yes_digit = InlineKeyboardButton(text='Да ✅', callback_data='yes_digit')
button_no_digit = InlineKeyboardButton(text='Нет ❌', callback_data='no_digit')

#да/нет кнопки нужны ли заглавные буквы
button_yes_upper = InlineKeyboardButton(text='Да ✅', callback_data='yes_upper')
button_no_upper = InlineKeyboardButton(text='Нет ❌', callback_data='no_upper')

#да/нет кнопки нужны ли символы
button_yes_simbols = InlineKeyboardButton(text='Да ✅', callback_data='yes_simbols')
button_no_simbols = InlineKeyboardButton(text='Нет ❌', callback_data='no_simbols')

#кол-во символов клавиатура
button_q1 = InlineKeyboardButton(text='1', callback_data='q1')
button_q2 = InlineKeyboardButton(text='3', callback_data='q2')
button_q3 = InlineKeyboardButton(text='5', callback_data='q3')

#длинна пароля кнопки
button_len1 = InlineKeyboardButton(text='10', callback_data='len1')
button_len2 = InlineKeyboardButton(text='12', callback_data='len2')
button_len3 = InlineKeyboardButton(text='15', callback_data='len3')

button_repeat = InlineKeyboardButton(text='Повторить', callback_data='repeat')
button_stop = InlineKeyboardButton(text='Cтоп', callback_data='stop')

button_generations = InlineKeyboardButton(text='Сгенерировать', callback_data='generations')

#да/нет клавиатура нужны ли цифры
keyboard_digit = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_digit, button_no_digit]
])

#да/нет клавиатура нужны ли заглавные
keyboard_upper = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_upper, button_no_upper]
])

#да/нет клавиатура нужны ли символы
keyboard_simbols = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_simbols, button_no_simbols]
])


#кол-во символов клавиатура
keyboard_quantity = InlineKeyboardMarkup(inline_keyboard=[
    [button_q1, button_q2, button_q3]
])

#длина пароля клавиатура
keyboard_len = InlineKeyboardMarkup(inline_keyboard=[
    [button_len1, button_len2, button_len3]
])

keyboard_repeat = InlineKeyboardMarkup(inline_keyboard=[
    [button_repeat, button_stop]
])

keyboard_generations = InlineKeyboardMarkup(inline_keyboard=[
    [button_generations]
])

digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'




@router.message(Command("start"))
async def process_start_command(message: Message):
    global chars
    chars = 'abcdefghijklmnopqrstuvwxyz'
    global quantity
    quantity = 0
    global len_s
    len_s = 0
    await message.answer('Привет! Это бот - генератор паролей, ответь на несколько вопросов и я пришлю тебе ответ.')
    await message.answer('Количество паролей для генерации: ', reply_markup=keyboard_quantity)


#обработка коллбэков кол-во паролей
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



#обработка коллбэков клавиатуры запроса длинны пароля
@router.callback_query(F.data == 'len1')
async def handler_10_quantity(callback: CallbackQuery):
    len_s = 10
    await callback.message.delete()
    await callback.message.answer(f'Длина пароля = {len_s} символов')
    await callback.message.answer('Включать ли цифры?', reply_markup=keyboard_digit)
    await callback.answer()

@router.callback_query(F.data == 'len2')
async def handler_12_quantity(callback: CallbackQuery):
    len_s = 12
    await callback.message.delete()
    await callback.message.answer(f'Длина пароля = {len_s} символов')
    await callback.message.answer('Включать ли цифры?', reply_markup=keyboard_digit)
    await callback.answer()

@router.callback_query(F.data == 'len3')
async def handler_15_quantity(callback: CallbackQuery):
    len_s = 15
    await callback.message.delete()
    await callback.message.answer(f'Длина пароля = {len_s} символов')
    await callback.message.answer('Включать ли цифры?', reply_markup=keyboard_digit)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли цифры'
@router.callback_query(F.data == 'yes_digit')
async def handler_yes_digit(callback: CallbackQuery):
    global chars
    chars += digits
    await callback.message.delete()
    await callback.message.answer(f'Цифры включены')
    await callback.message.answer('Включать ли заглавные буквы?', reply_markup=keyboard_upper)
    await callback.answer()

@router.callback_query(F.data == 'no_digit')
async def handler_no_digit(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Включать ли заглавные буквы?', reply_markup=keyboard_upper)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли заглавные'
@router.callback_query(F.data == 'yes_upper')
async def handler_yes_upper(callback: CallbackQuery):
    global chars
    chars += uppercase_letters
    await callback.message.delete()
    await callback.message.answer(f'Заглавные буквы включены')
    await callback.message.answer('Включать ли символы?', reply_markup=keyboard_simbols)
    await callback.answer()

@router.callback_query(F.data == 'no_upper')
async def handler_no_upper(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Включать ли символы?', reply_markup=keyboard_simbols)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли символы'
@router.callback_query(F.data == 'yes_simbols')
async def handler_yes_simbols(callback: CallbackQuery):
    global chars
    chars += punctuation
    await callback.message.delete()
    await callback.message.answer('...', reply_markup=keyboard_generations)
    await callback.answer()

@router.callback_query(F.data == 'no_simbols')
async def handler_no_simbols(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('...', reply_markup=keyboard_generations)
    await callback.answer()


@router.callback_query(F.data == 'generations')
async def handler_yes_simbols(callback: CallbackQuery):
    global quantity
    global len_s
    global chars
    li = []
    result = ''
    for i in range(quantity):
        for _ in range(len_s):
            result += random.choice(chars)

        li.append(result)
        result = ''

    await callback.message.delete()
    await callback.message.answer(f'pass:{li}')
    await callback.message.answer('Повторить генерацию?', reply_markup=keyboard_repeat)
    await callback.answer()   


#обработка коллбэков клавиатуры 'repeat and stop'
@router.callback_query(F.data == 'repeat')
async def handler_repeat(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('...', reply_markup=keyboard_generations)
    await callback.answer()

@router.callback_query(F.data == 'stop')
async def handler_stop(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Для того, что бы начать - нажмите /start')
    await callback.answer()

dp.include_router(router)

if __name__ == '__main__':
    dp.run_polling(bot)