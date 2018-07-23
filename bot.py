import discord
from discord.ext import commands
import asyncio
from func import showCreature
from priv import TOKEN
bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    
@bot.command(pass_context=True, name='creature')
async def creature(context, *args):

    res = showCreature(' '.join(args))
    print(res)
    if (res == False):
        await bot.send_message(context.message.channel, 'Je ne trouve pas ' + ' '.join(args))
    else:
        embed0 = discord.Embed(title=res['title'], color=0x00ff00)
        embed1 = discord.Embed(title="Sort", color=0x00ff00)
        embed2 = discord.Embed(title="Sort", color=0x00ff00)
        embed3 = discord.Embed(title="Sort", color=0x00ff00)
        
        embed0.add_field(name="__**Informations**__", value=res['head'], inline=True)
        embed0.add_field(name="__**Caractéristiques (max evolve)**__", value=res['stats'], inline=True)
        embed0.add_field(name="__**Lien vers la fiche**__", value=res['provider'], inline=True)
        
        embed0.set_thumbnail(url=res['image'])
        embed0.set_footer(text="Données fournies par mmeg-db.com")

        await bot.send_message(context.message.channel, embed=embed0)
        
        embed1.add_field(name = '__**Sort 1**__', value=res['spell1'], inline=False)      
        embed1.set_footer(text="Données fournies par mmeg-db.com")      
        await bot.send_message(context.message.channel, embed=embed1)

        embed2.add_field(name="__**Sort 2**__", value=res['spell2'], inline=False)      
        embed2.set_footer(text="Données fournies par mmeg-db.com")      
        await bot.send_message(context.message.channel, embed=embed2)

        embed3.add_field(name="__**Sort 3**__", value=res['spell3'], inline=False)      
        embed3.set_footer(text="Données fournies par mmeg-db.com")      
        await bot.send_message(context.message.channel, embed=embed3)

bot.run(TOKEN)



