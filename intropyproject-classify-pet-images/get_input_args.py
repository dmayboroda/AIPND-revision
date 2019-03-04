#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: David Mayboroda
# DATE CREATED: March 4, 2019
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
import sys
# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
#


def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function
    parser = argparse.ArgumentParser(epilog='\tClassifier: \r\n' + "Please set image folder, CNN architecture, "
                                                                   "dog names file")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('--dir', type=str, help="Dogs images dir", required=True, default='pet_images/')
    parser.add_argument('--arch', type=str, help="CNN architecture", required=True, default='vgg')
    parser.add_argument('--dogfile', type=str, help='Text file with dog names', required=True, default='dognames.txt')

    return parser.parse_args()


def parser_error(errmsg):
    print("Error: " + errmsg)
    print("Use -h for help")
    sys.exit()