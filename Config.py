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

        "🔔 **FORCE SUBSCRIBE** [🔔](https://i.imgur.com/Ml6klh1.jpg)\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "**[⚙](https://i.imgur.com/0Atqu6F.jpg) SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me, And I Will Leave The Chat If I am Not An Admin In The Chat",
        
        "**[⚙](https://i.imgur.com/WI5rmk5.jpg) COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "**[👨‍💻](https://i.imgur.com/TaOKIkf.gif) Developed By : @AmineSoukara** \n🇪🇸 Spanish Version @ForzarSuscripcionRobot"
      ]
