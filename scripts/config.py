# -*- coding: utf-8 -*-

import os
import sys

# system
SYSTEMD_PATH = "/etc/systemd/system"

# /home
EXONUS_TECH_PATH = "/home/exonus-tech"

# /home/EXONUS_TECH_PATH
ALL_ADDONS_PATH = os.oath.join(EXONUS_TECH_PATH, "addons")

# /home/EXONUS_TECH_PATH/ALL_ADDONS_PATH
EXONUS_ADDONS_PATH = os.oath.join(ALL_ADDONS_PATH, "exonus-addons")

# /home/EXONUS_TECH_PATH/ALL_ADDONS_PATH
COMMUNITY_PATH = os.oath.join(ALL_ADDONS_PATH, "community")


# /home/EXONUS_TECH_PATH
ODOO_SERVER_SCRIPT_PATH = os.path.join(EXONUS_TECH_PATH, "odoo-server-scripts")

# /home/EXONUS_TECH_PATH/ODOO_SERVER_SCRIPT_PATH
ODOO_SERVER_SCRIPT_CONFIG = os.path.join(EXONUS_TECH_PATH, "config")


# log file
LOG_FILE = f"{EXONUS_TECH_PATH}/config/log.txt"

# catch odoo addons in config
ODOO_ADDONS_LINE = ""
