import random

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
                self.qstates = [] * nS
                self.visited = [] * nS
                for i in range(nS):
                        self.qstates.append([] * nA)
                        self.visited.append([] * nA)
                        for _ in range(nA):
                                self.qstates[i].append(float('-inf'))
                                self.visited[i].append(0)
                # define this function
              
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                # define this function
                # print("select one action to learn better")
                a = 0
                mod = False
                for action in aa:
                        if self.qstates[st][action] < self.qstates[st][a]:
                                a = action
                                mod = True
                if not mod:
                        a = random.randrange(len(aa))
                # define this function
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                # define this function
                a = 0
                for i in range(aa):
                     if self.qstates[st][i] < self.qstates[st][a]:
                        a = i
                # print("select one action to see if I learned")
                return a

        def qlearning(self,state,action,nst,r):
                alfa = 0.1 #learning rate - stochastically small
                gamma = 0.91 #discount - typically from 0.8 to 0.99
                qnew = (1-alfa) * self.qstates[state][action] + alfa * (r + gamma * max(self.qstates[nst]))
                self.qstates[state][action] = qnew

        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                alfa = 0.1 #learning rate - stochastically small
                gamma = 0.91 #discount - typically from 0.8 to 0.99
                qnew = (1-alfa) * self.qstates[ost][a] + alfa * (r + gamma * max(self.qstates[nst]))
                self.qstates[ost][a] = qnew
                #print("learn something from this data")
                return
