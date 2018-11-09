# parse_ini.py

import os
import configobj

newConfig = configobj.ConfigObj('new/front_decode.ini')
defaultConfig = configobj.ConfigObj('front_decode.ini')

for section in newConfig.keys():
    for key in newConfig[section].keys():
        # print section, key, newConfig[section][key]
        defaultConfig[section][key] = newConfig[section][key]
        
os.rename('front_decode.ini', 'front_decode_bak.ini')
        
with open('front_decode.ini', 'w') as configfile:
    defaultConfig.write(configfile)