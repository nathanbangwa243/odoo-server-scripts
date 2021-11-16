
from scripts import *


def test_get_repo_name_from_url():

    from scripts import update_addons

    name = update_addons.get_repo_name_from_url("https://github.com/ishepard/pydriller.git/asd")

    print(name)

def test_extract_compressed_file():

    from scripts import update_addons

    update_addons.extract_compressed_file(
        cfilename="C:\\Users\\NathanBangwa\\Documents\\Projects\\exonus-tech\\odoo-server-scripts\\localhost\\sale_rental.zip", 
        dest_folder="C:\\Users\\NathanBangwa\\Documents\\Projects\\exonus-tech\\odoo-server-scripts\\localhost"
    )

if __name__ == "__main__":
    pass
    # test_extract_compressed_file()
