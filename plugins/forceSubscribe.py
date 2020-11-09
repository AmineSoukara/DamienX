import time
import logging
from Config import Config
from pyrogram import Client, filters
from sql_helpers import forceSubscribe_sql as sql
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

logging.basicConfig(level=logging.INFO)

static_data_filter = filters.create(lambda _, __, query: query.data == "onUnMuteRequest")
@Client.on_callback_query(static_data_filter)
def _onUnMuteRequest(client, cb):
  user_id = cb.from_user.id
  chat_id = cb.message.chat.id
  chat_db = sql.fs_settings(chat_id)
  if chat_db:
    channel = chat_db.channel
    chat_member = client.get_chat_member(chat_id, user_id)
    if chat_member.restricted_by:
      if chat_member.restricted_by.id == (client.get_me()).id:
          try:
            client.get_chat_member(channel, user_id)
            client.unban_chat_member(chat_id, user_id)
            if cb.message.reply_to_message.from_user.id == user_id:
              cb.message.delete()
          except UserNotParticipant:
            client.answer_callback_query(cb.id, text="❗ Join The Mentioned 'Channel' And Press The 'UnMute Me' Button Again.", show_alert=True)
      else:
        client.answer_callback_query(cb.id, text="❗ You Are Muted By Admins For Other Reasons.", show_alert=True)
    else:
      if not client.get_chat_member(chat_id, (client.get_me()).id).status == 'administrator':
        client.send_message(chat_id, f"❗ **{cb.from_user.mention} Is Trying To UnMute Himself But I Can't Unmute Him Because I Am Not An Admin In This Chat Add Me As Admin Again.**\n#Leaving This Chat ...")
        client.leave_chat(chat_id)
      else:
        client.answer_callback_query(cb.id, text="❗ Warning: Don't Click The Button If You Can Speak Freely.", show_alert=True)



@Client.on_message(filters.text & ~filters.private & ~filters.edited, group=1)
def _check_member(client, message):
  chat_id = message.chat.id
  chat_db = sql.fs_settings(chat_id)
  if chat_db:
    user_id = message.from_user.id
    if not client.get_chat_member(chat_id, user_id).status in ("administrator", "creator") and not user_id in Config.SUDO_USERS:
      channel = chat_db.channel
      try:
        client.get_chat_member(channel, user_id)
      except UserNotParticipant:
        try:
          sent_message = message.reply_text(
              "{}, You Are **Not Subscribed** To My [Channel](https://t.me/{}) Yet. Please Join 👉 @{} And **Press The Button Below** 👇 To Unmute Yourself.".format(message.from_user.mention, channel, channel),
              disable_web_page_preview=True,
              reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton("🔕 UnMute Me", callback_data="onUnMuteRequest"),
                    InlineKeyboardButton("🔔 Bot Channel", url="https://t.me/DamienSoukara")]]
              )
          )
          client.restrict_chat_member(chat_id, user_id, ChatPermissions(can_send_messages=False))
        except ChatAdminRequired:
          sent_message.edit("❗ **I Am Not An Admin Here.**\nMake Me Admin With Ban User Permission And Add Me Again.\n#Leaving This Chat ...")
          client.leave_chat(chat_id)
      except ChatAdminRequired:
        client.send_message(chat_id, text=f"❗ **I Am Not An Admin In @{channel}**\nMake Me Admin In The Channel And Add Me Again.\n#Leaving This Chat ...")
        client.leave_chat(chat_id)


@Client.on_message(filters.command(["forcesubscribe", "fsub"]) & ~filters.private)
def config(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status is "creator" or user.user.id in Config.SUDO_USERS:
    chat_id = message.chat.id
    if len(message.command) > 1:
      input_str = message.command[1]
      input_str = input_str.replace("@", "")
      if input_str.lower() in ("off", "no", "disable"):
        sql.disapprove(chat_id)
        message.reply_text("❌ **Force Subscribe is Disabled Successfully.**")
      elif input_str.lower() in ('clear'):
        sent_message = message.reply_text('**Unmuting All Members Who Are Muted By Me ...**')
        try:
          for chat_member in client.get_chat_members(message.chat.id, filter="restricted"):
            if chat_member.restricted_by.id == (client.get_me()).id:
                client.unban_chat_member(chat_id, chat_member.user.id)
                time.sleep(1)
          sent_message.edit('✅ **UnMuted All Members Who Are Muted By Me.**')
        except ChatAdminRequired:
          sent_message.edit('❗ **I Am Not An Admin In This Chat.**\nI Can\'t Unmute Members Because I Am Not An Admin In This Chat Make Me Admin With Ban User Permission.')
      else:
        try:
          client.get_chat_member(input_str, "me")
          sql.add_channel(chat_id, input_str)
          message.reply_text(f"✅ **Force Subscribe is Enabled**\nForce Subscribe Is Enabled, All The Group Members Have To Subscribe This [Channel](https://t.me/{input_str}) In Order To Send Messages In This Group.", disable_web_page_preview=True)
        except UserNotParticipant:
          message.reply_text(f"❗ **Not An Admin In The Channel**\nI Am Not An Admin In The [Channel](https://t.me/{input_str}). Add Me As A Admin In Order To Enable ForceSubscribe.", disable_web_page_preview=True)
        except (UsernameNotOccupied, PeerIdInvalid):
          message.reply_text(f"❗ **Invalid Channel Username.**")
        except Exception as err:
          message.reply_text(f"❗ **ERROR:** ```{err}```")
    else:
      if sql.fs_settings(chat_id):
        message.reply_text(f"✅ **Force Subscribe Is Enabled In This Chat.**\nFor This [Channel](https://t.me/{sql.fs_settings(chat_id).channel})", disable_web_page_preview=True)
      else:
        message.reply_text("❌ **Force Subscribe Is Disabled In This Chat.**")
  else:
      message.reply_text("❗ **Group Creator Required**\n__You have To Be The Group Creator To Do That.")
