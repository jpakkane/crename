#!/usr/bin/env python3

import os, sys, os.path, pathlib, shutil, subprocess, re

def handle_makefiles():
    file_finder = re.compile(r'\b[-_a-zA-Z0-9/]+\.C\b')
    # If you want to process CMake files, then change
    # this glob to **/CMakeLists.txt (not tested)
    for f in pathlib.Path('.').glob('**/Makefile*'):
        outlines = []
        def file_matcher(mobj):
            # Only change those strings that point to existing
            # files on disk. If your build system does something
            # fancier like building paths by string concatenation,
            # you might need to loosen the requirements here.
            fname = mobj.group(0)
            fpath = f.parent / fname
            if fpath.exists():
                return fname[:-2] + '.cpp'
            else:
                return fname
        for line in f.open():
            outlines.append(file_finder.sub(file_matcher, line))
        f.write_text(''.join(outlines))

def rename_files():
    for f in pathlib.Path('.').glob('**/*.C'):
        subprocess.check_call(['git', 'mv', f, f.with_suffix('.cpp')])

def process():
    handle_makefiles()
    rename_files()

if __name__ == '__main__':
    if not os.path.exists('.git'):
        sys.exit('This script must be run in the root of the git directory.')
    if not shutil.which('git'):
        sys.exit('Git not available.')
    process()

