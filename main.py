import logging
from telegram.ext import *
import pdiskuploader

API_KEY = '1967670843:AAFxcZxYw643MS0KFPPHSKkP-n6WMFzjJ08'

#   setting up logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info("Starting bot...")

header = {
    'api_key': pdiskuploader.PDISK_API_KEY,
    'content_src': pdiskuploader.CONTENT_SRC,
    'link_type': pdiskuploader.LINK_TYPE,
    'title': pdiskuploader.FILE_NAME,
}


def start_command(update, context):
    update.message.reply_text('Bot Started....\n'
                              'Follow the these steps to upload files in your pdisk account'
                              '\n1)send /set_api command and give api key'
                              '\n2)send /video_link command and '
                              '\nGive the video direct link or magnet link.'
                              '\n3)send /link_type command and '
                              'give the link type like \'link/magnet\'.'
                              '\n4)send /file_name command and give the '
                              'video file name.'
                              '\n5)send /done command'
                              '\n\nnote: \n\t\t\t\t1) Use all commands like inline commands.\n'
                              '2) If you need to upload no. of files continuously'
                              ' repeat the steps 2 to 5. only')


def set_api_command(update,context):
    message_text = update.effective_message.text
    pdiskuploader.PDISK_API_KEY = message_text.replace('/set_api', '').lower()
    update.message.reply_text('successfully stored your api key. Do the further steps.')

def set_src_command(update, context):
    message_text = update.effective_message.text
    pdiskuploader.CONTENT_SRC = message_text.replace('/video_link ', '')
    update.message.reply_text(f'Hey {update.message.chat.username}, I stored your link.'
                              f'\n\n\nEntered link : {pdiskuploader.CONTENT_SRC}')

def set_link_type_command(update, context):
    message_text = update.effective_message.text
    message_text = message_text.replace('/link_type', '')
    pdiskuploader.LINK_TYPE = message_text
    update.message.reply_text('done bro....')

def set_title_command(update, context):
    message_text = update.effective_message.text
    pdiskuploader.FILE_NAME = message_text.replace('/file_name', '')
    update.message.reply_text('Excellent work...')

def final(update, context):
    pdiskuploader.user(header)
    message_text = pdiskuploader.Result
    message_text = message_text.replace('"msg":', '')
    message_text = message_text.replace(',"status":500', '')
    update.message.reply_text(f'check your {message_text}')

def message_handler(update, context):
    update.message.reply_text('sorry, I can\'t understand what you are saying..'
                              '\nPlease use commands only. Thank you.')

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    Updater = Updater(API_KEY, use_context=True)

    dp = Updater.dispatcher
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('set_api', set_api_command))
    dp.add_handler(CommandHandler('video_link', set_src_command))
    dp.add_handler(CommandHandler('link_type', set_link_type_command))
    dp.add_handler(CommandHandler('file_name', set_title_command))
    dp.add_handler(CommandHandler('done', final))

    dp.add_handler(MessageHandler(Filters.text, message_handler))

    dp.add_error_handler(error)
    Updater.start_polling(1.5)
    Updater.idle()
