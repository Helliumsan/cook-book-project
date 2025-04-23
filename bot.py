import asyncio
import logging


from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7574317784:AAH8RHO_BGCuV4egptvdRvsUtwF5o7bd2bU")
dp = Dispatcher()
#_________________________________________________________________________________________________________________________________________________
busy_bunny_photo = 'AgACAgIAAxkBAAIBjGftXllU6EfUHWjrW2ZhyESs3BzuAAI08TEbjrZwSxc_-IBZAAF_VgEAAwIAA3kAAzYE'
strawberry_kitty_photo = 'AgACAgIAAxkBAAIBjmftXmuRuTJMgVuEOnyGSyVBdrDxAAI38TEbjrZwSyMXIi5sAfYfAQADAgADeQADNgQ'
anxious_kitty_photo = 'AgACAgIAAxkBAAIBjmftXmuRuTJMgVuEOnyGSyVBdrDxAAI38TEbjrZwSyMXIi5sAfYfAQADAgADeQADNgQ'
alien_puppy_photo = 'AgACAgIAAxkBAAIBkmftXoG8R4tWdL0Oi_UHHbkBaJaMAAI68TEbjrZwS7jtYDVelqKfAQADAgADeQADNgQ'

scores=[0,0,0,0] #жёлтый, розовый, голубой, зелёный
results=['Деловой зайчик','Сладкий котик','Тревожный котик','Инопланетный щеночек']
results_photos=[busy_bunny_photo,strawberry_kitty_photo,anxious_kitty_photo,alien_puppy_photo]
#_________________________________________________________________________________________________________________________________________________
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb=[[types.KeyboardButton(text='Начнём!')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Добро пожаловать в тест, в котором ты сможешь узнать, на какое из четырёх маленьких забавных существ ты похож.\nНачнём?',reply_markup=keyboard)

#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text=='Начнём!')
async def first_question(message: types.Message):
    kb = [[types.KeyboardButton(text='Осень')],[types.KeyboardButton(text='Лето')],[types.KeyboardButton(text='Зима')],[types.KeyboardButton(text='Весна')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("1) Какое твоё любимое время года?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "осень")
async def second_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Жёлтый')],[types.KeyboardButton(text='Розовый')],[types.KeyboardButton(text='Голубой')],[types.KeyboardButton(text='Зелёный')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("2) Какой цвет тебе нравится больше остальных?",reply_markup=keyboard)

@dp.message(F.text.lower() == "лето")
async def second_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Жёлтый')],[types.KeyboardButton(text='Розовый')],[types.KeyboardButton(text='Голубой')],[types.KeyboardButton(text='Зелёный')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("2) Какой цвет тебе нравится больше остальных?",reply_markup=keyboard)

@dp.message(F.text.lower() == "зима")
async def second_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Жёлтый')],[types.KeyboardButton(text='Розовый')],[types.KeyboardButton(text='Голубой')],[types.KeyboardButton(text='Зелёный')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("2) Какой цвет тебе нравится больше остальных?",reply_markup=keyboard)

@dp.message(F.text.lower() == "весна")
async def second_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Жёлтый')],[types.KeyboardButton(text='Розовый')],[types.KeyboardButton(text='Голубой')],[types.KeyboardButton(text='Зелёный')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("2) Какой цвет тебе нравится больше остальных?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________

@dp.message(F.text.lower() == "жёлтый")
async def third_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Скорее да, чем нет')],[types.KeyboardButton(text='На дух не переношу путешествия')],[types.KeyboardButton(text='Не могу представить свою жизнь без путешествий')],[types.KeyboardButton(text='Люблю, но тяжело переношу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("3) Нравится ли тебе путешествовать?",reply_markup=keyboard)

@dp.message(F.text.lower() == "розовый")
async def third_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Скорее да, чем нет')],[types.KeyboardButton(text='На дух не переношу путешествия')],[types.KeyboardButton(text='Не могу представить свою жизнь без путешествий')],[types.KeyboardButton(text='Люблю, но тяжело переношу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("3) Нравится ли тебе путешествовать?",reply_markup=keyboard)

@dp.message(F.text.lower() == "голубой")
async def third_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Скорее да, чем нет')],[types.KeyboardButton(text='На дух не переношу путешествия')],[types.KeyboardButton(text='Не могу представить свою жизнь без путешествий')],[types.KeyboardButton(text='Люблю, но тяжело переношу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("3) Нравится ли тебе путешествовать?",reply_markup=keyboard)

@dp.message(F.text.lower() == "зелёный")
async def third_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Скорее да, чем нет')],[types.KeyboardButton(text='На дух не переношу путешествия')],[types.KeyboardButton(text='Не могу представить свою жизнь без путешествий')],[types.KeyboardButton(text='Люблю, но тяжело переношу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("3) Нравится ли тебе путешествовать?",reply_markup=keyboard)

#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "скорее да, чем нет")
async def fourth_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Немного сладкого иногда полезно для души')],[types.KeyboardButton(text='Если бы мог, я бы ел только сладости')],[types.KeyboardButton(text='Сладкое? Через мой труп')],[types.KeyboardButton(text='Съем если дадут')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("4) Как относишься к сладостям?",reply_markup=keyboard)

@dp.message(F.text.lower() == "на дух не переношу путешествия")
async def fourth_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Немного сладкого иногда полезно для души')],[types.KeyboardButton(text='Если бы мог, я бы ел только сладости')],[types.KeyboardButton(text='Сладкое? Через мой труп')],[types.KeyboardButton(text='Съем если дадут')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("4) Как относишься к сладостям?",reply_markup=keyboard)

@dp.message(F.text.lower() == "не могу представить свою жизнь без путешествий")
async def fourth_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Немного сладкого иногда полезно для души')],[types.KeyboardButton(text='Если бы мог, я бы ел только сладости')],[types.KeyboardButton(text='Сладкое? Через мой труп')],[types.KeyboardButton(text='Съем если дадут')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("4) Как относишься к сладостям?",reply_markup=keyboard)

@dp.message(F.text.lower() == "люблю, но тяжело переношу")
async def fourth_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Немного сладкого иногда полезно для души')],[types.KeyboardButton(text='Если бы мог, я бы ел только сладости')],[types.KeyboardButton(text='Сладкое? Через мой труп')],[types.KeyboardButton(text='Съем если дадут')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("4) Как относишься к сладостям?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "немного сладкого иногда полезно для души")
async def fifth_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Удобство важнее, но и красота важна')],[types.KeyboardButton(text='Красивая')],[types.KeyboardButton(text='Удобство превыше всего')],[types.KeyboardButton(text='Удобная и красивая')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("5) Удобная или красивая одежда?",reply_markup=keyboard)

@dp.message(F.text.lower() == "если бы мог, я бы ел только сладости")
async def fifth_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Удобство важнее, но и красота важна')],[types.KeyboardButton(text='Красивая')],[types.KeyboardButton(text='Удобство превыше всего')],[types.KeyboardButton(text='Удобная и красивая')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("5) Удобная или красивая одежда?",reply_markup=keyboard)

@dp.message(F.text.lower() == "сладкое? через мой труп")
async def fifth_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Удобство важнее, но и красота важна')],[types.KeyboardButton(text='Красивая')],[types.KeyboardButton(text='Удобство превыше всего')],[types.KeyboardButton(text='Удобная и красивая')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("5) Удобная или красивая одежда?",reply_markup=keyboard)

@dp.message(F.text.lower() == "съем если дадут")
async def fifth_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Удобство важнее, но и красота важна')],[types.KeyboardButton(text='Красивая')],[types.KeyboardButton(text='Удобство превыше всего')],[types.KeyboardButton(text='Удобная и красивая')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("5) Удобная или красивая одежда?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "удобство важнее, но и красота важна")
async def sixth_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Пять-шесть часов')],[types.KeyboardButton(text='Три? Пять? Не помню')],[types.KeyboardButton(text='Меньше двух, мне некогда')],[types.KeyboardButton(text='Столько же сколько бодрствую')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("6) Сколько часов в день проводишь перед монитором?",reply_markup=keyboard)

@dp.message(F.text.lower() == "красивая")
async def sixth_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Пять-шесть часов')],[types.KeyboardButton(text='Три? Пять? Не помню')],[types.KeyboardButton(text='Меньше двух, мне некогда')],[types.KeyboardButton(text='Столько же сколько бодрствую')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("6) Сколько часов в день проводишь перед монитором?",reply_markup=keyboard)

@dp.message(F.text.lower() == "удобство превыше всего")
async def sixth_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Пять-шесть часов')],[types.KeyboardButton(text='Три? Пять? Не помню')],[types.KeyboardButton(text='Меньше двух, мне некогда')],[types.KeyboardButton(text='Столько же сколько бодрствую')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("6) Сколько часов в день проводишь перед монитором?",reply_markup=keyboard)

@dp.message(F.text.lower() == "удобная и красивая")
async def sixth_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Пять-шесть часов')],[types.KeyboardButton(text='Три? Пять? Не помню')],[types.KeyboardButton(text='Меньше двух, мне некогда')],[types.KeyboardButton(text='Столько же сколько бодрствую')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("6) Сколько часов в день проводишь перед монитором?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "пять-шесть часов")
async def seventh_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Тихая, с небольшой облачностью')],[types.KeyboardButton(text='Грибной дождь')],[types.KeyboardButton(text='Полный штиль')],[types.KeyboardButton(text='Ливень и гроза')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("7) Какая погода для тебя самая приятная?",reply_markup=keyboard)

@dp.message(F.text.lower() == "три? пять? не помню")
async def seventh_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Тихая, с небольшой облачностью')],[types.KeyboardButton(text='Грибной дождь')],[types.KeyboardButton(text='Полный штиль')],[types.KeyboardButton(text='Ливень и гроза')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("7) Какая погода для тебя самая приятная?",reply_markup=keyboard)

@dp.message(F.text.lower() == "меньше двух, мне некогда")
async def seventh_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Тихая, с небольшой облачностью')],[types.KeyboardButton(text='Грибной дождь')],[types.KeyboardButton(text='Полный штиль')],[types.KeyboardButton(text='Ливень и гроза')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("7) Какая погода для тебя самая приятная?",reply_markup=keyboard)

@dp.message(F.text.lower() == "столько же сколько бодрствую")
async def seventh_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Тихая, с небольшой облачностью')],[types.KeyboardButton(text='Грибной дождь')],[types.KeyboardButton(text='Полный штиль')],[types.KeyboardButton(text='Ливень и гроза')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("7) Какая погода для тебя самая приятная?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "тихая, с небольшой облачностью")
async def eighth_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Низких')],[types.KeyboardButton(text='Высоких')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("8) Жить на низких или высоких этажах?",reply_markup=keyboard)

@dp.message(F.text.lower() == "грибной дождь")
async def eighth_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Низких')],[types.KeyboardButton(text='Высоких')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("8) Жить на низких или высоких этажах?",reply_markup=keyboard)

@dp.message(F.text.lower() == "полный штиль")
async def eighth_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Низких')],[types.KeyboardButton(text='Высоких')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("8) Жить на низких или высоких этажах?",reply_markup=keyboard)

@dp.message(F.text.lower() == "ливень и гроза")
async def eighth_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Низких')],[types.KeyboardButton(text='Высоких')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("8) Жить на низких или высоких этажах?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "низких")
async def ninth_question(message: types.Message):
    scores[0] += 1
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Любить')],[types.KeyboardButton(text='Быть любимым')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("9) Любить или быть любимым?",reply_markup=keyboard)

@dp.message(F.text.lower() == "высоких")
async def ninth_question(message: types.Message):
    scores[2] += 1
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Любить')],[types.KeyboardButton(text='Быть любимым')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("9) Любить или быть любимым?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "любить")
async def tenth_question(message: types.Message):
    scores[0] += 1
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Вся моя жизнь проходит под музыку')],[types.KeyboardButton(text='Не очень, по настроению обычно')],[types.KeyboardButton(text='Время от времени, чтобы отвлечься')],[types.KeyboardButton(text='Нет, терпеть музыку не могу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("10) Часто ли вы слушаете музыку?",reply_markup=keyboard)

@dp.message(F.text.lower() == "быть любимым")
async def tenth_question(message: types.Message):
    scores[1] += 1
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Вся моя жизнь проходит под музыку')],[types.KeyboardButton(text='Не очень, по настроению обычно')],[types.KeyboardButton(text='Время от времени, чтобы отвлечься')],[types.KeyboardButton(text='Нет, терпеть музыку не могу')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("10) Часто ли вы слушаете музыку?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "вся моя жизнь проходит под музыку")
async def result_question(message: types.Message):
    scores[0] += 1
    kb = [[types.KeyboardButton(text='Да!')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тест пройден! Готов узнать результат?",reply_markup=keyboard)

@dp.message(F.text.lower() == "не очень, по настроению обычно")
async def result_question(message: types.Message):
    scores[1] += 1
    kb = [[types.KeyboardButton(text='Да!')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тест пройден! Готов узнать результат?",reply_markup=keyboard)

@dp.message(F.text.lower() == "время от времени, чтобы отвлечься")
async def result_question(message: types.Message):
    scores[2] += 1
    kb = [[types.KeyboardButton(text='Да!')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тест пройден! Готов узнать результат?",reply_markup=keyboard)

@dp.message(F.text.lower() == "нет, терпеть музыку не могу")
async def result_question(message: types.Message):
    scores[3] += 1
    kb = [[types.KeyboardButton(text='Да!')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тест пройден! Готов узнать результат?",reply_markup=keyboard)
#_________________________________________________________________________________________________________________________________________________
@dp.message(F.text.lower() == "да!")
async def creature_question(message: types.Message):
    if scores.index(max(scores))==0:
        await bot.send_photo(chat_id=message.chat.id, photo=busy_bunny_photo,
                             caption=f"Поздравляю! Твой результат - {results[scores.index(max(scores))]}!")

    elif scores.index(max(scores))==1:
        await bot.send_photo(chat_id=message.chat.id, photo=strawberry_kitty_photo,
                             caption=f"Поздравляю! Твой результат - {results[scores.index(max(scores))]}!")

    elif scores.index(max(scores))==2:
        await bot.send_photo(chat_id=message.chat.id, photo=anxious_kitty_photo,
                             caption=f"Поздравляю! Твой результат - {results[scores.index(max(scores))]}!")

    elif scores.index(max(scores))==3:
        await bot.send_photo(chat_id=message.chat.id, photo=alien_puppy_photo,
                             caption=f"Поздравляю! Твой результат - {results[scores.index(max(scores))]}!")

#_________________________________________________________________________________________________________________________________________________
async def main():
    await dp.start_polling(bot)
    dp.message.register(first_question, F.text)
    dp.message.register(second_question, F.text)
    dp.message.register(third_question, F.text)
    dp.message.register(fourth_question, F.text)
    dp.message.register(fifth_question, F.text)
    dp.message.register(sixth_question, F.text)
    dp.message.register(seventh_question, F.text)
    dp.message.register(eighth_question, F.text)
    dp.message.register(ninth_question, F.text)
    dp.message.register(tenth_question, F.text)
    dp.message.register(result_question, F.text)
    dp.message.register(creature_question, F.text)

if __name__ == "__main__":
    asyncio.run(main())




