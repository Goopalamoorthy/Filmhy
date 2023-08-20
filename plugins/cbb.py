#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫🥴 : <a href='tg://user?id={OWNER_ID}'>𝐎𝐧𝐥𝐲 𝐏𝐢𝐞𝐜𝐞🍁</a>\n○ Language 🦞: <b>Python3.6</b>\n○ Library : <a href='https://t.me/QTVS_BOT_X_CLOUD'>Master☘️ {__version__}</a>\n○ Source Code🛖 : <a href='https://t.me/QTVS_BOT_X_CLOUD'>Click here</a>\n○ Channel💥 : href='https://t.me/SAM_DUB_LEZHa\n○ Support Group : @QTVS_BOT_X_CLOUD</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝐂𝐨𝐦𝐞𝐁𝐚𝐜𝐤", callback_data = "back")
                    ]
                ]
            )
        )
    elif data == "back":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
