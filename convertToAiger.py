import time
import sys
import random
import os
import collections

sys.setrecursionlimit(2147483647)  #this is the maximum possible: 2^31 - 1(signed integer)
maxLit = 0  # maximum literal in the aig literals
oseedVars = [] # to store the selected variables in the output function
########################Converting BDD to AIG ##################################
#levelIndex starts with 1
def getAIGVarIdx(levelIndex, input_nb):
    return 2 * int(levelIndex)  # level 0 contains 0 and 1

def getAIGVarIdx_out(levelIndex,input_nb):
    return 2 * (int(levelIndex) + input_nb)  # level 0 contains 0 and 1

def getAIGVarIdx_out_random(levelIndex,input_nb):
    return 2 * (oseedVars[int(levelIndex)] + input_nb)  # level 0 contains 0 and 1

def negateAIG_lit(aig_lit):
    return aig_lit ^ 1

def next_lit():
    """ :return: next possible literal """
    return (maxLit) + 2

def createAndGate(a_lit, b_lit,andGates):
    global maxLit
    if a_lit == 0 or b_lit == 0:
        return 0
    if a_lit == 1 and b_lit == 1:
        return 1
    if a_lit == 1:
        return b_lit
    if b_lit == 1:
        return a_lit
    if a_lit > 1 and b_lit > 1:
        a_b_lit = next_lit()
        andGates.append((a_b_lit, a_lit, b_lit))
        maxLit = a_b_lit
        return a_b_lit



def convertToAndGate(bdd_id, get_aig_lit, bdd_tuple, input_nb, andGates, bdd_to_lit):
    if bdd_id == 1 or bdd_id == 2:
        return bdd_id - 1
    level, left, right = bdd_tuple[bdd_id]
    x = get_aig_lit(level, input_nb)  # bdd root variable
    #check if it is in cache first
    # bdd else fct
    x_e = -1
    if left in bdd_to_lit:
        x_e = bdd_to_lit[left]
    else:
        x_e = convertToAndGate(left, get_aig_lit, bdd_tuple, input_nb, andGates, bdd_to_lit)
    #check if it is in cache first
    # bdd then fct
    if right in bdd_to_lit:
        x_t = bdd_to_lit[right]
    else:
        x_t = convertToAndGate(right, get_aig_lit, bdd_tuple, input_nb, andGates, bdd_to_lit)
    # f = x*x_t + !x*x_e
    # f = !(!(x*x_t) * !(!x*x_e))
    nx = negateAIG_lit(x)
    x_x_t = createAndGate(x, x_t,andGates)
    nx_x_e = createAndGate(nx, x_e, andGates)
    neg_x_x_t = negateAIG_lit(x_x_t)
    neg_nx_x_e = negateAIG_lit(nx_x_e)
    temp = createAndGate(neg_x_x_t, neg_nx_x_e, andGates)
    f = negateAIG_lit(temp)
    bdd_to_lit[bdd_id] = f
    return f

def get_aiger_input(input_nb):
    input_list = []
    level = 1
    while level <= input_nb:
        input_list.append(getAIGVarIdx(level, input_nb))
        level +=1
    return input_list

