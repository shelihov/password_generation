from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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