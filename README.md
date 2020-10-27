# Utility-bwt

A BWT (Burrows Wheeler Transform) utility suite written in python.

## Usage

to execute the script simply run the following command:

```python
python3 bwt.py -i <sequence> -c <B> -s <A>
```

Where:

- ```-i```: is the input sequence without the final '$' character (the script will add the '$' for you). If you accidentaly add
one or more '$' in the input sequence, the script will remove those for you. In particular, it will remove all the wrong
'$' and then put a final '$', in order to compute the BWT, CA and SA. For example, if you run the script with the
sequence "$pa$nam$aban$ana$s$", the script will convert it to "panamabananas" and then it will append a final '$',
getting "panamabananas$".

- ```-c```: is the integer B used for computing the Checkpoint Array. If not specified, the default value will be 1.
- ```-s```: is the integer A used for computing the Suffix Array. If not specified, the default value will be 1.

The previous arguments are also aviable in their extended version:

- ```--input```
- ```--checkpoint_array```
- ```--suffix_array```

Their behavior is the same as the corrensponding short version.

Here's an example of run:

```shell
➜  utility-bwt git:(master) ✗ python3 bwt.py -i biology -c 2 -s 3

                CA
BWM        FO   $bgiloy   SA
$biology | 0  | 0000000 | --
biology$ | 1  | ------- | 0
gy$biolo | 2  | 1000001 | --
iology$b | 3  | ------- | --
logy$bio | 4  | 1100011 | 3
ogy$biol | 5  | ------- | --
ology$bi | 6  | 1100121 | --
y$biolog | 7  | ------- | 6

Burrows-Wheeler Transform:      y$obolig

➜  utility-bwt git:(master) ✗ python3 bwt.py --input biology --checkpoint_array 2 --suffix_array 3

                CA
BWM        FO   $bgiloy   SA
$biology | 0  | 0000000 | --
biology$ | 1  | ------- | 0
gy$biolo | 2  | 1000001 | --
iology$b | 3  | ------- | --
logy$bio | 4  | 1100011 | 3
ogy$biol | 5  | ------- | --
ology$bi | 6  | 1100121 | --
y$biolog | 7  | ------- | 6

Burrows-Wheeler Transform:      y$obolig
```

## Alternative usage

If you don't like command line arguments, it is possible to run the script without them. In this case, the terminal
will prompt you a message asking if you want to insert the argument manually, or you want to close the program. Here is
an example.

```shell
➜  utility-bwt git:(master) ✗ python3 bwt.py
Missing mandatory parameters, whould you like to specify those now? [y/n] n
➜  utility-bwt git:(master) ✗

➜  utility-bwt git:(master) ✗ python3 bwt.py
Missing mandatory parameters, whould you like to specify those now? [y/n] maybe
Please respond with 'yes' or 'no' (or 'y' or 'n').

Missing mandatory parameters, whould you like to specify those now? [y/n] yes
Enter sequence: panamabananas
Enter integer B for the Checkpoint array (blank for 1): 2
Enter integer A for the Suffix array (blank for 1): 3

                      CA
BWM              FO   $abmnps   SA
$panamabananas | 0  | 0000000 | --
abananas$panam | 1  | ------- | --
amabananas$pan | 2  | 0001001 | 3
anamabananas$p | 3  | ------- | --
ananas$panamab | 4  | 0001111 | --
anas$panamaban | 5  | ------- | 9
as$panamabanan | 6  | 0011211 | --
bananas$panama | 7  | ------- | 6
mabananas$pana | 8  | 0111311 | --
namabananas$pa | 9  | ------- | --
nanas$panamaba | 10 | 0311311 | --
nas$panamabana | 11 | ------- | --
panamabananas$ | 12 | 0511311 | 0
s$panamabanana | 13 | ------- | 12

Burrows-Wheeler Transform:      smnpbnnaaaaa$a
```