#u_nb : number of uncontrollable input
#c_nb : number of controllable input
#aiger format: header - c_inpt - u_inpt - latches - output - andgates - var_desc
def internal_create_aiger(fileName, u_nb, c_nb,latches,seeds,oseed,output_lit, andGates):
    global maxLit
    input_list = get_aiger_input(u_nb + c_nb)
    content = input_list
    #laches
    for l in latches:
        content.append(str(l) + ' ' + str(latches[l]))
    #end of latches
    content.append(output_lit)
    #and gates
    for ag in andGates:
        content.append(str(ag[0]) + ' ' + str(ag[1]) + ' ' + str(ag[2]))
    #end of and gates
    #var description
    count = 0
    var_desc = []
    c_inputs = input_list[:c_nb]
    for c in c_inputs:
        var_desc.append('i' + str(count) + ' controllable_c_' + str(count))
        count += 1
    u_inputs = input_list[-u_nb:]
    for u in u_inputs:
        var_desc.append('i' + str(count) + ' u_' + str(count))
        count += 1
    count = 0
    for l in latches:
        var_desc.append('l' + str(count) + ' l_' + str(count))
        count += 1
    var_desc.append('o0' + ' err')
    content.extend(var_desc)
    #end of var description
    #header
    header = 'aag ' + str(int(maxLit/2)) + ' ' + str(u_nb + c_nb) + ' ' \
        + str(len(latches)) + ' 1 ' + str(len(andGates))
    content.insert(0, header)
    #end of header
    fileOb = open(fileName, 'w+')
    for i in range(len(content)):
        fileOb.write(str(content[i]) + os.linesep)
    #writing comments
    fileOb.write('c' + os.linesep)
    for i in range(len(seeds) - 1):
        fileOb.write('latch ' + str(i) + ' seed: ' + str(seeds[i]) + os.linesep)
    fileOb.write('output ' + str(len(seeds) - 1) + ' seed: ' + str(seeds[len(seeds) - 1]) + os.linesep)
    fileOb.write('output vars seed: ' + str(oseed) + os.linesep)
    fileOb.close()

def conertToAiger(fileName, u_nb, c_nb, var_nb, latches_nb, outVarnb, top_var_index, fctIDs, outfctID, seeds, oseed, bdd_tuple, outbdd_tuple):
    global maxLit
    
    bdd_to_lit = dict()  # holds the aig literals of the bdds bdd_ID --> aig_lit
    andGates = []  # list of tuples (ag left right)
    input_nb = c_nb + u_nb
    maxLit = getAIGVarIdx(top_var_index, input_nb)
    latches = collections.OrderedDict()  #latch lit --> fct lit
    output_lit = 0  # output fct literal
    latch_lit = getAIGVarIdx(var_nb - latches_nb + 1, input_nb)
    for fctID in fctIDs:
        #fctID maps to a tuple (index,left,right) in the list bdd_tuple
        fct_lit = convertToAndGate(fctID, getAIGVarIdx, bdd_tuple, input_nb, andGates, bdd_to_lit)
        #bdd_tuple.clear()
        latches[latch_lit] = fct_lit
        latch_lit += 2
    
    bdd_to_lit.clear()
    out_bdd_to_lit = dict()
    #output_lit = generateConfigurableOutput(input_nb, latches_nb, outVarnb)
    #handle output
    needRandom = (latches_nb - outVarnb) != 0
    if needRandom:
        if(oseed is None or oseed == 0):
            oseed = int(round(time.time() * 1000000))
            random.seed(oseed)
        else:
            random.seed(oseed)
        global oseedVars
        oseedVars = random.sample(range(1, latches_nb + 1), outVarnb)[:]
        oseedVars.insert(0,-1)#this as levelindex starts from 1
        output_lit = convertToAndGate(outfctID, getAIGVarIdx_out_random, outbdd_tuple, input_nb, andGates, out_bdd_to_lit)
    else:
        output_lit = convertToAndGate(outfctID, getAIGVarIdx_out, outbdd_tuple, input_nb, andGates, out_bdd_to_lit)
        #The convertToAndGate function here takes as argument the function
        #"getAIGVarIdx_out" instead of "getAIGVarIdx" as the indices in the output
        #functions should be only latches indices.

    #compute the cube of the remiaining variables of the latches if any
    cubeSize = latches_nb - outVarnb
    if cubeSize > 0:
        counter = 0
        while outVarnb + counter < latches_nb:
            output_lit = createAndGate(output_lit, getAIGVarIdx_out(outVarnb + counter +1, input_nb), andGates)
            counter += 1
    internal_create_aiger(fileName, u_nb, c_nb,latches,seeds,oseed,output_lit,andGates)
