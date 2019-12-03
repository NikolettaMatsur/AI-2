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
                self.qstates = list()
                self.visited = list()
                
                for _ in range(nS):
                        actions = list()
                        visits= list()
                        for _ in range(nA):
                                actions.append(float('-inf'))
                                visits.append(0)
                        self.qstates.append(actions)
                        self.visited.append(visits)


                # define this function


        #      self.qstates = [] * nS
                # self.visited = [] * nS
                # for i in range(nS):
                        # self.qstates.append([] * nA)
                        # self.visited.append([] * nA)
                        # for _ in range(nA):
                                # self.qstates[i].append(float('-inf'))
                                # self.visited[i].append(0)   
        
        # Select one action, used when learning  
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontolearn(self,st,aa):
                a = 0
                mod = False
                epsilon = 0.2
                if random.random() < epsilon: 
                        for action in range(len(aa)):
                                if self.qstates[st][action] > self.qstates[st][a]:
                                        a = action
                                        mod = True
                        if not mod:
                                a = random.randrange(len(aa))
                else:
                        a = random.randrange(len(aa))
                return a

        # Select one action, used when evaluating
        # st - is the current state        
        # aa - is the set of possible actions
        # for a given state they are always given in the same order
        # returns
        # a - the index to the action in aa
        def selectactiontoexecute(self,st,aa):
                a = 0
                for i in range(len(aa)):
                     if self.qstates[st][i] > self.qstates[st][a]:
                        a = i
                # print("select one action to see if I learned")
                return a

        # this function is called after every action
        # ost - original state
        # nst - next state
        # a - the index to the action taken
        # r - reward obtained
        def learn(self,ost,nst,a,r):
                alfa = 0.9 #learning rate - stochastically small
                gamma = 0.91 #discount - typically from 0.8 to 0.99
                qold = self.qstates[ost][a]
                if qold == float("-inf"):
                        qnew = alfa * (r + gamma * max(max(self.qstates[nst]),0))
                else: 
                        qnew = qold + alfa * (r + gamma * max(self.qstates[nst]) - qold)
                self.qstates[ost][a] = qnew
                return
