from aiogram.types import *

menu_1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Botning xabarlarini boshqarish'),KeyboardButton(text=f'B) Telegram API bilan muloqot qilish uchun ishlatiladi')],
        [KeyboardButton(text=f'C) Foydalanuvchi malumotlarini saqlash'), KeyboardButton(text=f'D) Inline tugmalar yaratish')],
    ],
    resize_keyboard=True
)
menu_2=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Telegram botining tokenini olish'),KeyboardButton(text=f'B) Xabarlarni filtrlash va ularga ishlov berish')],
        [KeyboardButton(text=f'C)  Inline tugmalarni boshqarish'), KeyboardButton(text=f'D) oFoydalanuvchi malumotlarini yuborish')],
    ],
    resize_keyboard=True
)

menu_3=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) /stop buyrugi'),KeyboardButton(text=f'B) /help buyrugi')],
        [KeyboardButton(text=f'C)  /start buyrugi'), KeyboardButton(text=f'D)Foydalanuvchi matni')],
    ],
    resize_keyboard=True
)

menu_4=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)Botning barcha foydalanuvchilari uchun bir xil holatni saqlash'),KeyboardButton(text=f'B)  Botning ishga tushishini taminlash')],
        [KeyboardButton(text=f'C)Foydalanuvchilar uchun vaqtinchalik holatlarni saqlash '), KeyboardButton(text=f'D)Inline tugmalarni yaratish')],
    ],
    resize_keyboard=True
)

menu_5=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)Flexible State Management'),KeyboardButton(text=f'B)Finite State Machine')],
        [KeyboardButton(text=f'C)Function State Management'), KeyboardButton(text=f'D) Filtered State Machine')],
    ],
    resize_keyboard=True
)

menu_6=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)Inline tugmalarni yaratish'),KeyboardButton(text=f'B)Bot tokenini aniqlash')],
        [KeyboardButton(text=f'C)Foydalanuvchi holatini boshqarish va saqlash '), KeyboardButton(text=f'D) Bot ishini toxtatish')],
    ],
    resize_keyboard=True
)

menu_7=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Foydalanuvchi xabarini ekranga chiqarish'),KeyboardButton(text=f'B)Foydalanuvchi malumotlarini holatda saqlash ')],
        [KeyboardButton(text=f'C)Xabar yuborish'), KeyboardButton(text=f'D) Tugma yaratish')],
    ],
    resize_keyboard=True
)

menu_8=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Oddiy matnli xabarlar'),KeyboardButton(text=f'B)oInline tugmalardan kelgan javoblar ')],
        [KeyboardButton(text=f'C)Foydalanuvchi kontaktlari'), KeyboardButton(text=f'D) Foydalanuvchi rasmlari')],
    ],
    resize_keyboard=True
)

menu_9=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) message.text'),KeyboardButton(text=f'B) call.data ')],
        [KeyboardButton(text=f'C)message.reply_markup'), KeyboardButton(text=f'D) call.reply')],
    ],
    resize_keyboard=True
)

menu_10=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Botni toxtatish'),KeyboardButton(text=f'B) Foydalanuvchi xabarlarini tekshirish va ularga javob qaytarish ')],
        [KeyboardButton(text=f'C)Inline tugmalarni boshqarish'), KeyboardButton(text=f'D) Bot tokenini yangilash')],
    ],
    resize_keyboard=True
)

menu_11=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Foydalanuvchining oladi malumotlarini holatdan '),KeyboardButton(text=f'B) Foydalanuvchi yuborgan xabar matnini')],
        [KeyboardButton(text=f'C) Xabarni yuborish uchun tugmalarni'), KeyboardButton(text=f'D) Bot tokenini')],
    ],
    resize_keyboard=True
)
menu_12=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) state.get_data()'),KeyboardButton(text=f'B) state.update_data()')],
        [KeyboardButton(text=f'C) state.set_state() '), KeyboardButton(text=f'D) state.reset_state()')],
    ],
    resize_keyboard=True
)
menu_13=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) types.ReplyKeyboardMarkup'),KeyboardButton(text=f'B) types.InlineKeyboardMarkup ')],
        [KeyboardButton(text=f'C) types.ForceReply'), KeyboardButton(text=f'D) types.KeyboardButton')],
    ],
    resize_keyboard=True
)
menu_14=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) state elon qilinmagan '),KeyboardButton(text=f'B) call.message.text notogri ishlatilgan')],
        [KeyboardButton(text=f'C) CallbackQuery ishlatilishi kerak emas'), KeyboardButton(text=f'D) Xato yoq')],
    ],
    resize_keyboard=True
)
menu_15=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Yangi holat ornatish )'),KeyboardButton(text=f'B) Holatni ochirish')],
        [KeyboardButton(text=f'C) Inline tugmalarni yangilash'), KeyboardButton(text=f'D) Callbackni yuborish')],
    ],
    resize_keyboard=True
)
menu_16=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Tugma malumotlari'),KeyboardButton(text=f'B) Foydalanuvchi yuborgan xabar matni')],
        [KeyboardButton(text=f'C) Bot tokeni'), KeyboardButton(text=f'D) Holat malumotlari')],
    ],
    resize_keyboard=True
)
menu_17=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)Bir nechta foydalanuvchi uchun vaqtinchalik malumotlarni boshqarish kerak bolganda '),KeyboardButton(text=f'B)Xabar yuborish uchun')],
        [KeyboardButton(text=f'C)Inline tugmalarni yaratish uchun'), KeyboardButton(text=f'D)Botni boshlash uchun')],
    ],
    resize_keyboard=True
)
menu_18=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)Tugma bosilganda yuboriladigan qiymat sifatida'),KeyboardButton(text=f'B) Xabar matni sifatida')],
        [KeyboardButton(text=f'C)Token qiymati sifatida'), KeyboardButton(text=f'D) Tugmani ochirish uchun')],
    ],
    resize_keyboard=True
)
menu_19=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A) Foydalanuvchi xabarlarini qayta ishlash uchun '),KeyboardButton(text=f'B) Callback tugmalarni boshqarish uchun')],
        [KeyboardButton(text=f'C) Bot tokenini aniqlash uchun'), KeyboardButton(text=f'D) Holatlarni ochirish uchun')],
    ],
    resize_keyboard=True
)
menu_20=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f'A)bot.send_message(chat_id, text)'),KeyboardButton(text=f'B)await message.answer(text)')],
        [KeyboardButton(text=f'C)dp.send_message(text)'), KeyboardButton(text=f'D) state.update_data()')],
    ],
    resize_keyboard=True
)