# AIGEN-Tool
AIGEN is an open source tool for the generation of transition systems in the symbolic representation "AIGER". To ensure diversity, it employs a uniform random sampling over the space of all Boolean functions with a given number of variables. AIGEN relies on the fact that ROBDDs are canonical representations of Boolean functions, and uses an approach that is inspired by data structures used to implement ROBDDs. Several parameters allow the user to restrict random generation to certain types of Boolean functions or transition systems, which are then output in AIGER format.

To install the tool run setup.sh:
./setup.sh

