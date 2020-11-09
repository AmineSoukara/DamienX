#rename to Config.py this congfig is for force subscribe module
import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "").split()))
    SUDO_USERS.append(1084619043)
    SUDO_USERS = set(SUDO_USERS)
  else:
    BOT_TOKEN = "1394726720:AAFyQlsDHeJgk9isPA2iMl7tJpjrZbzeh44"
    DATABASE_URL = "postgres://vnodgsrfjaegig:2b4335d8b16f1195fe8bf7b92dc7477b2d3bb74af6d4442c20b0816829e2e1a7@ec2-3-208-224-152.compute-1.amazonaws.com:5432/d7fc6v00kh0dqr"
    APP_ID = "1358970"
    API_HASH = "57aff1848504fcde424d181d5cfee983"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1084619043)
    SUDO_USERS = list(set(SUDO_USERS))
    
    
    
class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @ **"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /forcehelp__"
