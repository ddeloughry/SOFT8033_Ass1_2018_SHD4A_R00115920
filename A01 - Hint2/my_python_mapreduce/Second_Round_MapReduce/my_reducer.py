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
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(input_stream, total_words, output_stream):
    dictionary = dict()
    for each_line in input_stream:
        if (each_line.split())[0] not in dictionary:
            dictionary[(each_line.split())[0]] = 0
        dictionary[(each_line.split())[0]] = dictionary[(each_line.split())[0]] + int((each_line.split())[1])
    sorted_dict = sorted(dictionary.items(), key=lambda x: int(x[1]), reverse=True)
    for each in sorted_dict:
        output_stream.write(each[0] + "\t(" + str(each[1]) + ", " + str(each[1] / total_words * 100) + ")\n")


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, total_words, o_file_name):
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
    my_reduce(my_input_stream, total_words, my_output_stream)


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

    # Replace this with the result of the first stage
    # total_words = 0
    total_words = 21996631

    i_file_name = "sort_simulation.txt"
    o_file_name = "reduce_simulation.txt"

    my_main(debug, i_file_name, total_words, o_file_name)
