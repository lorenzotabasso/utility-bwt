"""
A Simple BWT script in python that computes BWM, First Occurrences array,
Checkpoint Array and Suffix Array.
"""

__author__ = "Lorenzo Tabasso"

import sys
import re
from optparse import OptionParser
from itertools import cycle


def rotations(t):
    """ Return list of rotations of input string t """
    tt = t * 2
    return [ tt[i:i+len(t)] for i in list(range(0, len(t))) ]


def bwm(t):
    """ Return lexicographically sorted list of t’s rotations (BWM) """
    global bwt_all
    temp = sorted(rotations(t))

    for i in list(range(0, len(temp))):
        bwt_all[i] = (temp[i],)

    return temp


def bwt_via_bwm(t):
    """ Given a string T, returns BWT(T) by way of the BWM """
    return ''.join(map(lambda x: x[-1], bwm(t)))


def first_occurrence():
    """ Returns the First Occurence array of the input sequence """
    global bwt_all

    for i in bwt_all:
        bwt_all[i] += (i,)


def checkpoint_array(bwt, b=1):
    """ Returns the Checkpoint Array of the input sequence """

    global bwt_all, checkpoint_array_letters

    letters = set(bwt)
    checkpoint_array_letters = sorted(list(letters))

    row = ""
    for i in bwt_all:
        if b and i % b == 0:
            for letter in checkpoint_array_letters:
                row += str(bwt[:i].count(letter))

            bwt_all[i] += (row,)
            row = ""
        else:
            for letter in checkpoint_array_letters:
                row += str(bwt[:i].count(letter))

            row = "-" * len(checkpoint_array_letters)
            bwt_all[i] += (row,)
            row = ""


def suffix_array(a=1):
    """ Returns the Suffix Array of the input sequence """

    global bwt_all

    for i in bwt_all:

            rotation = bwt_all[i][0]
            rotation_length = len(rotation)-1

            pool = cycle(rotation)
            j = 0
            for c in pool:
                if c == "$":
                    break
                j += 1

            sa = rotation_length - j
            if a and sa % a == 0:
                bwt_all[i] += (rotation_length - j,)
            else:
                bwt_all[i] += ("--",)


def pretty_print(sequence):
    """ It does some pretty printing """

    str_bwm = "BWM" + " " * int(len(sequence) + 3 - len("BWM"))
    str_fo = "FO" + " " * 3
    str_sa = " " * 3 + "SA"
    str_ca = " " * len(str_bwm + str_fo) + "CA"

    letter = ""
    for x in checkpoint_array_letters:
        letter += x

    print("\n{0}".format(str_ca))
    print("{0}{1}{2}{3}".format(str_bwm, str_fo, letter, str_sa))

    for i in bwt_all:
        if len(str(bwt_all[i][1])) == 1:
            print("{0} | {1}  | {2} | {3}".format(bwt_all[i][0], bwt_all[i][1], bwt_all[i][2], bwt_all[i][3]))
        else:
            print("{0} | {1} | {2} | {3}".format(bwt_all[i][0], bwt_all[i][1], bwt_all[i][2], bwt_all[i][3]))


# Global variables
bwt_all = {}
checkpoint_array_letters = []

if __name__ == "__main__":
    
    argv = sys.argv[1:]
    parser = OptionParser()

    parser.add_option("-i", "--input", help='input', action="store", type="string", dest="input")

    parser.add_option("-c", "--checkpoint_array", help='integer B for the checkpoint array', action="store", type="int",
                        dest="checkpoint_array", default=1)

    parser.add_option("-s", "--suffix_array", help='integer A for the suffix array', action="store", type="int",
                        dest="suffix_array", default=1)

    (options, args) = parser.parse_args()

    if options.input is None or options.checkpoint_array is None or options.suffix_array is None:
        valid = {"yes": True, "y": True, "no": False, "n": False}
        
        exit = False
        while not exit:
            message = "Missing mandatory parameters, whould you like to specify those now? [y/n] "
            choice = input(message)
            if choice not in valid:
                print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
            elif valid[choice] == False:
                sys.exit(2)
            else:  # valid[choice] == True, e.g. "yes"
                exit = True

        sequence = input('Enter sequence: ')

        b = input('Enter integer B for the Checkpoint array (blank for 1): ')
        a = input('Enter integer A for the Suffix array (blank for 1): ')
        if b == "":
            b = 1
        if a == "":
            a = 1
    else:
        sequence = options.input
        b = options.checkpoint_array
        a = options.suffix_array

    cleaned_sequence = sequence.replace("$", "") + "$" 
    final = bwt_via_bwm(cleaned_sequence)

    first_occurrence()
    checkpoint_array(final, int(b))
    suffix_array(int(a))
    pretty_print(cleaned_sequence)

    print('\nBurrows-Wheeler Transform:\t{}'.format(final))
