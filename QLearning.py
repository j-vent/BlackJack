import blackjack
from pylab import *
from numpy import *
import random

def policy(s):
    rew1,state = blackjack.sample(s,0)
    rew2,state = blackjack.sample(s,1)
    stc = rew1#reward for sticking
    hit = rew2 #reward for hitting
                
    if stc > hit : #reward for sticking> reward for hitting
        rd = 0
    elif stc < hit:
        rd = 1
    else:
        rd = random.randint(0,1)
    return rd,state
    

numEpisodes = 2000
returnSum = 0.0
epsilon = 0.0# act greedy 90% of the time, stochastically 10%
alpha = 0.001
 


A = [0,1]
S = range(-1,181)
q = {s:{a:0 for a in A} for s in S}  #-1,0,0 / -1,1,0 
counter = 0 
s = blackjack.init()
print("initial state: ", s)
p1 = q[s][0] #if this is only initial, it should only be done at the start 
p2 = q[s][1]
if(p1 > p2):
        rd = 0
else:
        rd = 1
for episodeNum in range(numEpisodes): 
    
    G = 0 #resets every ep
    
    while(s != -1):
        
        ''''
        x = random.random()
        if x < epsilon:
            rd = random.randint(0,1) 
        '''
            
            
        
        #reward, state = blackjack.sample(s, rd ) 
        reward,state = policy(s)
        print("reward:",reward)
        print("state", state)
        
        G = G + reward #return val: sum of all rewards in the episode
        s = state
        
        
        print("S",s)
        #print(q)
        print(q[s])
    
        maxQ = max(q[s][i] for i in q[s] )
        
        valQ = q[s][rd]
        valQ = valQ + alpha * (G + maxQ - valQ)
        
    
        print ("Episode: ", episodeNum, "Return: ", G)
    
    returnSum = returnSum + G
   
    if (counter)% 1000 == 0:                
        print("Average return: ", returnSum/numEpisodes)
    counter += 1
    
print("Average return:", returnSum/numEpisodes)

print(policy)
blackjack.printPolicy(policy)


#print ("Average return: ", returnSum/numEpisodes)               
#print("Average return: ", returnSum/episodeNum)


