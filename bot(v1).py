import discord

settings = {
    'token': '',
    'bot': '',
    'id': ,
    'prefix': '*'
}

pathsave = ""
myear = "mounth-year"
notime = 0 # 0 - for the period; 1 - throughout history

class MyClient(discord.Client):
    bot = discord.Client()
    @bot.event


    async def on_ready(bot):
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

        channel = bot.get_channel()#channel id

        messages = await channel.history(limit=10).flatten()#limit of downloaded photos

        # reversing because discord sends only data first
        messages.reverse()
        if notime == 0:
            for ch in messages:
                tods = ch.created_at
                my = str(tods.month) + "-" + str(tods.year)
                if my == myear:
                    print('check')
                    att = ch.attachments
                    todss = ch.created_at
                    print(att)
                    my = str(todss.month) + "-" + str(todss.year)
                    print(todss.year, todss.month)
                    for attach in ch.attachments:
                        await attach.save(pathsave + my + "-" + str(ch.id) + ".png")

        elif notime == 1:
            for ch in messages:
                tods = ch.created_at
                my = str(tods.month) + "-" + str(tods.year)
                print('check')
                att = ch.attachments
                print(att)
                print(tods.year, tods.month)
                for attach in ch.attachments:
                    await attach.save(pathsave + my + "-" + str(ch.id) + ".png")


client = MyClient()
client.run(settings['token'])
