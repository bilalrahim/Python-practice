#Python looks for modules in sys.path. sys.path is a python list we can add the module directory by appending module directory to sys.path .
# 1.Import sys module.
# 2.sys.path.append('module_path')


import sys
#to add directory path sys.path.append ('C:\Users\mazhrR\Desktop\Bilal\Python Practice')
for path in sys.path:
    print (path)

import circle

print circle.pi
