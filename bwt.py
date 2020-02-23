
# global vaiables definition
bwt = []
firstOccurrence = []
checkpointArray = []
suffixArray = []


def BWT(sequence):
    sequence += '$'
    bwt = [sequence[index:] + sequence[:index]
           for index, _ in enumerate(sequence)]
    bwt.sort()

    # transposing the matrix and getting his first row (the first column)
    for index in range(len(sequence)):
        firstOccurrence.append(index)

    # Just for test
    print("your firstOccurrence is: " + repr(firstOccurrence))

    checkpointIndexes = []  # empty list
    for character in sequence:
        if character not in checkpointIndexes:
            checkpointIndexes.append(character)
    checkpointIndexes.sort()

    # Just for test
    print("your sorted is: " + repr(checkpointIndexes))

    # Presentation, formatting the string for the video

    print("\n")
    print("BWT Matrix")
    length = len(sequence)

    for elem in range(len(sequence)):
        row = bwt.__getitem__(elem)
        print('|' + row[0] + ' ' + row[1:length-1] + ' ' + row[length-1] + '| '
              + repr(firstOccurrence[elem]) + '| ')
    print("\n")

    finalBwt = [rotation[-1] for rotation in bwt]
    finalBwt = ''.join(finalBwt)

    return finalBwt


def inverse_BWT(sequence):
    table = [col for col in sequence]
    for i in range(len(sequence) - 1):
        table.sort()
        table = [sequence[i] + table[i] for i in range(len(sequence))]

    return table[[row[-1] for row in table].index('$')]


sequence = input('Enter sequence: ')
if sequence != "":
    bwt = BWT(sequence)
    print('Burrows-Wheeler Transform:         ' + str(bwt))

    inverse = inverse_BWT(bwt)
    print('Inverse Burrows-Wheeler Transform: ' + str(inverse))
else:
    print("Error: cannot apply BTW on empty string!")
