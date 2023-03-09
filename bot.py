from aiogram import Bot, Dispatcher, executor, types
import logging

import openai

TELEGRAM_BOT_TOKEN = '6121401802:AAGzabdF-WtUVuchmh7w2Dg_mdX8DdldVdQ'

OPENAI_API_KEY = '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'

openai.api_key = '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'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


async def ai(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system",
                    "content": ''},
                {'role': 'user', 'content': prompt}
            ]
        )

        return completion.choices[0].message.content
    except:
        return None


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Привет, я бот от Ивана. Чем могу помочь?")


@dp.message_handler()
async def echo(message: types.Message):
    answer = await ai(message.text)
    if answer != None:
        await message.reply(answer)
    else:
        await message.reply('Попробуйте ещё раз!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
