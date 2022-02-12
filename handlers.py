
from aiogram.types import Message,ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard, keyboard1, keyboard2,keyboard3,keyboard4
from aiogram import Bot, Dispatcher, executor, types
from main import bot, dp
from preparation import open_new_file, orm_apply_add, select_brand
from datetime import datetime

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Choose a <strong>brand</strong> of your equipment:", reply_markup=keyboard)



@dp.message_handler(commands="help")
async def cmd_start(message: types.Message):
    await message.answer("Welcome to our company’s bot!\n \
        Here you can check instantly actual prices for service.\n\
            <strong>Contacts:</strong> Las Vegas, boulevard Z, 999.\n \
            <b>&#9990;</b> 44-123-34-45", reply_markup=None)
            
@dp.message_handler(commands="admin")
async def cmd_start(message: types.Message):
    await message.answer("Dear Admins! \n \
        Due to protection, please send using <strong>SFTP</strong> actual csv-file.\n\
        Dear Teachers, in my github you will find an example of <i>printers.csv</i> and also during \
        conversation I can show how the bot handles this file.\n \
        After loading cvs-file, please use command <strong>/addnewprice</strong>.", reply_markup=None)


@dp.message_handler(Text(equals=["Help"]))
async def get_goods(message: Message):
    await message.answer("Welcome to our company’s bot!\n \
        Here you can check instantly actual prices for service.\n\
            <strong>Contacts:</strong> Las Vegas, boulevard Z, 999.\n\
            <b>&#9990;</b> 44-123-34-45", reply_markup=None)



@dp.message_handler(Command('addnewprice'))
async def add_cmd(message:Message):
    orm_apply_add(open_new_file("printers1.csv"))
    await message.answer('new prices were loaded into DB')

#---------Samsung-------------------

@dp.message_handler(Text(equals=["Samsung"]))
async def get_goods(message: Message):
    fout = open("db_button_push_log.txt","a")
    out="Button Samsung was pushed at "+str(datetime.now())+" \n"
    fout.write(out)
    fout.close()
    await message.answer("Choose a <strong>model</strong> of your equipment: Samsung", reply_markup=keyboard1)

@dp.callback_query_handler(text_contains='Samsung_Model_1')
async def model_1(call:CallbackQuery):
    arrSamsung=select_brand("samsung")
    tup=arrSamsung[0]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Samsung \"model 1\":</strong>",reply_markup=None)
    print("this is a tuple Samsung Model_1",tup)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None) #!!!!!


@dp.callback_query_handler(text_contains='Samsung_Model_2')
async def model_2(call:CallbackQuery):
    arrSamsung=select_brand("samsung")
    tup=arrSamsung[1]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Samsung \"model 2\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)


@dp.callback_query_handler(text_contains='Samsung_Model_3')
async def model_3(call:CallbackQuery):
    arrSamsung=select_brand("samsung")
    tup=arrSamsung[2]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Samsung \"model 3\":</strong>",reply_markup=None)    
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Samsung_Model_4')
async def model_3(call:CallbackQuery):
    arrSamsung=select_brand("samsung")
    tup=arrSamsung[3]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Samsung \"model 4\":</strong>",reply_markup=None)    
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Samsung_Model_5')
async def model_3(call:CallbackQuery):
    arrSamsung=select_brand("samsung")
    tup=arrSamsung[4]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Samsung \"model 5\":</strong>",reply_markup=None) 
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)


#---------------Herox---------------------
@dp.message_handler(Text(equals=["Herox"]))
async def get_goods(message: Message):
    fout = open("db_button_push_log.txt","a")
    out="Button Herox was pushed at "+str(datetime.now())+" \n"
    fout.write(out)
    fout.close()
    await message.answer("Choose a <strong>model</strong> of your equipment: Herox", reply_markup=keyboard2)

@dp.callback_query_handler(text_contains='Herox_Model_1')
async def model_1(call:CallbackQuery):
    arrHerox=select_brand("herox")
    tup=arrHerox[0]
    print("this is a tuple Samsung Model_1",tup)
    textus=""
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Herox \"model 1\":</strong>",reply_markup=None) 
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Herox_Model_2')
async def model_2(call:CallbackQuery):
    arrHerox=select_brand("herox")
    tup=arrHerox[1]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Herox \"model 2\":</strong>",reply_markup=None) 
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Herox_Model_3')
async def model_3(call:CallbackQuery):
    arrHerox=select_brand("herox")
    tup=arrHerox[2]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Herox \"model 3\":</strong>",reply_markup=None) 
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)


#------------------------HP-----------------------

@dp.message_handler(Text(equals=["HP"]))
async def get_goods(message: Message):
    fout = open("db_button_push_log.txt","a")
    out="Button HP was pushed at "+str(datetime.now())+" \n"
    fout.write(out)
    fout.close()
    await message.answer("Choose a <strong>model</strong> of your equipment: HP", reply_markup=keyboard3)

@dp.callback_query_handler(text_contains='HP_Model_1')
async def model_1(call:CallbackQuery):
    arrHP=select_brand("hp")
    tup=arrHP[0]
    print("this is a tuple HP Model_1",tup)
    await call.answer(cache_time=20)
    await call.message.answer("<strong>Price for HP \"model 1\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='HP_Model_2')
async def model_2(call:CallbackQuery):
    arrHP=select_brand("hp")
    tup=arrHP[1]
    await call.answer(cache_time=20)
    await call.message.answer("<strong>Price for HP \"model 2\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)


#------------------------Canon-----------------------

@dp.message_handler(Text(equals=["Canon"]))
async def get_goods(message: Message):
    fout = open("db_button_push_log.txt","a")
    out="Button Canon was pushed at "+str(datetime.now())+" \n"
    fout.write(out)
    fout.close()
    await message.answer("Choose a <strong>model</strong> of your equipment: Canon", reply_markup=keyboard4)

@dp.callback_query_handler(text_contains='Canon_Model_1')
async def model_1(call:CallbackQuery):
    arrCanon=select_brand("canon")
    tup=arrCanon[0]
    print("this is a tuple Canon Model_1",tup)
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Canon \"model 1\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Canon_Model_2')
async def model_2(call:CallbackQuery):
    arrCanon=select_brand("canon")
    tup=arrCanon[1]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Canon \"model 2\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Canon_Model_3')
async def model_3(call:CallbackQuery):
    arrCanon=select_brand("canon")
    tup=arrCanon[2]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Canon \"model 3\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

@dp.callback_query_handler(text_contains='Canon_Model_4')
async def model_4(call:CallbackQuery):
    arrCanon=select_brand("canon")
    tup=arrCanon[3]
    await call.answer(cache_time=60)
    await call.message.answer("<strong>Price for Canon \"model 4\":</strong>",reply_markup=None)
    textus=""
    for i in range(3):
        textus=textus+"service #"+str(i+1)+": "+str(tup[i+2])+"&#8381;\n"
    await call.answer(cache_time=60)
    await call.message.answer(textus,reply_markup=None)

