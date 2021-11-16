# -*- coding:utf -*-


# system
import os

# file manag
from zipfile import ZipFile

# web
import requests

# mine
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


def get_repo_name_from_url(url: str) -> str:
    # make copy of url
    clean_url = str(url)

    # catch .git index
    git_suffix_index = clean_url.rfind(".git")

    # clean url
    clean_url = url[:git_suffix_index]

    # catch last slash
    last_slash_index = clean_url.rfind("/")

    if last_slash_index < 0 or git_suffix_index <= last_slash_index:
        raise Exception("Badly formatted url {}".format(url))

    repo_name = clean_url[last_slash_index + 1:git_suffix_index]

    return repo_name


def extract_compressed_file(cfilename, dest_folder):
    log_msg = "[update_addons.py/extract_compressed_file] Start Process\n"

    try:
        with ZipFile(cfilename, 'r') as zip_obj:
            # extract content at dest_folder
            zip_obj.extractall(path=dest_folder)

    except Exception as error:
        log_msg += f"[extract_compressed_file error] : {error}\n"
    else:
        log_msg += f"[extract_compressed_file success] filename : path = {cfilename}\n"
    finally:
        log_msg += f"[update_addons.py/extract_compressed_file] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def download_file(url, filename, dest_folder, is_compressed=False):

    log_msg = "[update_addons.py/download_file] Start Process\n"

    try:
        # get file stream
        response = requests.get(url)

        filename_path = os.path.join(config.EXONUS_TECH_TEMP_PATH, filename)

        # save file stream
        if response.status_code == 200:
            with open(filename_path, "w") as fp:
                fp.write(response.content)

            # add log
            log_msg += f"[download_file success] located at : {filename_path}\n"

            if is_compressed:
                # extract file
                extract_compressed_file(
                    cfilename=filename_path, dest_folder=dest_folder)

        else:
            # add log
            raise requests.exceptions.RequestException(
                f"[download_file error] status_code : {response.status_code}"
            )

    except Exception as error:
        log_msg += f"[download_file error] filename : {error}\n"
    else:
        log_msg += f"[update_exonus_addons success] filename : Link = {url}\n"
    finally:
        log_msg += f"[update_addons.py/download_file] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def update_addons_repertory(addon_parent_dir, addon_path, addon_config_data):
    # addons group is git-repo
    if addon_config_data["is-git-repo"]:
        # git repo
        github_group_repo_link = addon_config_data['github-link']

        if os.path.exists(addon_path):
            # update
            git_pull(addon_path)

        else:
            # clone
            git_clone(parent_path=addon_parent_dir,
                      github_repo=github_group_repo_link)

    # addons must be download
    elif addon_config_data["is-downloadable"]:
        if addon_config_data["is-compressed"]:
            # assert filename not None
            assert isinstance(addon_config_data["module_name"], str)

            # download file
            download_file(
                url=addon_config_data["download-link"],
                filename=addon_config_data["module_name"],
                dest_folder=addon_path,
                is_compressed=True
            )
        else:
            pass


def update_exonus_addons(config_exonus_data):
    log_msg = "[update_addons.py/git_pull] Start Process\n"

    try:
        # update exonus addons
        update_addons_repertory(
            addon_parent_dir=config.ALL_ADDONS_PATH,
            addon_path=config.EXONUS_ADDONS_PATH,
            addon_config_data=config_exonus_data)

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[update_exonus_addons success] filename : path = {config.EXONUS_ADDONS_PATH}\n"
    finally:
        log_msg += f"[update_addons.py/update_exonus_addons] End Process"

        # save log
        savelog.add_log(log_msg=log_msg)


def update_community_addons(config_community_data):
    log_msg = "[update_addons.py/update_community_addons] Start Process\n"

    try:
        for addon_groups_key, addon_groups_datas in config_community_data.items():
            # addons groups path
            addon_groups_path = os.path.join(
                config.COMMUNITY_ADDONS_PATH, addon_groups_key)

            if addon_groups_datas["is-git-repo"] or addon_groups_datas["is-downloadable"]:
                update_addons_repertory(
                    addon_parent_dir=config.COMMUNITY_ADDONS_PATH,
                    addon_path=addon_groups_path,
                    addon_config_data=addon_groups_datas
                )

            # addons in addons groups must be treat individualy
            else:
                # list modules
                for module_datas in addon_groups_datas["modules"]:
                    log_msg += f"[update_community_addons loop] module_name : {module_datas['module_name']}\n"

                    # module path
                    addon_path = os.path.join(
                        addon_groups_path, module_datas["module_name"])

                    update_addons_repertory(
                        addon_parent_dir=addon_groups_path,
                        addon_path=addon_path,
                        addon_config_data=module_datas
                    )

                    log_msg += f"[update_community_addons loop success] module_name : {module_datas['module_name']}\n"

    except Exception as error:
        log_msg += f"[git_clone error] filename : {error}\n"
    else:
        log_msg += f"[update_community_addons success] filename : addons_path = {config.COMMUNITY_ADDONS_PATH}\n"
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
            config_exonus_data=config_data['addons']['exonus'],
        )

        # update community addons
        update_community_addons(
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
