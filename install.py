#!/usr/bin/env python3

import os
import pathlib
import shutil
import stat

if __name__ == '__main__':
    ib_utils_path = os.path.expanduser('~/.ib_utils')
    if not os.path.exists(ib_utils_path):
        os.mkdir(ib_utils_path)
    for script in pathlib.Path('.').glob('*.py'):
        if script == 'install.py':
            continue
        final_path = ib_utils_path + '/' + script.name
        shutil.copy(script, final_path)
        st = os.stat(final_path)
        os.chmod(final_path, st.st_mode | stat.S_IEXEC)

    bash_profile_path = os.path.expanduser('~/.bash_profile')
    if os.path.exists(bash_profile_path):
        with open(bash_profile_path, mode='a') as bash_profile_file:
            bash_profile_file.write('\nPATH=$HOME/.ib_utils:$PATH\n')

    profile_path = os.path.expanduser('~/.profile')
    if os.path.exists(profile_path):
        with open(profile_path, mode='a') as profile_file:
            profile_file.write('\nPATH=$HOME/.ib_utils:$PATH\n')

    bashrc_path = os.path.expanduser('~/.bashrc')
    if os.path.exists(bashrc_path):
        with open(bashrc_path, mode='a') as bashrc_file:
            bashrc_file.write('\nPATH=$HOME/.ib_utils:$PATH\n')
