import discord
import os
from discord.ext import commands
from Cybernator import Paginator

PREFIX = "!"
TOKEN = os.environ.get('BOT_TOKEN')
bot = commands.Bot(command_prefix=PREFIX)
bot.load_extension("jishaku")
bot.remove_command('help')


@bot.event
async def on_ready():
    print("BOT connected")


@bot.command()
async def help(ctx):
    embed1 = discord.Embed(title = "Informational📕", description = 'Информация в компактном варианте🍁')
    embed1.add_field(name = 'userinfo [@member]', value = 'Общая информация о пользователе', inline = False)
    embed1.add_field(name = 'serverinfo', value = 'Общая информация о сервере', inline = False)
    embed1.add_field(name = 'avatar [@member]', value = 'Аватар пользователя', inline = False)

    embed2 = discord.Embed(title = "Moderation🧧", description = 'Регулируйте порядок на вашем сервере🚨')
    embed2.add_field(name = 'kick [@member]', value = 'Исключит пользователя с сервера', inline = False)
    embed2.add_field(name = 'ban [@member]', value = 'Заблокирует пользователя на сервере', inline = False)
    embed2.add_field(name = 'unban [@member]', value = 'Разблокирует пользователя на сервере', inline = False)
    embed2.add_field(name = 'mute [@member]', value = 'Уберет возможность общаться', inline = False)
    embed2.add_field(name = 'unmute [@member]', value = 'Вернёт возможность общаться', inline = False)
    embed2.add_field(name = 'tempmute [@member] [time] [s, m, h, d]', value = 'Уберёт возможность общаться на определенное время', inline = False)
    embed2.add_field(name = 'tempban [@member] [time] [s, m, h, d]', value = 'Заблокирует пользователя на определенное время', inline = False)

    embed3 = discord.Embed(title = "Mass commands📈", description = 'Массовые команды, предназначаные только администраторам💡')
    embed3.add_field(name = 'massroleadd [@role]', value = 'Массово выдаст роль всем пользователям на сервере', inline = False)
    embed3.add_field(name = 'massroleremove [@role]', value = 'Массово заберет роль у всех на сервере', inline = False)
    embed3.add_field(name = 'masslock', value = 'Закроет все чаты на сервере для everyone', inline = False)
    embed3.add_field(name = 'massunlock', value = 'Откроет все чаты на сервере для everyone', inline = False)

    embed4 = discord.Embed(title = "Utils⚙️", description = 'Общие команды которые не подходят под конкретную категорию🎫')
    embed4.add_field(name = 'x [text]', value = 'Написать от имени бота [Полезно для информационных сообщений]', inline = False)
    embed4.add_field(name = 'cl [0/100]', value = 'Очистит чат на указанное количество сообщений [Если не указать очистит 100]', inline = False)
    embed4.add_field(name = 'edit [id] [text]', value = 'Изменит текст сообщения бота на указанный', inline = False)
    embed4.add_field(name = 'ls [@member] [text]', value = 'Напишет личное сообщение пользователю от имени бота', inline = False)
    embed4.add_field(name = 'roles [@role]', value = 'Покажет у скольки людей имеется указанная роль', inline = False)
    embed4.add_field(name = 'event [@role]', value = 'Рандомно разыграет роль среди тех кто нажмет на реакцию и выведет победителя', inline = False)
    embed4.add_field(name = 'qu [text]', value = 'Посторается ответить на ваш вопрос)', inline = False)
    embed4.add_field(name = 'lock', value = 'Закроет и откроет чат при повторном использовании для everyone', inline = False)
    embed4.add_field(name = 'nsfw', value = 'Покажет вам много интересного <18+>', inline = False)

    embed5 = discord.Embed(title = "Activity❤️", description = 'Реакции, показывайте свои эмоции!🌿')
    embed5.add_field(name = 'kiss [@member]', value = 'Поцеловать пользователя', inline = False)
    embed5.add_field(name = 'poke [@member]', value = 'Тыкнуть пользователя', inline = False)
    embed5.add_field(name = 'pat [@member]', value = 'Погладить пользователя', inline = False)
    embed5.add_field(name = 'hug [@member]', value = 'Обнять пользователя', inline = False)
    embed5.add_field(name = 'tic [@member]', value = 'Пощекотать пользователя', inline = False)

    embed6 = discord.Embed(title = "Embed🎉", description = 'Приглашения на мероприятия✨')
    embed6.add_field(name = 'mafia', value = 'Выведет приглашение на мафию', inline = False)
    embed6.add_field(name = 'cinema', value = 'Выведет приглашение на посмотр фильма', inline = False)
    embed6.add_field(name = 'voice', value = 'Выведет приглашение в войс от вашего лица', inline = False)

    embed7 = discord.Embed(title = "Music🎙", description = 'Тестовый раздел, скоро будет готово!☕️')
    embed7.add_field(name = 'join', value = 'Подключится к голосовому каналу', inline = False)
    embed7.add_field(name = 'leave', value = 'Отлючится от голосового канала', inline = False)
    embed7.add_field(name = 'play [text]', value = 'Включит выбранную песню', inline = False)
    embed7.add_field(name = 'now', value = 'Выведет песню которая играет в данный момент', inline = False)
    embed7.add_field(name = 'queue', value = 'Покажет песни в очереди', inline = False)
    embed7.add_field(name = 'remove [number]', value = 'Уберет указанную песню из очереди', inline = False)
    embed7.add_field(name = 'shuffle', value = 'Включит или отключит режим случайного воспроизведения', inline = False)
    embed7.add_field(name = 'loop', value = 'Включит повторение очереди или при повторном использовании последней песни', inline = False)
    embed7.add_field(name = 'volume [0/100]', value = 'Поставит указанную громкость', inline = False)
    embed7.add_field(name = 'pause', value = 'Поставит песню на паузу', inline = False)
    embed7.add_field(name = 'resume', value = 'Продолжит воспроизведение', inline = False)
    embed7.add_field(name = 'summon', value = 'Бот подключится к вашему голосому каналу. Используется только с правами администратора.', inline = False)
    embed7.add_field(name = 'skip', value = 'Пропустит включенную песню из очереди', inline = False)
    embed7.add_field(name = 'stop', value = 'Остановит проигрывание и очистит очередь', inline = False)

    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]
    message = await ctx.send(embed=embed1)
    page = Paginator(bot, message, only=ctx.author, timeout = 120, use_more=False,  color = 0xFFEAE7, embeds=embeds)
    await page.start()

bot.run(TOKEN)