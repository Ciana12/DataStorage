import random
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
def run():

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix = "-", intents = intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
    async def on_command_error(ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("handled error globally")


    # @add.error
    # async def add_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("handled error locally")



    @bot.command(
        aliases = ['p'],

        # help = 'this is help',
        # description = 'this is description',
        # # brief = 'this is brief',

        enable = True,
        hidden = False
    )
    async def ping(ctx):
        """ ping pong  """
        await ctx.send("pong")

    

    @bot.group()
    async def math(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")


    @math.command()
    async def add(ctx, one : int, two : int):
        await ctx.send(one + two)


    @math.command()
    async def substract(ctx, one : int, two : int):
        await ctx.send(one - two)


    @math.command()
    async def divide(ctx, one: int , two: int):
        await ctx.send(one / two)
    

    @math.command()
    async def multiple(ctx, one: int, two: int):
        await ctx.send(one * two)

    


        


    bot.run(settings.DISCORD_API_SECRET, root_logger = True)

if __name__ == "__main__":
    run()