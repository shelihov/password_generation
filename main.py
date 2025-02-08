import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

BOT_TOKEN = '7923159442:AAHSTM3XUMKtgt8LuBp6yWX_2IChuuKQPJY'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
router = Router()

user_data = {}

#Кнопки
button_q1 = InlineKeyboardButton(text='1', callback_data='q1')
button_q2 = InlineKeyboardButton(text='3', callback_data='q3')
button_q3 = InlineKeyboardButton(text='5', callback_data='q5')

button_len1 = InlineKeyboardButton(text='15', callback_data='l15')
button_len2 = InlineKeyboardButton(text='20', callback_data='l20')
button_len3 = InlineKeyboardButton(text='25', callback_data='l25')

button_yes_digit = InlineKeyboardButton(text='Да ✅', callback_data='yes_digit')
button_no_digit = InlineKeyboardButton(text='Нет ❌', callback_data='no_digit')

button_yes_upper = InlineKeyboardButton(text='Да ✅', callback_data='yes_upper')
button_no_upper = InlineKeyboardButton(text='Нет ❌', callback_data='no_upper')

button_yes_simbols = InlineKeyboardButton(text='Да ✅', callback_data='yes_simbols')
button_no_simbols = InlineKeyboardButton(text='Нет ❌', callback_data='no_simbols')

button_generations = InlineKeyboardButton(text='Сгенерировать', callback_data='generations')

button_repeat = InlineKeyboardButton(text='Повторить', callback_data='repeat')
button_stop = InlineKeyboardButton(text='Cтоп', callback_data='stop')

#Клавиатуры
keyboard_quantity = InlineKeyboardMarkup(inline_keyboard=[
    [button_q1, button_q2, button_q3]
])
keyboard_len = InlineKeyboardMarkup(inline_keyboard=[
    [button_len1, button_len2, button_len3]
])
keyboard_digit = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_digit, button_no_digit]
])
keyboard_upper = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_upper, button_no_upper]
])
keyboard_simbols = InlineKeyboardMarkup(inline_keyboard=[
    [button_yes_simbols, button_no_simbols]
])
keyboard_generations = InlineKeyboardMarkup(inline_keyboard=[
    [button_generations]
])
keyboard_repeat = InlineKeyboardMarkup(inline_keyboard=[
    [button_repeat, button_stop]
])


digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'


@router.message(Command("start"))
async def process_start_command(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {
        'chars': 'abcdefghijklmnopqrstuvwxyz',
        'quantity': 0,
        'len_s': 0
    }
    hello_text = 'Привет! Это бот - <b>генератор надежных паролей</b>, ответь на несколько вопросов и я пришлю тебе пароль.'
    await message.answer(hello_text, parse_mode="HTML")
    await message.answer('Количество паролей для генерации:', reply_markup=keyboard_quantity)


#обработка коллбэков кол-во паролей
@router.callback_query(F.data.in_(['q1', 'q3', 'q5']))
async def handler_quantity(callback: CallbackQuery):
    user_id = callback.from_user.id
    quantity = int(callback.data[1])
    user_data[user_id]['quantity'] = quantity
    await callback.message.answer(f'Кол-во паролей = {quantity}')
    await callback.message.answer('Введите длину пароля:', reply_markup=keyboard_len)
    await callback.answer()

#обработка коллбэков клавиатуры запроса длинны пароля
@router.callback_query(F.data.in_(['l15', 'l20', 'l25']))
async def handler_quantity(callback: CallbackQuery):
    user_id = callback.from_user.id
    len_s = int(callback.data[1:])
    user_data[user_id]['len_s'] = len_s
    await callback.message.answer(f'Длина пароля = {len_s} символов')
    await callback.message.answer('Включать ли цифры?', reply_markup=keyboard_digit)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли цифры'
@router.callback_query(F.data.in_(['yes_digit', 'no_digit']))
async def handler_digits(callback: CallbackQuery):
    user_id = callback.from_user.id
    if callback.data == 'yes_digit':
        user_data[user_id]['chars'] += digits
        await callback.message.answer(f'Цифры включены')
    else:
        await callback.message.answer(f'Цифры не включены')    
    await callback.message.answer('Включать ли заглавные буквы?', reply_markup=keyboard_upper)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли заглавные'
@router.callback_query(F.data.in_(['yes_upper', 'no_upper']))
async def handler_upper(callback: CallbackQuery):
    user_id = callback.from_user.id
    if callback.data == 'yes_upper':
        user_data[user_id]['chars'] += uppercase_letters
        await callback.message.answer(f'Заглавные буквы включены')
    else:
        await callback.message.answer(f'Заглавные буквы не включены')
    await callback.message.answer('Включать ли символы?', reply_markup=keyboard_simbols)
    await callback.answer()


#обработка коллбэков клавиатуры 'нужны ли символы'
@router.callback_query(F.data.in_(['yes_simbols', 'no_simbols']))
async def handler_yes_simbols(callback: CallbackQuery):
    user_id = callback.from_user.id
    if callback.data == 'yes_simbols':
        user_data[user_id]['chars'] += punctuation
        await callback.message.edit_text('Символы включены')
    else:
        await callback.message.edit_text('Символы не включены')
    await callback.message.answer('Готово! Нажмите "Сгенерировать".', reply_markup=keyboard_generations)
    await callback.answer()

# генерация
@router.callback_query(F.data == 'generations')
async def handler_generation(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = user_data.get(user_id, {})
    chars = data.get('chars', '')
    quantity = data.get('quantity', 0)
    len_s = data.get('len_s', 0)

    if not chars or not quantity or not len_s:
        await callback.message.answer('Ошибка: не все параметры заданы. Начните снова.')
        return
    
    passwords = []
    for _ in range(quantity):
        password = ''.join(random.choice(chars) for _ in range(len_s))
        passwords.append(password)

    await callback.message.edit_text(f'Сгенерированные пароли:\n\n' + '\n'.join(passwords))
    await callback.message.answer('Повторить генерацию?', reply_markup=keyboard_repeat)
    await callback.answer()   


#обработка коллбэков клавиатуры 'repeat and stop'
@router.callback_query(F.data.in_(['repeat', 'stop']))
async def handler_repeat_or_stop(callback: CallbackQuery):
    user_id = callback.from_user.id
    if callback.data == 'repeat':
        await callback.message.answer('Начинаем заново.')
        await callback.message.answer('Нажмите "Сгенерировать".', reply_markup=keyboard_generations)
    else:
        await callback.message.edit_text('Генерация завершена. Для начала нажмите /start.')
        user_data.pop(user_id, None)
    await callback.answer()



dp.include_router(router)

if __name__ == '__main__':
    dp.run_polling(bot)