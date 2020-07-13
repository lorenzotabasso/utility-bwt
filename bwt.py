"""
A Simple BWT script in python that computes BWM, First Occurrences array,
Checkpoint Array and Suffix Array.
"""

__author__ = "Lorenzo Tabasso"

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
    sequence = input('Enter sequence: ')
    sequence += "$"

    b = input('Enter integer B for the Checkpoint array (blank for 1): ')
    a = input('Enter integer A for the Suffix array (blank for 1): ')
    if b == "":
        b = 1
    if a == "":
        a = 1

    final = bwt_via_bwm(sequence)

    first_occurrence()
    checkpoint_array(final, int(b))
    suffix_array(int(a))
    pretty_print(sequence)

    print('\nBurrows-Wheeler Transform:\t{}'.format(final))
