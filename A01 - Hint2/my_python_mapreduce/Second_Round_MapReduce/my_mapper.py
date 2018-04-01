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
def my_map(input_stream, per_language_or_project, output_stream):
    dictionary = dict()
    for each_line in input_stream:
        lang = (each_line.split())[0]
        if '.' in lang:
            lang = (each_line.split())[0].split('.')[1]
            if per_language_or_project:
                lang = (each_line.split())[0].split('.')[0]
        elif not per_language_or_project:
            lang = "wikipedia"
        if lang not in dictionary:
            dictionary[lang] = 0
        if (each_line.split())[-2].isdigit():
            dictionary[lang] = dictionary[lang] + int((each_line.split())[-2])
        elif (each_line.split())[1].isdigit():
            dictionary[lang] = dictionary[lang] + int((each_line.split())[1])
    for key in dictionary:
        output_stream.write(key + "\t" + str(dictionary[key]) + "\n")


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, per_language_or_project):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_map(my_input_stream, per_language_or_project, my_output_stream)


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

    per_language_or_project = True  # True for language and False for project

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, per_language_or_project)
