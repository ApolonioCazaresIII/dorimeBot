import discord
import random
import math
from discord.ext import commands


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('Oi Blyat!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def oi(ctx):
    await ctx.send('Oi Blyat!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Bruh you got that Mcdonald\'s connection: {round(client.latency * 1000)}ms')

@client.command()
async def helpme(ctx):
    await ctx.send("Oh, you want help? \n Go here https://github.com/ApolonioCazaresIII/dorimeBot")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Nah fam..."]
    await ctx.send(f'This was your boujee question: {question}\nAnswer: {random.choice(responses)}')

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

@client.command()
async def dmg(ctx, *, input):
    if input == None:
        await ctx.send(f'Nibba enter the values')
    else:
        dmg_roll, dmg_mods, enemy_dt, enemy_dr = input.split()
        result = ((float(dmg_roll) * (1.0 + float(dmg_mods)) - float(enemy_dt)) * (1.0 - float(enemy_dr)))
        mess = round_up(result)
        await ctx.send(f'Result rounded up: {mess}, unrounded: {result}')

@client.command()
async def hit(ctx, *, input):
    if input == None:
        await ctx.send(f'Nibba enter the values')
    enmy_ac, plyr_ammo_ac_pen,ply_skill, roll_skill, ta_ba_pen, \
    plyr_stance, enmy_stance, cond_pen, \
    env_mod, veh_mod, cov_pena, hc_bonus = input.split()
    enAcLeft = int(enmy_ac) + int(plyr_ammo_ac_pen)
    MHC = (int(ply_skill) -int(roll_skill)) + int(ta_ba_pen) + int(plyr_stance) + int(enmy_stance) + \
          int(cond_pen) + int(env_mod) + int(veh_mod) - int(enAcLeft) + int(cov_pena) + int(hc_bonus)
    if MHC >= 0:
        print(f'Result:{MHC}, Hit Successful!')
        await ctx.send(f'Result:{MHC}, Hit successful!')
    else:
        print(f'Result:{MHC}, Hit Failure')
        await ctx.send(f'Result:{MHC}, Hit Failure!')

@client.command()
async def skill(ctx, *, input):
    skill100_roll,plyr_skill, skill_pen = input.split()
    resVal = int(plyr_skill) - int(skill_pen)
    if resVal >= int(skill100_roll):
        print(f'Result: {skill100_roll} <= {resVal}, You pass the skill check!')
        await ctx.send(f'Result: {skill100_roll} <= {resVal}, You pass the skill check!')
    else:
        print(f'Result: {skill100_roll} > {resVal}, You fail the skill check!')
        await ctx.send(f'Result: {skill100_roll} > {resVal}, You fail the skill check!')

@client.command()
async def spec(ctx, *, input):
    skill100_roll,plyr_skill, skill_pen = input.split()
    resVal = int(plyr_skill) - int(skill_pen)
    if resVal >= int(skill100_roll):
        print(f'Result: {skill100_roll} <= {resVal}, You pass the special check!')
        await ctx.send(f'Result: {skill100_roll} <= {resVal}, You pass the special check!')
    else:
        print(f'Result: {skill100_roll} > {resVal}, You fail the special check!')
        await ctx.send(f'Result: {skill100_roll} > {resVal}, You fail the special check!')

@client.command()
async def sacredtext(ctx):
    theText='I tried to stop but I cant stop\n' +\
            'I just cant stop thinking about her\n' +\
            'I dont know, all I remember was she wear the skechers\n' +\
            'The light up ones...\n\n'+\
            'Shawty bad with the Skechers on\n' +\
            'Wana hold your hand make you my girl\n' +\
            'Light up light up sketchers,\n' +\
            'Light up Light up my world\n\n'+\
            'Shawty bad with the Skechers on\n' +\
            'Wana hold your hand make you my girl\n' +\
            'Light up light up sketchers,\n' +\
            'Light up Light up my world\n\n'+\
            'I like your Skechers,\n' +\
            'You like me my Gucci shoes,\n' +\
            'I’ll buy you that purse, only if you show me your boobs\n\n' +\
            'I like your Skecher, You like me too\n' +\
            'Bring your friends, all of us in the pool\n' +\
            'Bad lil bich, all my drip make her drool,\n' +\
            'Brand new whip, come and sit in the coupe\n\n' +\
            'I just wana make you mine,\n' +\
            'Hop inside the ride,\n'+\
            'Nina by my side promise you it’s all be fine\n'
    await ctx.send(theText)


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

client.run('NjM2MDU3ODIzNDI3NjkwNTA4.Xa6GGQ.enRgdcbq-ftfqcYDcyNvqNr4-_U')
