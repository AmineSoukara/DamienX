<p align="center">
    <a href="https://github.com/AmineSoukara/Damien-X/alpha">
        <img src="resources/logo.png" alt="Damien-X">
    </a>
    <br>
    <b>Pluggable Telegram UserBot</b>
    <br>
    <a href="https://github.com/AmineSoukara/Damien-X#inspiration-">Inspiration</a>
    &nbsp•&nbsp
    <a href="https://github.com/AmineSoukara/Damien-X#features-">Features</a>
    &nbsp•&nbsp
    <a href="https://github.com/AmineSoukara/Damien-X#example-plugin-">Example</a>
    &nbsp•&nbsp
    <a href="https://github.com/AmineSoukara/Damien-X#requirements-">Requirements</a>
    &nbsp•&nbsp
    <a href="https://github.com/AmineSoukara/Damien-X#project-credits-">Project Credits</a>
    &nbsp•&nbsp
    <a href="https://github.com/AmineSoukara/Damien-X#copyright--license-">Copyright & License</a>
</p>

# 🔥 Damien-X :

[![Build Status](https://travis-ci.com/UsergeTeam/Userge.svg?branch=dev)](https://travis-ci.com/UsergeTeam/Userge) ![Python Version](https://img.shields.io/badge/python-3.8-lightgrey) ![Release](https://img.shields.io/github/v/release/UsergeTeam/Userge) ![Stars](https://img.shields.io/github/stars/UsergeTeam/Userge) ![Forks](https://img.shields.io/github/forks/UsergeTeam/Userge) ![Issues Open](https://img.shields.io/github/issues/UsergeTeam/Userge) ![Issues Closed](https://img.shields.io/github/issues-closed/UsergeTeam/Userge) ![PR Open](https://img.shields.io/github/issues-pr/UsergeTeam/Userge) ![PR Closed](https://img.shields.io/github/issues-pr-closed/UsergeTeam/Userge) ![Contributors](https://img.shields.io/github/contributors/UsergeTeam/Userge) ![Repo Size](https://img.shields.io/github/repo-size/UsergeTeam/Userge) ![License](https://img.shields.io/github/license/UsergeTeam/Userge) ![Commit Activity](https://img.shields.io/github/commit-activity/m/UsergeTeam/Userge) [![Plugins Repo!](https://img.shields.io/badge/Plugins%20Repo-!-orange)](https://github.com/UsergeTeam/Userge-Plugins) [![Join Channel!](https://img.shields.io/badge/Join%20Channel-@DamienSouka-purple)](https://t.me/DamienSoukara) [![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/UsergeTeam/Userge/?ref=repository-badge)

> **Damien-X** is a Powerful , _Pluggable_ Telegram UserBot written in _Python_ using [Pyrogram](https://github.com/pyrogram/pyrogram).

## ℹ Read More :
<details>
  <summary><b>Details & Guides</b></summary>

### For Any Query Or Want To Know How it Works Join Group And Channel 

<a href="https://t.me/DamienSoukara"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/DamienHelp"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>


## Inspiration 😇

> This project is inspired by the following projects :)

* [tg_userbot](https://github.com/watzon/tg_userbot) ( heavily ) 🤗
* [PyroGramUserBot](https://github.com/SpEcHiDe/PyroGramUserBot)
* [Telegram-Paperplane](https://github.com/RaphielGang/Telegram-Paperplane)
* [UniBorg](https://github.com/SpEcHiDe/UniBorg)
* [Userge](https://github.com/UsergeTeam/Userge)
* [Userge-X](https://github.com/code-rgb/USERGE-X)
> Special Thanks to all of you !!!.

## Features 😍

* Powerful and Very Useful **built-in** Plugins
  * gdrive [ upload / download / etc ] ( Team Drives Supported! ) 🤥
  * zip / tar / unzip / untar / unrar
  * telegram upload / download
  * pmpermit / afk
  * notes / filters
  * split / combine
  * gadmin
  * plugin manager
  * etc...
* Channel & Group log support
* Database support
* Build-in help support
* Easy to Setup & Use
* Easy to add / port Plugins
* Easy to write modules with the modified client

## Example Plugin 🤨

```python
from userge import userge, Message, filters

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object

# add command handler
@userge.on_cmd("test", about="help text to this command")
async def test_cmd(message: Message):
   LOG.info("starting test command...")  # log to console
   # some other stuff
   await message.edit("testing...", del_in=5)  # this will be automatically deleted after 5 sec
   # some other stuff
   await CHANNEL.log("testing completed!")  # log to channel

# add filters handler
@userge.on_filters(filters.me & filters.private)  # filter my private messages
async def test_filter(message: Message):
   LOG.info("starting filter command...")
   # some other stuff
   await message.reply(f"you typed - {message.text}", del_in=5)
   # some other stuff
   await CHANNEL.log("filter executed!")
```

## Requirements 🥴

* Python 3.8 or Higher 👻
* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)

## Damien-X MODES 🕹

* **USER** mode `(using user account)`
* **BOT** mode `(using bot account)`
* **DUAL** mode `(using both user and bot account)`

  > further **read** [config.env.sample](https://github.com/AmineSoukara/Damien-X/blob/alpha/config.env.sample)

# How To Deploy 👷

### **[HEROKU](https://www.heroku.com/) Method** 🚀

  > [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AmineSoukara/Damien-X/tree/alpha)

  > Fill `API_ID`, `API_HASH`, `DATABASE_URL` and `LOG_CHANNEL_ID` (**required**)

  > Choose your [**MODE**](https://github.com/AmineSoukara/Damien-X#userge-modes-)

  > Then fill other **non-required** vars as relevent to your **MODE**

  > Finally **hit deploy** button

  > [**NOTE**] : your can fill other vars as your need and they are optional. (settings -> reveal config vars)

## String Session :
**VAR :** `HU_STRING_SESSION`

### HEROKU :
- [open your app](https://dashboard.heroku.com/apps/) then go to **more** -> **run console** and paste the command below and click **run**.
  > command: `bash genStr`
### REPL :
- [**Generate on REPL**](https://stringsessiongen.leorio.repl.run/)

## **Docker Method** 🐳 

    - [**See Detailed Guide**](resources/radmeDocker.md)
* **Other Method** 🔧

  ```bash
  # clone the repo
  git clone https://github.com/AmineSoukara/Damien-X.git
  cd Userge

  # create virtualenv
  virtualenv -p /usr/bin/python3 venv
  . ./venv/bin/activate

  # install requirements
  pip install -r requirements.txt

  # Create config.env as given config.env.sample and fill that
  cp config.env.sample config.env

  # get string session and add it to config.env
  bash genStr

  # finally run the Userbot ;)
  bash run
  ```

* **[More Detailed Guide](https://docs.google.com/document/d/15uoiOn2NkN518MMkx9h5UaMEWMp8aNZqJocXvS0uI6E)** 📝

### Project Credits 💆‍♂️

* [Specially to these projects](https://github.com/UsergeTeam/Userge#inspiration-) 🥰
* [@uaudIth](https://t.me/uaudIth)
* [@K_E_N_W_A_Y](https://t.me/K_E_N_W_A_Y)
* [@nawwasl](https://t.me/nawwasl)
* [@TharukaN97](https://t.me/TharukaN97)
* [@Supun97](https://t.me/Supun97)
* [@gotstc](https://t.me/gotstc)

### Copyright & License 👮

* Copyright (C) 2020 by [UsergeTeam](https://github.com/UsergeTeam) ❤️️
* Licensed under the terms of the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/UsergeTeam/Userge/blob/master/LICENSE)
</details>
