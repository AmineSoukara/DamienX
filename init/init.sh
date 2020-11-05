#!/bin/bash
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT

initUserge() {
    printLogo
    assertPrerequisites
    sendMessage "💬 Initializing DAMIEN-X ..."
    assertEnvironment
    editLastMessage "✅ Starting DAMIEN-X ..."
    printLine
}

startUserge() {
    runPythonModule userge "$@"
}

stopUserge() {
    sendMessage "⚠️ Exiting DAMIEN-X ..."
    exit 0
}

handleSigTerm() {
    log "💬 Exiting With SIGTERM (143) ..."
    stopUserge
    endLogBotPolling
    exit 143
}

handleSigInt() {
    log "💬 Exiting With SIGINT (130) ..."
    stopUserge
    endLogBotPolling
    exit 130
}

runUserge() {
    initUserge
    startLogBotPolling
    startUserge "$@"
    stopUserge
}
