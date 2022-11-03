import os,sys
try:
    os.system("git pull")
    __import__('NOOB').main_menu()
except:
    sys.exit()
