import random
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Логирование для отладки
logging.basicConfig(level=logging.INFO)

# Токен вашего бота
API_TOKEN = "8508442203:AAHv9KwHsW67V_I85YyrjuSFqLj4ihE0v7c"

# Создаем объект бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Функция для генерации мира
def generate_world(world_type: str):
    worlds = {
        "фэнтези": {
            "map": "Великое королевство с лесами, горами и таинственными подземельями.",
            "characters": ["Эльф", "Гном", "Человек", "Дворф"],
            "quests": [
                "Найти древний артефакт",
                "Защитить деревню от орков",
                "Исследовать заброшенные руины",
            ],
            # ТУТ ВСТАВЬ СВОИ ССЫЛКИ НА КАРТИНКИ
            "images": [
                "https://picsum.photos/seed/fantasy1/800/600",
                "https://picsum.photos/seed/fantasy2/800/600",
                "https://avatars.mds.yandex.net/i?id=8e2aa6ae8233af2894169ac4a20b37dbb29ddccd-10853576-images-thumbs&n=13",
            ],
        },
        "постапокалипсис": {
            "map": "Разрушенная пустошь, наполненная радиоактивными зонами и бандами выживших.",
            "characters": ["Выживший", "Мутант", "Рейдер", "Торговец"],
            "quests": [
                "Найти воду для поселения",
                "Собрать ресурсы для оружия",
                "Отправиться в безопасную зону",
            ],
            "images": [
                "https://avatars.mds.yandex.net/i?id=768b5d4fe94736f67e26a1c34105f13ab038a59e-4937330-images-thumbs&n=13",
                "https://avatars.mds.yandex.net/i?id=9dc319b87f3ecf407a452242b513c839a940b4ac-5313038-images-thumbs&n=13",
            ],
        },
        "фантастика": {
            "map": "Мега-город с высокими небоскрёбами, космическими станциями и чуждыми расами.",
            "characters": ["Астронавт", "Индивидуальный агент", "Киборг", "Робот", "Человек"],
            "quests": [
                "Спасти космический корабль",
                "Пробраться в корпорацию противника",
                "Исследовать новую планету",
            ],
            "images": [
                "https://avatars.mds.yandex.net/i?id=5a4820e46b98746af05ace825dea36abc0484aa5-2454879-images-thumbs&n=13",
                "https://avatars.mds.yandex.net/i?id=702d257dbf2df5cdce5a76509a6d637a8600097c-5440356-images-thumbs&n=13",
            ],
        },
        "средневековье": {
            "map": "Великое королевство, огромных размеров, полное разнообразных существ и загадок.",
            "characters": ["Маг", "Рыцарь", "Король", "Принц", "Крестьянин"],
            "quests": [
                "Основать свой бизнес",
                "Защитить королевство от войны",
                "Свергнуть власть",
            ],
            "images": [
                "https://avatars.mds.yandex.net/i?id=c33a6486c056c9ef6701436e692e1740c5767f04-3380069-images-thumbs&n=13",
                "https://i.pinimg.com/474x/33/4b/3b/334b3bcd801937c02964a9b6ff6e3305.jpg",
            ],
        },
    }

    world = worlds.get(world_type)
    if world:
        map_ = world["map"]
        character = random.choice(world["characters"])
        quest = random.choice(world["quests"])
        image_url = random.choice(world["images"])
        text = f"Мир: {map_}\nПерсонаж: {character}\nКвест: {quest}"
        return text, image_url
    else:
        return None, None


# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе создать уникальный мир для ролевой игры.\n"
        "Выбери тип мира: фэнтези, постапокалипсис, фантастика, средневековье.\n\n"
        "Пример: /generate фэнтези"
    )


# Команда /generate
@dp.message(Command("generate"))
async def generate(message: types.Message):
    # Получаем текст после /generate
    parts = message.text.strip().lower().split(" ", 1)
    if len(parts) == 1:
        await message.answer(
            "Ты не указал тип мира.\n\n"
            "Пример: /generate фэнтези"
        )
        return

    user_input = parts[1]

    valid_worlds = ["фэнтези", "постапокалипсис", "фантастика", "средневековье"]

    if user_input in valid_worlds:
        text, image_url = generate_world(user_input)
        if text and image_url:
            # Отправляем картинку с описанием в подписи
            await message.answer_photo(photo=image_url, caption=text)
        else:
            await message.answer("Произошла ошибка при генерации мира.")
    else:
        await message.answer(
            "Неверный тип мира.\n"
            "Выбери один из: фэнтези, постапокалипсис, фантастика, средневековье.\n\n"
            "Пример: /generate фэнтези"
        )


# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
