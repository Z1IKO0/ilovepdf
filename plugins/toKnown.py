# fileName : plugins/toKnown.py
# copyright ©️ 2021 nabilanavab




from pyrogram.types import Message
from plugins.fileSize import get_size_format as gSF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup




#--------------->
#--------> LOCAL VARIABLES
#------------------->

pdfInfoMsg = """`Bu faylla nə etmək istərdin?`

Fayl Adı : `{}`
Fayl Həcmi : `{}`

Səhifə sayı {}`📄"""

#--------------->
#--------> CHECKPDF MESAJINI DÜZENLE (ƏGƏR PDF ŞİFRELƏMƏMƏSİNSƏ)
#------------------->

# convert unknown to known page number msgs
async def toKnown(callbackQuery, number_of_pages):
    try:
        fileName = callbackQuery.message.reply_to_message.document.file_name
        fileSize = callbackQuery.message.reply_to_message.document.file_size
        
        await callbackQuery.edit_message_text(
            pdfInfoMsg.format(
                fileName, await gSF(fileSize), number_of_pages
            ),
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⭐ get page No & info ⭐",
                            callback_data=f"KpdfInfo|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Şəkil 🖼️",
                            callback_data=f"KtoImage|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Tekst ✏️",
                            callback_data=f"KtoText|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Şifrələyin 🔐",
                            callback_data=f"Kencrypt|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Şifrəni açın 🔓",
                            callback_data=f"notEncrypted"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Kompress 🗜️",
                            callback_data=f"Kcompress"
                        ),
                        InlineKeyboardButton(
                            "Döndürün 🤸",
                            callback_data=f"Krotate|{number_of_pages}"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                           "Bölün ✂️",
                            callback_data=f"Ksplit|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Birləşdirin 🧬",
                            callback_data="merge"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Möhürlüyün ™️",
                            callback_data=f"Kstamp|{number_of_pages}"
                        ),
                        InlineKeyboardButton(
                            "Adını dəyiş ✏️",
                            callback_data="rename"
                        )
                    ]
                ]
            )
        )
    except Exception as e:
        print(f"plugins/toKnown: {e}")


#                                                                                  Telegram: @nabilanavab
