# CD Command Simulator

## Description

This is a program simulating the behavior of the cd Unix command, which allows
users to change the current directory within a file system. The program takes
two path strings as input from the command line terminal and prints the new path
or an error message.

## Usage

```commandline
python mycd.py [source] [target]
```

* Python3 needed
* Replace `[source]` with the source directory and `[target]` with the target directory.

### Example

```commandline
python mycd.py /abc/def /abc
```

## Test Cases

All test cases are in test_mycd.py.
To execute all tests, run

```commandline
python test_mycd.py
```