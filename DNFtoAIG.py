"""
Created on Wed Sep 30 15:43:00 2020

@author: msakr
"""
import time
import sys
import random
import os
import collections
import math
import ABCMinimization


andGatesDNF = []
sys.setrecursionlimit(2147483647)  #this is the maximum possible: 2^31 - 1(signed integer)
maxDNFLit = 0  # maximum literal in the aig literals
outVarseedVars = [] # to store the selected variables in the output function
########################Converting BDD to AIG ##################################
#levelIndex starts with 1
def getDNFAIGVarIdx(levelIndex, input_nb):
    #print("index: ", levelIndex, "return", 2 * int(levelIndex + 1))
    return 2 * int(levelIndex + 1)

def getDNFAIGVarIdx_out(levelIndex,input_nb):
    # we need to add the input_nb as outpit function has no input vars
    #print("index_out: ", levelIndex, "return", 2 * (int(levelIndex + 1) + input_nb))
    return 2 * (int(levelIndex + 1) + input_nb)  # level 0 contains 0 and 1


def getDNFAIGVarIdx_out_random(levelIndex,input_nb):
    return 2 * (outVarseedVars[int(levelIndex)] + input_nb)  # level 0 contains 0 and 1

def negateAIG_lit(aig_lit):
    return aig_lit ^ 1

def DNF_next_lit():
    """ :return: next possible literal """
    return (maxDNFLit) + 2

def createDNFAndGate(ag1,ag2,andGatesDNF,andGatesDNFMap):
    global maxDNFLit
    mapKey = str(ag1) + "-" + str(ag2)
    mapKey2 = str(ag2) + "-" + str(ag1)
    if mapKey in andGatesDNFMap:
        return andGatesDNFMap[mapKey]
    elif mapKey2 in andGatesDNFMap:
        return andGatesDNFMap[mapKey2]
    else:
        ag1_ag2_lit = DNF_next_lit()
        andGatesDNF.append((ag1_ag2_lit, ag1, ag2))
        maxDNFLit = ag1_ag2_lit
        andGatesDNFMap[mapKey] = ag1_ag2_lit
        return ag1_ag2_lit
        
  

def bitVecToANDGATE(bitVec, getAIGVarLiteral, input_nb, andGatesDNF,andGatesDNFMap):
    FAGID = -1 #Final AndGate ID
    for i in range(0, len(bitVec)):
        tempID = getAIGVarLiteral(i, input_nb)
        if bitVec[i] == 0:
            tempID += 1
        if FAGID == -1:
            FAGID = tempID
        else:
            FAGID = createDNFAndGate(FAGID, tempID, andGatesDNF,andGatesDNFMap)
    return FAGID # if all bits are zero it will return 0

def generate_DNF_latch_fct(bitVec, var_nb, getAIGVarLiteral, input_nb, andGatesDNF,andGatesDNFMap):
    FAGID = -1
    FinalFAGID = -1
    counter = 0
    tempEndGates = []
    moreThanOne = False
    for i in range(0, len(bitVec)):
        if bitVec[i] == 1:
            ibitVec = ("{0:0" + str(var_nb) +"b}").format(i)
            dnfClause = [int(ibitVec[idx : idx + 1]) for idx in range(0, len(ibitVec), 1)]
            andGateID = bitVecToANDGATE(dnfClause, getAIGVarLiteral, input_nb, andGatesDNF,andGatesDNFMap)
            andGateID = andGateID + 1 #DNF so we need to negate it
            if FAGID == -1:
                FAGID = andGateID 
            else:
                FAGID = createDNFAndGate(FAGID, andGateID, andGatesDNF,andGatesDNFMap)
            counter = counter + 1
            if not moreThanOne and counter > 0:
                moreThanOne = True
            if counter == 100000:
                counter = 0
                tempEndGates.append(FAGID)
                FAGID = -1

    if len(tempEndGates) > 1:
        for ag in tempEndGates:
            if FinalFAGID == -1:
                FinalFAGID = ag
            else:
                FinalFAGID = createDNFAndGate(FinalFAGID, ag, andGatesDNF,andGatesDNFMap)
    elif len(tempEndGates) > 0:
        FinalFAGID = tempEndGates[0]
    else:
        FinalFAGID = FAGID
    if(FinalFAGID != FAGID and FAGID > -1):
        FinalFAGID = createDNFAndGate(FAGID, FinalFAGID, andGatesDNF,andGatesDNFMap)
    #print("******************************************")
    if moreThanOne:
        return FAGID + 1 #DNF so we need to negate it
    if FAGID == -1:
        return 0
    return FAGID

def get_DNF_aiger_input(input_nb):
    input_list = []
    level = 0
    while level < input_nb:
        input_list.append(getDNFAIGVarIdx(level, input_nb))
        level +=1
    return input_list

def create_DNF_aiger_file(fileName, u_nb, c_nb,latches,seeds,oseed,outfctID, andGatesDNF, maxLit,input_list):
    content = input_list
    #laches
    for l in latches:
        content.append(str(l) + ' ' + str(latches[l]))
    #end of latches
    content.append(outfctID)
    #and gates
    for ag in andGatesDNF:
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
        + str(len(latches)) + ' 1 ' + str(len(andGatesDNF))
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
    return len(andGatesDNF)
    
