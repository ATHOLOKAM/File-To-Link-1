# (c) @AbirHasan2005 

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="**𝙷𝙴𝙻𝙻𝙾...⚡**\n\n**𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙵𝙸𝙻𝙴/𝚅𝙸𝙳𝙴𝙾 𝚃𝙾 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙾𝚁 𝙱𝙾𝚃.**\n\n**𝙸 𝙲𝙰𝙽 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙳𝙸𝚁𝙴𝙲𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾**/𝙵𝙸𝙻𝙴𝚂 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙾𝙽𝙻𝙸𝙽𝙴 & 𝙵𝙾𝚁 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶..**\n\n**𝚄𝚂𝙴 /help 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙳𝙴𝚃𝙰𝙸𝙻𝚂...**\n\n**𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾/𝙵𝙸𝙻𝙴 𝚃𝙾 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉....**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 ⚡", url="https://t.me/MWUpdatez"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/OpusTechz")],
                    [InlineKeyboardButton("💸 𝙳𝙾𝙽𝙰𝚃𝙴 💸", url="https://paypal.me/114912Aadil"), InlineKeyboardButton("💠 𝙶𝙸𝚃𝙷𝚄𝙱 💠", url="https://github.com/Aadhi000")],
                    [InlineKeyboardButton("💌 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 💌", url="https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**Your File Link Generated!** 🤓\n\n📂 **File Name:** `{}`\n📦**File Size:** `{}`\n\n📥 **Download Link:** `{}`\n\n🚸 Note: This Is a Permanent Link & Never Expire\n\n© @TheTeleRoid"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Now", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="⚡Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ....\nThis Bot Will Send You Permanent Link\n⚡This Link Can Be Used To Download Or Stream Files[Using External Video Player] Through My Server\n⚡For Streaming Just Copy The Mono Link And Paste It In Your Video Player To Start Streaming\n⚡This bot shAres the Permanent Link to yOu.\n⚡This Bot Is Also Supported in Channels. Add me to Channel as Admin to Make Me Workable!\nFor More Information: @TeleRoidGroup\n\n🔹**WARNING**🚸\n**🔞 Porn Contents Leads You To Permanent Ban From All Bots**", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"), InlineKeyboardButton("😇 Support", url="https://t.me/TeleRoid14")],
                [InlineKeyboardButton("🚸 Powered By ", url="https://t.me/MoviesFlixers_DL"), InlineKeyboardButton("💰 Donate", url="https://t.me/PayForBotZ")],
                [InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/TheTeleRoid")]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**𝚈𝙾𝚄 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴..**\n\n**𝙳𝚄𝙴 𝚃𝙾 𝙾𝚅𝙴𝚁𝙻𝙾𝙰𝙳 𝙾𝙽𝙻𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴𝚁𝚂 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=""" 💕 About My Self

╭──────[𝙵𝙸𝙻𝙴-𝚃𝙾-𝙻𝙸𝙽𝙺 𝙱𝙾𝚃]──────⍟
│
├<b>🤖Bot Name : <a href='https://t.me/teleroid_file2link_bot'>File To Link</a></b>
│
├<b>📢 Channel : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>
│
├<b>👥 Version : <a href='https://t.me/TeleRoid_Renamer_bot'>0.9.2 beta</a></b>
│
├<b>💢 Source : <a href='https://github.com/PredatorHackerzZ/TG-File2Link'>Click Here</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.9</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/PredatorHackerZ'>꧁ ƤℜɆĐ₳₮Øℜ 🇮🇳 ꧂</a></b>
│
├<b>🚸 Powered By : <a href='https://t.me/Moviesflixers_DL'>@HindiWebNetwork</a></b>
│
╰─────────[Thanks 😊]────────⍟""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🚸 Powered By ", url="https://t.me/MoviesFlixers_DL"), InlineKeyboardButton("💰 Donate", url="https://paypal.me/AbhishekKumarIN47")],
                [InlineKeyboardButton("Need Private Bot ❓", url="https://t.me/PayForBotz")]
            ]
        )
    )
