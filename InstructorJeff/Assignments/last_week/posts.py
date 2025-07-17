from typing import Final
import openai
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Set your keys
TELEGRAM_TOKEN: Final = '8045446555:AAEIPMaH3wqz-DtvF8fdGIrNBdaCBL0eggQ'
OPENAI_API_KEY: Final = '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'
BOT_USERNAME: Final = "@social_media_year2_bot"
openai.api_key = OPENAI_API_KEY


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm your AI Social Media Post Assistant.\n\n"
        "Type /post to create a post or /help for more info."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Help Menu*\n\n"
        "/start - Welcome message\n"
        "/post - Start creating a social media post\n"
        "/help - Show this help message\n\n"
        "Just type your topic after /post or send a message anytime!"
    )

# /post command (just prompts user)
async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "What do you want your post to be about?\nExample: *Promote my new mobile app*",
        parse_mode="Markdown"
    )

# Text handler for generating posts
async def generate_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Received a message to generate post...")  # Debug line

    user_input = update.message.text
    print(f"User input: {user_input}")  # Debug line

    try:
        prompt = (
            f"Generate a social media post with the following info:\n"
            f"Topic: {user_input}\n"
            f"Tone: friendly and engaging\n"
            f"Platform: Instagram\n"
            f"Include: relevant hashtags"
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        post = response.choices[0].message.content.strip()
        print("Generated post:", post)  # Debug line
        await update.message.reply_text(post)

    except Exception as e:
        print("Error during OpenAI call:", e)  # Debug error
        await update.message.reply_text("Sorry, I had trouble generating your post.")


# Run the bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_post))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
