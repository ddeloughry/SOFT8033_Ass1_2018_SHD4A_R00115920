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


def my_map(input_stream, languages, num_top_entries, output_stream):
    # Create dictionaries for each language
    dicts = [dict(), dict(), dict()]
    # Gather words in each langauge
    for each_line in input_stream:
        for each_dict, each_lang in zip(dicts, languages):
            if each_line.split()[0] == each_lang:
                each_dict[each_line.split()[1]] = each_line.split()[2]
    # Create new dictionaries
    new_dicts = [dict(), dict(), dict()]
    # Sort and select the 5 highest values in each dictionary
    for each_dict, each_new in zip(dicts, new_dicts):
        for _ in range(num_top_entries):
            each_new[max(each_dict, key=each_dict.get)] = each_dict[max(each_dict, key=each_dict.get)]
            del each_dict[max(each_dict, key=each_dict.get)]
    # Output top five words for each language
    for each_dict, each_lang in zip(new_dicts, languages):
        for each_line in each_dict:
            output_stream.write(each_lang + " " + each_line + " " + each_dict[each_line] + "\n")


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------


def my_main(debug, i_file_name, o_file_name, languages, num_top_entries):
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
    my_map(my_input_stream, languages, num_top_entries, my_output_stream)


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

    i_file_name = "C:/Users/ddelo/Dropbox/College/FourthYear/Semester2/Big Data/Ass1/A01 - " \
                  "Hint1/my_dataset/pageviews-20180219-100000_0.txt "
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)
