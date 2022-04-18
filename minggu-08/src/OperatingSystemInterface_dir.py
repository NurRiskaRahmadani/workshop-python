import os
dir(os)

help(os)

import shutil
shutil.copyfile('data.db', 'archive.db')

shutil.move('/build/executables', 'installdir')
