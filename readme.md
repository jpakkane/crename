# Rename all .C files to .cpp

Some projects use `.C` file extension for C++ source code.
Unfortunately other projects use the same extension for plain C source
files. Because of this and other reasons people are recommended to use
a different extension like `.cpp`.

Doing this conversion by hand is cumbersome, which is why this script
exists. Run it in your source root and it will rename all source files
and also go through all Makefiles and renames them as well. This
should do 99% of all the work. A test compilation should reveal any
remaining issues which can then be fixed by hand.

## Configuration

The script itself does not provide any options. If your needs are
different, edit the code directly, run the conversion and then you can
throw the script away.
