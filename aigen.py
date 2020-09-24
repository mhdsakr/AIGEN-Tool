import argparse
import time
import convertToAiger
import GenerateBDDs
import ABCMinimization
import os
import sys

if __name__ == '__main__':
####################End of Converting BDD to AIG ###############################
    startTime = int(round(time.time() * 1000))
    
    var_nb = 0  # total nuumber of variables in the aiger file
    input_nb = 0  # total number of inputs in the aiger
    u_nb = 0  # number of uncontrollable input
    c_nb = 0  # number of controllable input
    fileName = ""  # aiger file to be generated
    noABC = 0
    oseed = 0 # to store the seed for the selected variables in the output function
    inputSeeds = [] # to store input latches and output functions seeds if any
    
    
    parser = argparse.ArgumentParser(description='Generating random aiger files')
    parser.add_argument('-output','--outputFile',help='Output file name, ex: myFile.aag', required=True)
    parser.add_argument('-c','--controllables', help='Number of controllable input variables', type=int, required=True)
    parser.add_argument('-u','--uncontrollables',help='Number of uncontrollable input variables', type=int, required=True)
    parser.add_argument('-l','--latches',help='Number of latches', type=int, required=True)
    parser.add_argument('-o','--outputs',help='Number of output variables', type=int, required=True)
    parser.add_argument('-seeds','--seeds',help='list of seeds to be used for the random number generation', nargs='+', type=int, required=False)
    parser.add_argument('-oseed','--oseed',help='seed for the output function variables',type=int, required=False)
    parser.add_argument('-noABC','--noABC',help='stop ABC tool',type=int, default=0, required=False)
    
    args = parser.parse_args()
    if args.controllables <= 0 or args.uncontrollables <= 0 or args.latches <= 0 or args.outputs <= 0:
        sys.exit("Error: c,u,l,o must be greater than 0!")
    if args.outputs > args.latches :
        sys.exit("Error: Number of outputs variables must be smaller or equal to number of latches!")
    if args.seeds is not None and len(args.seeds) > 0 and len(args.seeds) > (args.latches + 1):
        sys.exit("Error: Number of seeds must be equal to l+1")    
    fileName = args.outputFile
    c_nb = args.controllables
    u_nb = args.uncontrollables
    latches_nb = args.latches
    var_nb = c_nb + u_nb + latches_nb
    input_nb = c_nb + u_nb
    top_var_index = var_nb
    outVarnb = args.outputs
    inputSeeds = args.seeds
    noABC = args.noABC
    oseed = args.oseed
    
    if inputSeeds is not None and len(inputSeeds) != (latches_nb + 1):
        sys.exit("Number of seeds must be equal to l + 1")
    # top(max) var index represents also the number of variables
    
    startTime = int(round(time.time() * 1000))
    fctIDs, outfctID, bdd_tuple, out_bdd_tuple, seeds = GenerateBDDs.generate_latches_fct(var_nb, latches_nb, outVarnb, top_var_index, input_nb, inputSeeds)
    print (len(bdd_tuple))
    print (len(out_bdd_tuple))
    convertToAiger.conertToAiger(fileName, u_nb, c_nb, var_nb, latches_nb, outVarnb, top_var_index, fctIDs, outfctID,seeds,oseed, bdd_tuple, out_bdd_tuple)
    print (fileName + ': ', int(round(time.time() * 1000)) - startTime)
    if noABC == 0:
        from shutil import copyfile
        abcFileName = os.path.splitext(fileName)[0] +'_abc.aag'
        copyfile(fileName, abcFileName)
        ABCMinimization.minimize(abcFileName)
        print (fileName + '_abc: ', int(round(time.time() * 1000)) - startTime)