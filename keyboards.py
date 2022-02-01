from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb=CallbackData('model')


keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text="Samsung"),
            KeyboardButton(text="Herox")
        ],
        [
            KeyboardButton(text="HP"),
            KeyboardButton(text="Canon")
        ],
        [
            KeyboardButton(text="Help")
        ]
    ],
    resize_keyboard=True
)



keyboard1=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Model_1',callback_data='Samsung_Model_1')
            

        ],
        [
            InlineKeyboardButton(text='Model_2',callback_data='Samsung_Model_2')
        ],
        [
            InlineKeyboardButton(text='Model_3', callback_data='Samsung_Model_3')
        ],
        [
            InlineKeyboardButton(text='Model_4', callback_data='Samsung_Model_4')
        ],
        [
            InlineKeyboardButton(text='Model_5', callback_data='Samsung_Model_5')
        ]
    ]
)

keyboard2=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Model_1',callback_data='Herox_Model_1')
        ],
        [
            InlineKeyboardButton(text='Model_2',callback_data='Herox_Model_2')
        ],
        [
            InlineKeyboardButton(text='Model_3', callback_data='Herox_Model_3')
        ]
    ]
)

keyboard3=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Model_1',callback_data='HP_Model_1')
        ],
        [
            InlineKeyboardButton(text='Model_2',callback_data='HP_Model_2')
        ]
    ]
)

keyboard4=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Model_1',callback_data='Canon_Model_1')
        ],
        [
            InlineKeyboardButton(text='Model_2',callback_data='Canon_Model_2')
        ],
        [
            InlineKeyboardButton(text='Model_3',callback_data='Canon_Model_3')
        ],
        [
            InlineKeyboardButton(text='Model_4',callback_data='Canon_Model_4')
        ]
    ]
)

