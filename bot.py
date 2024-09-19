from interactions import Client, Intents, listen
from interactions import ChannelType, GuildText, OptionType, SlashContext, slash_command, slash_option, Embed
from test import get_transaction_info
import asyncio

bot = Client(intents=Intents.DEFAULT)

@listen()
async def on_ready():
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


async def crypto_t(ctx: SlashContext, txid: str):
    api_key = "d86e71c2b35a4e9a8e571ebf37151517"  # Reemplaza con tu API key
    while True:
        date_time, status, confirmations = await get_transaction_info(txid, api_key)

        # Configura el embed según el status
        if status == 'Pending':
            color = 0xffa500  # Naranja
            thumbnail_url = "https://i.postimg.cc/nzc9dDb6/pending-512x504.png"
            description = f"Your transaction is in process, this may take a few minutes. \nConfirmactions: {confirmations}"
        else:
            color = 0x00ff00  # Verde
            thumbnail_url = "https://i.postimg.cc/Px3p05dN/check-mark-button-512x512.png"
            description = f"Congratulations, your transaction has arrived. \nConfirmations: {confirmations}"

        embed = Embed(
            title=f"Status: {status}",
            description=description,
            color=color  # Color del embed según el status
        )
        embed.set_footer(text=f"Transaction Date: {date_time}")
        embed.set_thumbnail(url=thumbnail_url)  # Thumbnail según el status
        await ctx.send(embeds=[embed])
        if status == 'Confirmed':
            break
        await asyncio.sleep(129)  # Espera 120 segundos antes de volver a buscar el status de la transacción

@slash_command(name="track-a-transaction", description="Find your hash", scopes=[1184329568216154123])
@slash_option(
    name="txid",
    description="Enter a hash",
    opt_type=OptionType.STRING,
    required=True
)
async def my_command_function(ctx: SlashContext, txid: str):
    await ctx.send(":mag: SEARCHING....")
    await crypto_t(ctx, txid)


bot.start("token")

