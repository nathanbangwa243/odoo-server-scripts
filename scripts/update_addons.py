# -*- coding:utf -*-


import os
from . import config
from . import savelog
from . import datamanag


def git_clone(parent_path, github_repo):
    log_msg = "[update_addons.py/git_clone] Start Process\n"

    # current work directory
    cwd = os.getcwd()

    try:
        os.chdir(f"{parent_path}")
        os.system(f"git clone {github_repo}")

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[git_clone success] filename : GitRepo = {github_repo}\n"
    finally:
        log_msg += f"[update_addons.py/git_clone] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)

        # switch to cwd
        os.chdir(cwd)


def git_pull(local_repo):
    log_msg = "[update_addons.py/git_pull] Start Process\n"

    # current work directory
    cwd = os.getcwd()

    try:
        os.chdir(f"{local_repo}")
        os.system(f"git pull")

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[git_pull success] filename : GitRepo = {local_repo}\n"
    finally:
        log_msg += f"[update_addons.py/git_pull] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)

        # switch to cwd
        os.chdir(cwd)


def update_exonus_addons(parent_path, exonus_addons_path, config_exonus_data):
    log_msg = "[update_addons.py/git_pull] Start Process\n"

    try:
        # git repo
        github_exonus_repo = config_exonus_data['git-repo']

        if os.path.exists(exonus_addons_path):
            # update
            git_pull(exonus_addons_path)

        else:
            # clone
            git_clone(parent_path=parent_path, github_repo=github_exonus_repo)

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[update_exonus_addons success] filename : GitRepo = {github_exonus_repo}\n"
    finally:
        log_msg += f"[update_addons.py/update_exonus_addons] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def update_community_addons(community_addons_path, config_community_data):
    log_msg = "[update_addons.py/git_pull] Start Process\n"

    try:
        for parent_addon_folder in config_community_data:
            #
            parent_addon_path = os.path.join(
                community_addons_path, parent_addon_folder)

            # list modules
            for module_infos in config_community_data[parent_addon_folder]:
                #
                module_name, module_repo = module_infos

                # module path
                module_path = os.path.join(parent_addon_path, module_name)

                if os.path.exists(module_path):
                    # update
                    git_pull(module_path)

                else:
                    # clone module repo
                    git_clone(parent_path=parent_addon_path,
                              github_repo=module_repo)

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[update_community_addons success] filename : addons_path = {community_addons_path}\n"
    finally:
        log_msg += f"[update_addons.py/update_community_addons] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def main():
    log_msg = "[update_addons.py/main] Start Process\n"

    try:
        # load config data
        config_data = datamanag.load_json_data(
            filename=config.ODOO_SERVER_SCRIPT_CONFIG_FILE,)

        # update exonus addons
        update_exonus_addons(
            parent_path=config.ALL_ADDONS_PATH,
            config_exonus_data=config_data['addons']['exonus'],
        )

        # update community addons
        update_community_addons(
            community_addons_path=config.COMMUNITY_ADDONS_PATH,
            config_community_data=config_data['addons']['community'],
        )

    except Exception as error:
        log_msg += f"[main error] filename : {error}\n"
    else:
        log_msg += f"[main success] filename\n"
    finally:
        log_msg += f"[update_addons.py/main] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)
