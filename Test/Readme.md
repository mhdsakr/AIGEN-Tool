noABCAll the files in folder "Aiger" are generateb by the tool.
All these files can be replicated. To replicate an existing file  file usse as arguments the same model(BDD or DNF), number of uncontrollable inputs, number of controllable inputs, number of latches, the same number of output variables, and the same seeds. All these info can be found as comments at the end of the file.

For instance to replicate the file "bdd_random_n1_4_4_7_7.aag". From its name, we can figure out that this file has 4 controllable inputs, 4 uncontrollable inputs, 7 latches, and 7 output variables that are used in the output function. The term BDD used in the name of the file indicate that the bdd approach is used instead of the DNF approach. Additionally at the end of this file we find the following info:

latch 0 seed: 1602059572241408

latch 1 seed: 1602059572968276

latch 2 seed: 1602059573619612

latch 3 seed: 1602059574343556

latch 4 seed: 1602059574958170

latch 5 seed: 1602059575536372

latch 6 seed: 1602059576146510

output 7 seed: 1602059576729040

output vars seed: None

Then to replicate the same file, a user can execute the following command:

python aigen.py -bdd -output experiments/bdd_random_n1_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 -seeds 1602059572241408 1602059572968276 1602059573619612 1602059574343556 1602059574958170 1602059575536372 1602059576146510 1602059576729040

The line "output vars seed: None" states that there was no need for the argument -oseeds.

Remember that if you don't want to use abc, which generate a minimized version of the same instance under the name "bdd_random_n1_4_4_7_7_abc.aag", use the argument "-noABC".

