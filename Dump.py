import os, platform

os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import Dump
elif bit == '32bit':
    import Dump32
