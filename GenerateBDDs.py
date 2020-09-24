import time
import mpmath
import sys
import random




sys.setrecursionlimit(2147483647)  #this is the maximum possible: 2^31 - 1(signed integer)
""" Global variables """




""" End of Global variables """

def computeDelta(sbn, bddID):
    #delta = 4*sbn*sbn -4*bdd_ID + 1
    nsq = mpmath.power(sbn,2)
    fournsq = mpmath.fmul(nsq,4)
    fourk = mpmath.fmul(4, bddID)
    sub = mpmath.fsub(fournsq, fourk)
    return mpmath.fadd(sub, 1)

def compute_sublevel_start(sbn, sli):
    #sls = sbn + n + 2(n-1) + 2(n-2)...2(n-sli)
    #sls = sbn + 2 * sbn * sli - sli*(sli + 1)
    p1 = mpmath.fadd(sbn, mpmath.fmul(2, mpmath.fmul(sbn, sli)))
    p2 = mpmath.fmul(sli, mpmath.fadd(sli, 1))
    return mpmath.fsub(p1,p2)

def ComputeASol(sbn, sqrtdelta):
    #sli = math.ceil(((2*sbn - 1 - sqdelta)/2) - 1)
    #x_2 - 1 <= i < x_2...i.e. i = ceil(x_2 - 1)
    two_n = mpmath.fmul(2, sbn)
    two_n = mpmath.fsub(two_n, 1)
    sol = mpmath.fdiv(mpmath.fsub(two_n, sqrtdelta),2)
    result = mpmath.fsub(sol, 1)
    return mpmath.ceil(result)

def construct_bdd(bdd_ID, bdd_tuple):
    if bdd_ID > 2 and bdd_ID not in bdd_tuple:
        level, left, right = getChildren(bdd_ID)
        #print "result", level, left, right
        bdd_tuple[bdd_ID] = level, left, right
        if left > 2:            ###############put this and the below check in the getChildren methooooooooooooooooooooooooooooooooooood############################################################
            construct_bdd(left, bdd_tuple)
        if right > 2:
            construct_bdd(right, bdd_tuple)

start = False
mpmath.pretty = True
#....we have precision problem
def getChildren(bdd_ID):
    tempStr = str(bdd_ID)
    input_length = len(tempStr)
    tempIdx = tempStr.find("+")
    if tempIdx > 0:
        input_length += int(tempStr[tempIdx+1:])
    mpmath.mp.dps = 2 * input_length  #we multiply by 2 as at some point we compute the cube of the number
    #first we should figure out the root node (variable index or level)
    #level = ceil(log(log(bdd_ID)))
    level = mpmath.ceil(mpmath.log(mpmath.log(bdd_ID, 2), 2))
    prev_lvl = level - 1
    smaller_bdd_nb = mpmath.power(2, mpmath.power(2, prev_lvl))
    sbn = smaller_bdd_nb  # just as a short hand...n
    #first we need to figure out in which sublevel does this number exist
    #now to compute the sublevel index sli or "i" for short we need to compute i
    #such that the below hold:
    #f1=n + 2(n-1) + 2(n-2)...2(n-i) < bdd_ID < f2=n + 2(n-1) + 2(n-2)...2(n-(i+1))
    #which turn out to be true when the smaller solution(racine) of f1 i.e. x_2
    #x_2 - 1 <= i < x_2...i.e. i = ceil(x_2 - 1) as we need integer solution
    #note that n + 2(n-1) + 2(n-2)...2(n-i) = n +2ni - 2i(i+1)/2
    #delta of f1 = 4n^2-4k +1
    #delta of f1 = 4*sbn*sbn -4*bdd_ID + 1
    delta = computeDelta(sbn, bdd_ID)
    sqdelta = mpmath.sqrt(delta)
    #2n-1 - sqrt(delta)/2 -1
    #sli = math.ceil(((2*sbn - 1 - sqdelta)/2) - 1)#....we have precision problem
    sli = ComputeASol(sbn, sqdelta)
    #we have to add 1 as our IDs starts from 1 instead of 0
    node1 = mpmath.fadd(sli, 1)  #sublevel index
    sls = 0  # sublevel start
    #sls = sbn + n + 2(n-1) + 2(n-2)...2(n-sli)
    #sls = sbn + 2 * sbn * sli - sli*(sli + 1)
    sls = compute_sublevel_start(sbn, sli)
    in_sublvl_index = mpmath.fsub(bdd_ID, sls)
    node2 = mpmath.fadd(node1, mpmath.ceil(mpmath.fdiv(in_sublvl_index,2)))
    #because of the ordering nature if this number is divisable by 2 or not
    #we decide which node is on the right and which one on the left
    if(mpmath.frac(mpmath.fdiv(in_sublvl_index,2)) != 0):
        return level,node1,node2
    return level,node2,node1

"""
var_nb = latches_nb + inputnb(controllable and uncontrollable)
This function creates for every latch an AIG, and it ceates an AIG
for the output function
"""
def generate_latches_fct(var_nb, latches_nb, outVarnb, top_var_index,input_nb, inputSeeds):
    seeds = [] # to save the used seeds
    bdd_tuple = dict()  # bdd_ID --> (level, left, right)
    out_bdd_tuple = dict()
    nb = latches_nb
    fctIDs = []
    #generatedFcts = []
    #in an Aiger file the variables listing start with inputs then latches then
    #output. The first variable literal is 2. Therefore var_nb - latches_nb gives
    #the nb of inputs, so the first latch comes directly after the last input.
    #therefore we initialize latch_lit with the first latch literal
    
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
        randomNumber = random.getrandbits(mpmath.power(2, top_var_index)) + 1
        fctID = randomNumber
        #the below create a list (bdd_tuple) where each item is a tuple (index,left,right)
        #therefore it resembles bdd unique table, and it avoids building the same
        #bdd twice.
        construct_bdd(fctID, bdd_tuple)
        fctIDs.append(fctID)
        nb -= 1
    outfctID, out_bdd_tuple = generateConfigurableOutput(input_nb, latches_nb, outVarnb, inputSeeds, seeds)
    return fctIDs, outfctID, bdd_tuple, out_bdd_tuple, seeds

"""
This method generates a random boolean function for the output.
It is configurable in a way that "outVarnb" represents the number of variables
in the function. The remaining variables {latches variables}\{outVarnb} we be
added to cube that conjuncted with the function. This way we can minimize the
size of the error region as much as possible. However the drawback is that we
don't know if the error will be reachable.
"""

def generateConfigurableOutput(input_nb, latches_nb, outVarnb, inputSeeds, seeds):
    #here we have only outVarnb instead of top_var_index as we dont want
    #the inputs to be part of the output(just to make things a bit simple)
    #we need the +1 as our IDs starts from 1 instead of 0
    out_bdd_tuple = dict()  # bdd_ID --> (level, left, right)
    if(inputSeeds is None or len(inputSeeds) == 0 or len(inputSeeds) < len(seeds)):
           milli_sec = int(round(time.time() * 1000000))
           seeds.append(milli_sec)
           random.seed(milli_sec)
    else:
       currentSeed = inputSeeds[len(seeds)]
       seeds.append(currentSeed)
       random.seed(currentSeed)
    randomNumber = random.getrandbits(mpmath.power(2, outVarnb)) + 1
    fctID = randomNumber
    construct_bdd(randomNumber, out_bdd_tuple)
    return fctID, out_bdd_tuple



