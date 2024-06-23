from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
from transformers import AutoModelForCausalLM, AutoTokenizer

TOKEN = '7343783425:AAFkNB18VNWLfPD81EdFEbtYfyuMSR-ZqpU'
USERNAME = '@Python1233bot'
PROXY_URL = "http://167.88.175.18:34567"

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

#Commands
async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐍 SssssHi! I am Viper. What would you like the Furious Five's help with? Sssss... 🐍")

async def help(update:Update, context:ContextTypes.DEFAULT_TYPE):
    str = """🐍 *Viper's Graceful Guidance* 🐍
    SsssssHello, dear friend! I'm Viper, here to assist you with elegance and precision. Let me show you the way:

    🐾 *Commands* 🐾
    - /start: Begin your journey with our bot.
    - /help: Receive guidance on how to use our bot (but you already knew that!).

      🌿 *Tips for Success* 🌿
    - Sssssstay calm and focused; remember that clarity is key to mastering any task.
    - Explore and experiment; every command is a new opportunity to learn.

    If you ever need my assistance again, just type /help, and I'll be right here, ready to guide you with grace.

    *Remember*: True ssssstrength lies in your heart and mind. Sssstay strong, ssssstay kind!

    🐍 With graceful regards,
    Viper

    """
    await update.message.reply_text(str)

#handle reponse
def handle_response(text : str):
    try:
        input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
        bot_response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        bot_response = tokenizer.decode(bot_response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return bot_response
    except Exception as e:
        return 'Sorry I cannot understand you :('
    

async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    chat_type :str = update.message.chat.type
    text :str = update.message.text

    print(f"User ({update.message.chat.id}) in ({chat_type}) : {text}")

    if chat_type == 'group':
        #group chats
        if USERNAME in text:
            new_text :str = text.replace(USERNAME,'').strip()
            response :str = handle_response(new_text)
        else:
            return " "
    else:
        #private chats
        response :str = handle_response(text)
    
    print('Bot: ',response)
    await update.message.reply_text(response)

async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def main():
    print("Starting Bot...")
    proxies = {
        'http': PROXY_URL,
        'https': PROXY_URL,
    }
    
    app = Application.builder().token(TOKEN).proxy(PROXY_URL).get_updates_proxy(PROXY_URL).build()

    #Commands
    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('help',help))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    #Check constantly for new updates/messages
    print("Polling...")
    app.run_polling(poll_interval=3)#set to 3 seconds

if __name__ == "__main__":
    main()






    

