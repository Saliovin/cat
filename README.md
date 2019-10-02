# Simple cat

## What is it?
This program is a Python implementation of various functionalities of the UNIX command "cat".

## Requirements
- [Python 3](https://www.python.org/downloads/)

## How to Use?
```
python simple_cat.py [-h] [-w] [-a] [-c] [-mk] [files [files ...]]
```

## Arguments
```
positional arguments:
  files         Files to be opened. Prints the contents of each file if there
                are no optional arguments.

optional arguments:
  -h, --help    show this help message and exit
  -w, --write   Requests a string from the user and writes it to every file
                Creates a new file if output file is non-existing.
  -a, --append  Takes all the data from inputted files, except the last and
                appends them to the last file. Creates a new file if output
                file is non-existing.
  -c, --concat  Takes all the data from inputted files, except the last and
                concatenates them to the last file. Creates a new file if
                output file is non-existing.
  -mk, --make   Creates each inputted file if non-existing.
```

## Examples
Creating three files named testA, testB, and testC.
```
python simple_cat.py -mk testA testB testC
```

Reading the content of testA
```
python simple_cat.py testA
```

Appending the contents of testA to testB.
```
python simple_cat.py -a testA testB testC
```

Concatenating the contents of testA, testB, and testC, then outputting it to testD
```
python simple_cat.py -c testA testB testC testD
```
