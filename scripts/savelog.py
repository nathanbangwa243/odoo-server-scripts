# -*- coding: utf-8 -*-

import os
import datetime

from . import config
import shutil

def init_log_file():
    now = datetime.now()

    config.LOG_FILE = now.strftime("%m-%d-%Y--%H-%M-%S.text")

    add_log(f"[Init log file at {now}]")

def add_log(log_msg):

    log_msg = "{log_msg}\n"

    # check log file
    if not(os.path.exists(config.LOG_FILE)):
        with open(config.LOG_FILE, 'w') as fp:
            pass
    
    with open(config.LOG_FILE, 'a') as fp:
        fp.write(log_msg)