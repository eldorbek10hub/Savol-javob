import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from config import BOT_TOKEN
from button import * 
from state import SavolJavoblar


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Xush kelibsiz! Testni boshlash uchun /test komandasini yuboring.")

@dp.message(Command("test"))
async def first_question_handler(message: types.Message, state: FSMContext):
    await message.answer("1 - Aiogram kutubxonasida Bot obyektining vazifasi nima?", reply_markup=menu_1)
    await state.set_state(SavolJavoblar.bir_s)

@dp.message(SavolJavoblar.bir_s)
async def second_question_handler(message: types.Message, state: FSMContext):
    await message.answer("2 - Dispatcher obyektining asosiy vazifasi nima?", reply_markup=menu_2)
    await state.set_state(SavolJavoblar.ikki_s)

@dp.message(SavolJavoblar.ikki_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"3 - Quyidagi kod qaysi buyruq uchun handlerni belgilaydi?", reply_markup=menu_3)
    await state.set_state(SavolJavoblar.uch_s)

@dp.message(SavolJavoblar.uch_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"4 - MemoryStoragening vazifasi nima?", reply_markup=menu_4)
    await state.set_state(SavolJavoblar.tort_s)

@dp.message(SavolJavoblar.tort_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"5 - FSM qanday ma'noni anglatadi?", reply_markup=menu_5)
    await state.set_state(SavolJavoblar.besh_s)

@dp.message(SavolJavoblar.besh_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"6 - FSMContext obyektidan qanday maqsadda foydalaniladi?", reply_markup=menu_6)
    await state.set_state(SavolJavoblar.olti_s)

@dp.message(SavolJavoblar.olti_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"7 - Quyidagi kodning vazifasi nima?", reply_markup=menu_7)
    await state.set_state(SavolJavoblar.yetti_s)

@dp.message(SavolJavoblar.yetti_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"8 - @dp.callback_query handleri qaysi turdagi hodisalarni qayta ishlaydi?", reply_markup=menu_8)
    await state.set_state(SavolJavoblar.sakkiz_s)

@dp.message(SavolJavoblar.sakkiz_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"9 - CallbackQuery'da qaysi atribut tugma bosilganda qaytadi?", reply_markup=menu_9)
    await state.set_state(SavolJavoblar.toqqiz_s)

@dp.message(SavolJavoblar.toqqiz_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"10 - start_polling funksiyasining vazifasi nima", reply_markup=menu_10)
    await state.set_state(SavolJavoblar.on_s)

@dp.message(SavolJavoblar.on_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"11 - await state.get_data() kodi nimani qaytaradi?", reply_markup=menu_11)
    await state.set_state(SavolJavoblar.onb_s)

@dp.message(SavolJavoblar.onb_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"12.FSMda holatni o'zgartirish uchun qaysi usul ishlatiladi?", reply_markup=menu_12)
    await state.set_state(SavolJavoblar.oni_s)


@dp.message(SavolJavoblar.oni_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"13.  Aiogramda inline tugmalar qanday aniqlanadi?", reply_markup=menu_13)
    await state.set_state(SavolJavoblar.onu_s)


@dp.message(SavolJavoblar.onu_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"14.  python \n Copy code \n @dp.callback_query(royhatga_olish.Shahar) \n async def callback_handler(call: types.CallbackQuery): \n await state.update_data(shahar=call.message.text) \n", reply_markup=menu_13)
    await state.set_state(SavolJavoblar.ont_s)



@dp.message(SavolJavoblar.ont_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"15 - await state.set_state() funksiyasining vazifasi nima?", reply_markup=menu_15)
    await state.set_state(SavolJavoblar.onbe_s)    



@dp.message(SavolJavoblar.onbe_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"16.  types.Message obyekti orqali qaysi ma'lumotlarni olish mumkin?", reply_markup=menu_16)
    await state.set_state(SavolJavoblar.ono_s) 


@dp.message(SavolJavoblar.ono_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"17.  FSMni qaysi holatda ishlatish lozim?", reply_markup=menu_17)
    await state.set_state(SavolJavoblar.ony_s)

@dp.message(SavolJavoblar.ony_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"18.  Inline tugmalarni ishlatish uchun callback_data qanday aniqlanadi??", reply_markup=menu_18)
    await state.set_state(SavolJavoblar.ons_s)


@dp.message(SavolJavoblar.ons_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"19.  @dp.message dekoratori qanday ishlatiladi?", reply_markup=menu_19)
    await state.set_state(SavolJavoblar.ond_s) 


@dp.message(SavolJavoblar.ond_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"20.  Aiogramda xabarni foydalanuvchiga qanday yuboriladi?", reply_markup=menu_20)
    await state.set_state(SavolJavoblar.yigi_s)

@dp.message(SavolJavoblar.ond_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"20.  Aiogramda xabarni foydalanuvchiga qanday yuboriladi?", reply_markup=menu_20)
    await state.set_state(SavolJavoblar.yigi_s)


@dp.message(SavolJavoblar.yigi_s)
async def start_handler(message:types.Message,state:FSMContext):
    await message.answer(f"To`g`ri javoblar"
                         f'1-B \n'
                         f'2-B \n'
                         f'3-C \n'
                         f'4-C \n'
                         f'5-B \n'
                         f'6-C \n'
                         f'7-B \n'
                         f'8-B \n'
                         f'9-B \n'
                         f'10-B \n'
                         f'11-A \n'
                         f"12-C \n"
                         f'13-B \n'
                         f'14-A \n'
                         f"15-A \n"
                         f'16-B \n'
                         f'17-A \n'
                         f'18-A \n'
                         f'19-A \n'
                         f'20-B')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
