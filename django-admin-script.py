#!C:\Users\puligpr1\AppData\Local\Programs\Python\Python35\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==1.9','console_scripts','django-admin'
__requires__ = 'Django==1.9'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Django==1.9', 'console_scripts', 'django-admin')()
    )
