import logging

from bot.data.config import ADMINS

from loader import dp



async def message2admins(text):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text)
        except Exception as err:
            logging.exception(err)
