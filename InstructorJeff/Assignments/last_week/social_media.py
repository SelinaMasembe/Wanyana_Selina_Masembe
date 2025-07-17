from typing import Final
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, Application

TOKEN: Final ="whatsapp"
BOT_USERNAME: Final = "recess_year2_bot"

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Recess Year Bot! I am a social media assistant."
    )
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I can help you create social media posts."
    )


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "This is a custom command."
    )
    
    
#responses
def handle_response(text:str) -> str:
    if "hello" in text.lower():
        return "Hello! How can I assist you today?"
    
    if "how are you" in text.lower():
        return "I'm all good!"
    
    if "I love python" in text.lower():
        return "Remember to subscribe. "
    
    return "I'm not sure how to respond to that. Can you please rephrase?"



#handling user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type   #whether its in a group chat or private chat
    text: str = update.message.text
    
    print(f'User ({update.effective_user.id}) in {message_type} sent: "{text}"')
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response = handle_response(new_text)
            await update.message.reply_text(response)
        else:
            return

    else:
        response:str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)
    
    
#logging errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    
if __name__ == "__main__":
    print("Starting the Recess Year Bot...")
    
    
    app = Application.builder().token(TOKEN).build()
    
    #commands
    app.add_handler(CommandHandler("start", start_command)) #take care of commands
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    
    
    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))  #handle text messages
    
    #errors
    app.add_error_handler(error)  #handle errors
    
    #checking for ipdates or new  user messages
    print("Bot is polling for updates...")
    app.run_polling(poll_interval =5)  #start the bot and check for updates every 5s
    
    
    
    
    
