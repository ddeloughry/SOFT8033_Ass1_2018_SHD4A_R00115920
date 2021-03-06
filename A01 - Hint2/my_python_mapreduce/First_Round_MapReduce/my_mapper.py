#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import codecs
import sys


# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(input_stream, output_stream):
    count = 0
    for each_line in input_stream:
        if (each_line.split())[-2].isdigit():
            count = count + int((each_line.split())[-2])
        elif (each_line.split())[1].isdigit():
            count = count + int((each_line.split())[1])
    output_stream.write("count\t" + str(count) + "\n")


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_map(my_input_stream, my_output_stream)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = True

    i_file_name = "C:\\Users\\ddelo\\Dropbox\\College\\FourthYear\\Semester2\\Big Data\\Ass1\\my_dataset\\pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name)
