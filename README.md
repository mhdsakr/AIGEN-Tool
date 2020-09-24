# AIGEN-Tool
AIGEN is an open source tool for the generation of transition systems in the symbolic representation "AIGER". To ensure diversity, it employs a uniform random sampling over the space of all Boolean functions with a given number of variables. AIGEN relies on the fact that ROBDDs are canonical representations of Boolean functions, and uses an approach that is inspired by data structures used to implement ROBDDs. Several parameters allow the user to restrict random generation to certain types of Boolean functions or transition systems, which are then output in AIGER format.

To install the tool execute: ./setup.sh

                           **********************************************************

To install it manually:

1- Unzip AIGEN Tool

2- Open to mpmath-1.1.0 Folder

3- run the command: sudo python setup.py install

4- Open aiger-1.9.9 Folder

5- run the command ./configure.sh && make

6- copy the executable "aigtoaig" to parent folder i.e. in the same location of "Convert-Int-To-Bdd_out.py"

7- run the command: sudo apt-get install libtinfo-dev

8- run the command: sudo dpkg -i libreadline-dev_7.0-3_amd64.deb

9- Open abc-master folder

10- run the command: make

11- copy the executable "abc" to parent folder i.e. in the same location of "aigen.py"

12- run the command: sudo apt install python-pip

13- run the command: sudo apt-get install libgmp-dev

14- run the command: sudo apt-get install libmpfr-dev

15- run the command: sudo apt-get install libmpc-dev

16- run the command: pip install gmpy2
                                                      
                           **********************************************************
                           
To run the tool execute the command: 

python aigen.py -output file1.aag -c 1 -u 1 -l 10 -o 9

where:

FileName.aag is the file name to be generated
c=1 means 1 controllable input
u=1 means 1 uncontrollable inputs
l=10 means 10 latches (i.e. the tool will generate 12 boolean functions over 15 variables)
o=9 means that 9 latches variable influences the output function (i.e. the output function will assign true to (l - o) variables and in this case (10-9) )

or with seeds. Note that the number of seeds must be equal to l + 1

python aigen.py -output random_n_14_4_3_7_6.aag -c 4 -u 3 -l 7 -o 6 -seeds 1589315720245050 1589315720836518 1589315721306326 1589315721746553 1589315722185292 1589315722596544 1589315722995663 1589315723406943 -oseed 1589315723415047 -noABC 1

oseed is the seed for the random 6 variables chosen out of 7 latches.
-noABC 1 is an optional parameter which means that we do not want to run ABC and obtain a reduced version. The files of the table in the paper were generated with "-noABC 1"




