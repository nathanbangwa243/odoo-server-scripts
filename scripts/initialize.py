# -*- coding: utf-8 -*-

# system
import os

# local
from . import config
from . import savelog
from . import datamanag


def copy_files(*files_to_copy, dest):
    # copy exonus-script.sh file and config.json

    log_msg = "[initialize.py/copy_files] Start Process\n"

    for src_files in files_to_copy:

        # copy file
        try:
            pass
        except Exception as error:
            log_msg += f"[copy_files error] filename : {src_files}\n{error}\n"
        else:
            log_msg += f"[copy_files success] filename : {src_files}\n"
        finally:
            log_msg += f"[initialize.py/copy_files] End Process"

            # save log
            savelog.add_log(log_msg=log_msg)


def modify_config(projectID):
    log_msg = "[initialize.py/modify_config] Start Process\n"

    try:

        config_data = datamanag.load_json_data(
            filename=f"{config.EXONUS_TECH_PATH}/config/config.json",
        )

        # update workOn projectID
        config_data["hosting"]['workOn'] = projectID

        # save config data
        datamanag.save_json_data(
            filename=f"{config.EXONUS_TECH_PATH}/config/config.json",
            data=config_data,
        )

    except Exception as error:
        log_msg += f"[modify_config error] filename : {error}\n"
    else:
        log_msg += f"[modify_config success] filename : projectID = {projectID}\n"
    finally:
        log_msg += f"[initialize.py/modify_config] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def main():
    # INIATIALIZE WORKFLOW
    savelog.init_log_file()

    # copy exonus-script.sh and config.json files
    copy_files(
        f"{config.ODOO_SERVER_SCRIPT_PATH}/config/exonus-script.sh",
        f"{config.ODOO_SERVER_SCRIPT_PATH}/config/config.json",
        dest=f"{config.EXONUS_TECH_PATH}/config",
    )

    # modify config
    projectID = input("[ProjectID]: ")
    modify_config(projectID=projectID)

    # copy exonus-tech.service
    copy_files(
        f"{config.ODOO_SERVER_SCRIPT_PATH}/scripts/exonus-tech.service",
        dest=f"{config.SYSTEMD_PATH}",
    )
