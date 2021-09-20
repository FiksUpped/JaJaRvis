from telethon import TelegramClient

api_hash = '00765fc90e559b58fa869ed7fd9bbf1f'
api_id = 1917091

username= "@dejkaa"

client = TelegramClient('session_name', api_id, api_hash)

client.start(password="AquAsonic3346378sb")

client.send_message('me', 'Hello to myself!')