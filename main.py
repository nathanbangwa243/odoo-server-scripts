#-*- coding: utf-8 -*-

import os
import sys

from scripts import initialize
from scripts import update_addons
from scripts import update_config

def main():
    if "--initialize" in sys.argv:
        # initialize
        initialize.main()
    
    elif "--update-addons" in sys.argv:
        pass

if __name__ == "__main__":
    main()