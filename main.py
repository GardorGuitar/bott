import os
import asyncio
from telethon import TelegramClient, events
from keep_alive import keep_alive

api_id = 23343762
api_hash = "6a8208f5da23f681669bd5081933e363"
token = os.environ["TELEGRAM_BOT_TOKEN"]

client = TelegramClient("bot", api_id, api_hash).start(bot_token=token)

source_channels = [-1001596887212, -1002687732807, -1002549051985]
target_channel = -1001234567890  # O'zingizning kanal ID'ingiz

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    try:
        await client.send_message(target_channel, event.message)
    except Exception as e:
        print("Xatolik:", e)

async def main():
    print("📥 Yuklash boshlandi...")
    await client.run_until_disconnected()

keep_alive()
asyncio.run(main())
