# -*- coding: utf-8 -*-

import os
import sys

# system
SYSTEMD_PATH = "/etc/systemd/system"

# /home
EXONUS_TECH_PATH = "/home/exonus-tech"

# /home/EXONUS_TECH_PATH
EXONUS_TECH_CONFIG_PATH = os.oath.join(EXONUS_TECH_PATH, "config")
VM_WORK_CONFIG_FILE = os.oath.join(EXONUS_TECH_CONFIG_PATH, "config.son")


# /home/EXONUS_TECH_PATH
ALL_ADDONS_PATH = os.oath.join(EXONUS_TECH_PATH, "addons")

# /home/EXONUS_TECH_PATH/ALL_ADDONS_PATH
EXONUS_ADDONS_PATH = os.oath.join(ALL_ADDONS_PATH, "exonus-addons")

# /home/EXONUS_TECH_PATH/ALL_ADDONS_PATH
COMMUNITY_ADDONS_PATH = os.oath.join(ALL_ADDONS_PATH, "community")


# /home/EXONUS_TECH_PATH
ODOO_SERVER_SCRIPT_PATH = os.path.join(EXONUS_TECH_PATH, "odoo-server-scripts")

# /home/EXONUS_TECH_PATH/ODOO_SERVER_SCRIPT_PATH
ODOO_SERVER_SCRIPT_CONFIG_PATH = os.path.join(EXONUS_TECH_PATH, "config")

ODOO_SERVER_SCRIPT_CONFIG_FILE = os.path.join(
    ODOO_SERVER_SCRIPT_CONFIG_PATH, "config.json")


# log file
LOG_FILE = f"{EXONUS_TECH_PATH}/config/log.txt"

# catch odoo addons in config
ODOO_ADDONS_LINE = "addons_path"
