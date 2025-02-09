import random
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import *

router = Router()
user_data = {}

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