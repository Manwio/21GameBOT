import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '')

ertekek = [
        ('A', 10), ('K', 10), ('Q', 10), ('J', 10), ('10', 10),
        ('9', 9), ('8', 8), ('7', 7), ('6', 6), ('5', 5),
        ('4', 4), ('3', 3), ('2', 2), ('1', 1)
        ]

szinek = [':trident:', ':fleur_de_lis:', ':diamond_shape_with_a_dot_inside:', ':high_brightness:']
szamok = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

LAPOK_OSSZEGE = []

BOT_SZAMAI = []

@client.event
async def on_ready():
    print('Bot is ready')

#COMMANDS

@client.command()
async def helpecske(ctx):
    await ctx.send(f"""
    **Szia!**
```fix
Én egy 21-es kártyajátékot imitáló BOT vagyok.
Különböző parancsok segítségével tudsz játszani velem :D```

```json
"Parancsok: helpecske | hello | game" ```

```ini
[Kicsit még nem működök jól, mert akkor kérek lapot, amikor te is :(
De idővel ügyesebb leszek.]```
    """)

@client.command()
async def hello(ctx):
    await ctx.send(f"""
```diff
- Minek köszöngetel??!!?!?!
- AMÚGY SZEVASSZ MÓNIKA```
    """)

#GAME
#########################################
@client.command()
async def game(ctx):
    await ctx.send(f"""
    **Kezdjük a játékot!**
    ```bash
    "Add ki a 'acca' parancsot a lap kéréséhez"```
    """)


def betus(s):
    lap_szamok = "123456789"

    if s == 'A' or s == 'K' or s == 'Q' or s == 'J' or s == '10':
        return 10
    if s in lap_szamok:
        return int(s)
    

@client.command()
async def acca(ctx):
    lap = random.choice(szamok)
    lap_bot = random.choice(szamok)

    await ctx.send(f"""A te lapod:{random.choice(szinek)} {lap}

Az én lapom: {random.choice(szinek)} {lap_bot}
```
Szeretnél még egy lapot hozzá?
Igen, kérek még egy lapot --> 'acca'
Nem, megállok --> 'megall' ```
    """)

    lap = int(betus(lap))
    lap_bot = int(betus(lap_bot))

    LAPOK_OSSZEGE.append(lap)
    BOT_SZAMAI.append(lap_bot)


def ki_nyert(en, bot):
    if en > bot:
        return (f'**Te nyertél!** :raised_hands: :partying_face:')
    if en < bot:
        return '**Én nyertem!** :partying_face: :space_invader:'
    else:
        return '**DÖNTETLEN** :angry: :exploding_head:'

@client.command()
async def megall(ctx):
    await ctx.send(f"""Neked összesen {sum(LAPOK_OSSZEGE)} van
Nekem pedig {sum(BOT_SZAMAI)}

{ki_nyert(sum(LAPOK_OSSZEGE), sum(BOT_SZAMAI))}

```
Szeretnél még játszani?
Ha igen add ki újra a 'game' parancsot```
    """)

    LAPOK_OSSZEGE.clear()
    BOT_SZAMAI.clear()


client.run('NzYyNzM0OTk2OTg4NDkzODY0.X3teUg.9GkLatlj_8aTGs-5J2ClskdWvDA')