import telebot
import openai
from config import OpenAI_KEY, BOT_API

chatstr = ''


def chatbot(prompt):
    global chatstr
    openai.api_key = OpenAI_KEY
    chatstr += f"Swehul: {prompt}\n SAMAEL: "
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print(response)
        chatstr += f"{response['choices'][0]['message']['content']}"
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't process your request at the moment."




bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello There! Welcome To Swehul Tech")

@bot.message_handler()
def chat(message):
    try:
        reply = chatbot(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        print(e)
        bot.reply_to(message, str(e))
    print(message.text)

print("Bot Started")
bot.polling()
