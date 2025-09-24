import asyncio
from telethon import TelegramClient, events

from task2.config import settings

seen_texts = set()

async def main():
    client = TelegramClient('session_name', settings.API_ID, settings.API_HASH)

    await client.start(
        phone=settings.PHONE,
        password=lambda: input('Введите 2FA пароль (если есть): '),
        code_callback=lambda: input('Введите код из Telegram: ')
    )

    print("Авторизация успешна. Ожидание сообщений...")

    target_chat = int(settings.TARGET_CHAT) if settings.TARGET_CHAT.lstrip("-").isdigit() else settings.TARGET_CHAT

    @client.on(events.NewMessage(chats=target_chat))
    async def handler(event):
        text = event.message.message
        if not text:
            return

        normalized = text.strip().lower()

        if normalized not in seen_texts:
            seen_texts.add(normalized)
            print(f"\nНовое уникальное сообщение от {event.sender_id}:")
            print(f"   {text}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nСкрипт остановлен пользователем.")
    except Exception as e:
        print(f"\nОшибка: {e}")