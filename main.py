import asyncio


from bot import MangoManBot


try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


bot = MangoManBot()


loop = asyncio.get_event_loop()
bot.run()
