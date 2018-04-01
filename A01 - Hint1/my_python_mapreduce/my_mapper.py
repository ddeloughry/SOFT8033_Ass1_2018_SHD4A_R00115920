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
    dictionary = dict()
    for each_line in input_stream:
        split_line = each_line.split()
        lang_abrev = split_line[0]
        if (lang_abrev[:2] in languages) == True:
            if lang_abrev.__len__() == 2 or ("." in lang_abrev) == True:
                if (lang_abrev in dictionary) == False:
                    dictionary[lang_abrev] = []
                dictionary[lang_abrev].append(split_line[1] + ", " + split_line[2])
    for each_proj_name in dictionary:
        each_proj = dictionary[each_proj_name]
        sorted_proj = []
        for each_line in each_proj:
            (k, v) = get_kv(each_line)
            sorted_proj.append((k, v))
        sorted_proj = sorted(sorted_proj, key=lambda value: value[1], reverse=True)
        for each in sorted_proj[:num_top_entries]:
            output_stream.write(each_proj_name + " (" + each[0] + "\t" + each[1] + ")\n")


# ------------------------------------------
# Return key and value for line
# ------------------------------------------
def get_kv(line):
    return line.split()[0], line.split()[1]


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

    i_file_name = "C:/Users/ddelo/Dropbox/College/FourthYear/Semester2/Big " \
                  "Data/Ass1/my_dataset/pageviews-20180219-100000_0.txt "
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)
