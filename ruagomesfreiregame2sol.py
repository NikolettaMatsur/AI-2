import random
import numpy
from math import inf

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment
class LearningAgent:

        # init
        # nS maximum number of states
        # nA maximum number of action per state
        def __init__(self,nS,nA):

                # define this function
                self.nS = nS
                self.nA = nA
                self.epsilon = 1
                self.qstates = list()
                self.visited = list()
                for _ in range(nS+1):
                        actions = list()
                        visits = list()
                        for _ in range(nA):
                                actions.append(-inf)
                                visits.append(0)
                        self.qstates.append(actions)
                        self.visited.append(visits)
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                a = 0
                if random.uniform(0,1) > self.epsilon: 
                        a = numpy.argmax(self.qstates[st][0:len(aa)])
                else:
                        if self.epsilon > 0.3:
                                self.epsilon -= 0.001
                        a = numpy.argmin(self.visited[st][0:len(aa)])
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                a = numpy.argmax(self.qstates[st][0:len(aa)])
                return a

        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                alfa = 0.35 #learning rate - stochastically small
                gamma = 0.9 #discount - typically from 0.8 to 0.99
                qold = self.qstates[ost][a]
                self.visited[ost][a] += 1
                maxstates = max(self.qstates[nst])
                if maxstates == -inf:
                        maxstates = 0

                if qold == -inf:
                        qnew = alfa * (r + gamma * maxstates)
                else: 
                        qnew = qold + alfa * (r + gamma * maxstates - qold)
                self.qstates[ost][a] = qnew
                return
