                           ******************************* AIGEN Tool  *********************************

AIGEN is an open source tool for the generation of transition systems in a symbolic representation "AIGER". To ensure diversity, it employs a uniform random sampling over the space of all Boolean functions with a given number of variables. AIGEN relies on reduced ordered binary decision diagrams (ROBDDs) and canonical disjunctive normal form (CDNF) as canonical representations that allow us to enumerate Boolean functions, in the former case with an encoding that is inspired by data structures used to implement ROBDDs. Several parameters allow the user to restrict generation to Boolean functions or transition systems with certain properties, which are then output in AIGER
format. .


                           ******************************* INSTALLATION  *********************************


To install the tool automatically run the following commands: (this will take around 15 minutes due to the abc tool compiling time)
	- chmod +x setup.sh
	- ./setup.sh

                           **************************** Manual Installation ******************************

To install it manually:

1- Unzip AIGEN Tool

2- Open to mpmath-1.1.0 Folder

3- run the command: sudo python setup.py install

4- Open aiger-1.9.9 Folder

5- run the command ./configure.sh && make

6- copy the executable "aigtoaig" to parent folder i.e. in the same location of "Convert-Int-To-Bdd_out.py"

7- run the command: sudo apt-get install libtinfo-dev

8- run the command: sudo dpkg -i libreadline-dev_8.0-4_amd64.deb  (for ubuntu 18: sudo dpkg -i libreadline-dev_7.0-3_amd64.deb)

9- Open abc-master folder

10- run the command: make

11- copy the executable "abc" to parent folder i.e. in the same location of "aigen.py"

12- run the command: sudo apt install python-pip

13- run the command: sudo apt-get install libgmp-dev

14- run the command: sudo apt-get install libmpfr-dev

15- run the command: sudo apt-get install libmpc-dev

16- run the command: pip3 install gmpy2 (for ubuntu 18: pip install gmpy2)
                                                      
                           **************************** Test the Tool ************************************
                           

AIGEN is pre-installed on this virtual machine in folder ”AIGEN-AE-Submission”.

To test its basic functionality, you can run a simple command like: 

python3 AIGEN-AE-Submission/aigen.py -bdd -output ReviewerTest.aag -c 1 -u 1 -l 5 -o 4 -noABC
where:
* FileName.aag is the file name to be generated.

* -bdd means that use a bdd based random generation. When replaced by

* -dnf the tool will use canonical DNF based random generation.
 
* -c 1 means 1 controllable input

* -u 1 means 1 uncontrollable inputs

* -l 10 means 10 latches (i.e. the tool will generate 12 Boolean functions over 15 variables)

* -o 9 means that 9 latches variable influences the output function (i.e. the output function will assign true to (l - o) variables and in this case (10-9)).

* -noABC is an optional parameter. A user has to omit it if he wants to run the ABC tool minimization procedure that reduces the size of the generated AIGER file.

After the call terminates, AIGEN will have generated the file ”FileName.aag”, including the resulting transition system in AIGER format and comments at the end of the file that include the parameters of its generation, namely the seeds that has been used to generate the random numbers for each latch, and the seed for choosing random 9 variables out of 10 to be used in the output function.

To replicate an existing file (an AIGER file that was generated previously by AIGEN tool), use as arguments the same model (bdd or dnf), number of uncontrollable inputs, number of controllable inputs, number of latches, the same number of output variables, and the same seeds. All these info can be found as comments at the end of the file. Note that the number of seeds must be equal to l + 1.