def generate_DNF_aiger(fileName, u_nb,c_nb, latches_nb, inputSeeds, outVarnb, outVarseed):
    global maxDNFLit
    andGatesDNF=[]
    andGatesDNFMap = dict()
    var_nb = u_nb + c_nb + latches_nb
    input_nb = u_nb + c_nb
    maxDNFLit = getDNFAIGVarIdx(var_nb - 1, input_nb)
    seeds = [] # to save the used seeds    
    input_list = get_DNF_aiger_input(u_nb + c_nb)
    nb = latches_nb
    latches = collections.OrderedDict()  #latch lit --> fct lit
    latch_lit = getDNFAIGVarIdx(var_nb - latches_nb, input_nb)
    fctIDs = []  
    while nb > 0:
        #generate a random number that corresponds to a unique boolean function.
        #top_var_index is the number of variables
        if(inputSeeds is None or len(inputSeeds) == 0 or len(inputSeeds) < len(seeds)):
            milli_sec = int(round(time.time() * 1000000))
            seeds.append(milli_sec)
            random.seed(milli_sec)
        else:
            currentSeed = inputSeeds[len(seeds)]
            seeds.append(currentSeed)
            random.seed(currentSeed)
        
        exp_n = int(math.pow(2, var_nb))
        charBitVec = ("{0:0" + str(exp_n) +"b}").format(random.getrandbits(exp_n))
        bitVect = [int(charBitVec[idx : idx + 1]) for idx in range(0, len(charBitVec), 1)] 
        fctID = generate_DNF_latch_fct(bitVect, var_nb, getDNFAIGVarIdx, input_nb, andGatesDNF,andGatesDNFMap)
        fctIDs.append(fctID)
        latches[latch_lit] = fctID
        latch_lit += 2
        nb -= 1        
    ########## Generate Output fct  ##############
    if(inputSeeds is None or len(inputSeeds) == 0 or len(inputSeeds) < len(seeds)):
           milli_sec = int(round(time.time() * 1000000))
           seeds.append(milli_sec)
           random.seed(milli_sec)
    else:
       currentSeed = inputSeeds[len(seeds)]
       seeds.append(currentSeed)
       random.seed(currentSeed)
    exp_n = int(math.pow(2, outVarnb))
    charBitVec = ("{0:0" + str(exp_n) +"b}").format(random.getrandbits(exp_n))
    bitVect = [int(charBitVec[idx : idx + 1]) for idx in range(0, len(charBitVec), 1)]
    ### Generate a random number for the variables to be picked to be part of
    ## the function, the remaining variables will be set to 1
    needRandom = (latches_nb - outVarnb) != 0
    tempOutID = -1
    if needRandom:
        if(outVarseed is None or outVarseed == 0):
            outVarseed = int(round(time.time() * 1000000))
            random.seed(outVarseed)
        else:
            random.seed(outVarseed)
        global outVarseedVars
        latchesRange = range(1, latches_nb + 1)
        outVarseedVars = random.sample(latchesRange, outVarnb)[:]
        #outVarseedVars.insert(0,-1)#this as levelindex starts from 1
        tempOutID = generate_DNF_latch_fct(bitVect, outVarnb, getDNFAIGVarIdx_out_random, input_nb,andGatesDNF,andGatesDNFMap)
    else:
        tempOutID = generate_DNF_latch_fct(bitVect, outVarnb, getDNFAIGVarIdx_out, input_nb,andGatesDNF,andGatesDNFMap)
        #The convertToAndGate function here takes as argument the function
        #"getDNFAIGVarIdx_out" instead of "getDNFAIGVarIdx" as the indices in the output
        #functions should be only latches indices.
    #compute the cube of the remiaining variables of the latches if any
    if needRandom:
       for j in latchesRange:
           if j not in outVarseedVars:
               #j-1 as outVarseedVars is 1 indexed
               tempOutID = createDNFAndGate(tempOutID, getDNFAIGVarIdx_out(j - 1, input_nb),andGatesDNF,andGatesDNFMap)
    outfctID = tempOutID
    return create_DNF_aiger_file(fileName, u_nb,c_nb,latches,seeds,outVarseed,outfctID, andGatesDNF, maxDNFLit,input_list)
    #return fctIDs, seeds, outfctID, outVarseed, input_list, latches
            

#fctIDs, seeds = generate_DNF_latches_fct(4,2,[1601631965876384,1601631965877135])
#u_nb = 8
#c_nb = 8
#latches_nb = 2
#outVarnb = 2
#fileName = "testDNF.aag"
#generate_DNF_aiger(fileName,c_nb,u_nb,latches_nb,None,outVarnb,None)
#fctIDs, seeds, outfctID, outVarseed,  input_list, latches = generate_DNF_latches_fct(u_nb,c_nb,l_nb,None,o_nb,None)
#create_DNF_aiger(fileName, u_nb,c_nb,latches,seeds,outVarseed,outfctID, andGatesDNF, maxDNFLit,input_list)

