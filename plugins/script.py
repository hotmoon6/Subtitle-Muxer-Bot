from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} What is your Truely Desire?

I'm Subtitle Muxer Bot

I can Mux subtitle to any video

Use Help to Know about me

Made With 💕 By Lucifer👿
"""
    HELP_TEXT = """
Recommended
➠ Use Hardmux If You Have More Time

Recommended
➠ Use Softmux To add Subtitle Fastly in It

Softmux
➠ Send /softmux to add Subtitle Softly in it

HardMux
➠ Send /hardmux to add Subtitle hardly in it 

Made With 💕 By Lucifer👿
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Sub-Muxer\n
 **👲 Developer :** Lucifer\n
 **👥 Channel :** [SilverCity](https://t.me/submuxer_robot)\n
 **❄️ Credits :** Everyone in the Hell\n
 **🍴 Source :** I am the Devil of my word👿\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('💬 1.Send srt', url='https://telegram.me/submuxer_robot'),
        InlineKeyboardButton('🎞️ 2.Send file', url='https://telegram.me/submuxer_robot')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
