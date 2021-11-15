# -*- coding: utf-8 -*-


import os

from . import config
from . import datamanag
from . import savelog


def update_config_file(old_config_file, new_config_file):
    log_msg = "[update_config.py/update_config_file] Start Process\n"

    try:
        # load old config data
        old_config_data = datamanag.load_json_data(
            filename=old_config_file,
        )

        # load updated config data
        updated_config_data = datamanag.load_json_data(
            filename=new_config_file,
        )

        # update 
        updated_config_data["hosting"]['workOn'] = old_config_data["hosting"]['workOn']

        datamanag.save_json_data(
            filename=old_config_file,
            data=updated_config_data,
        )

    except Exception as error:
        log_msg += f"[update_config_file error] filename : {error}\n"
    else:
        log_msg += f"[update_config_file success] filename : projectID = {old_config_file}\n"
    finally:
        log_msg += f"[update_config.py/update_config_file] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def update_odoo_config_file(config_file, addons_paths):
    # work with project config file
    log_msg = "[update_config.py/update_config_file] Start Process\n"

    try:
        # load work config data
        config_data = datamanag.load_json_data(
            filename=config_file,
        )

        # odoo config file path
        odoo_conf_file = config_data['hosting']['workOn']['odoo.conf.path']

        # build addons path
        all_addons = []

        # add exonus-tech addons
        all_addons += [
            addon_path for addon_path in os.listdir(os.path.join(
                addons_paths, "exonus-addons"))
        ]

        # add community addons
        all_addons += [
            addon_path for addon_path in os.listdir(os.path.join(
                addons_paths, "community"))
        ]

        # modify config file

        # load odoo config
        odoo_config_data = datamanag.read_data(odoo_conf_file)  # str

        # split odoo config data
        odoo_config_data = odoo_config_data.split('\n')  # list

        for index in range(len(odoo_config_data)):
            # data line
            data_line = odoo_config_data[index]

            # find odoo addons line
            if config.ODOO_ADDONS_LINE in data_line:
                # data split
                # odoo-addons = default path
                data_line = data_line.split(",")[0]

                data_line += all_addons

                # data join
                data_line = ",".join(data_line)

                # replace data line
                odoo_config_data[index] = data_line

                break

        # join odoo config
        odoo_config_data = "\n".join(odoo_config_data)  # str

        # save new odoo config file
        datamanag.write_data(odoo_conf_file, odoo_config_data)

    except Exception as error:
        log_msg += f"[update_odoo_config_file error] filename : {error}\n"
    else:
        log_msg += f"[update_odoo_config_file success] filename : {config_file}\n"
    finally:
        log_msg += f"[update_config.py/update_odoo_config_file] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)
