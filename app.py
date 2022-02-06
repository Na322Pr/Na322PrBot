import asyncio

from utils.misc import set_data
from utils.set_bot_commands import set_default_commands

from utils.misc.sending_out_messages import send_out_message


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


async def periodic(sleep_for):
    time_counter = 0
    while True:
        time_counter += 1
        await asyncio.sleep(sleep_for)
        await send_out_message(time_counter)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    loop = asyncio.get_event_loop()
    loop.create_task(periodic(3600))
    executor.start_polling(dp, on_startup=on_startup)
