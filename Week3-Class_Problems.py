
# coding: utf-8

# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one

# In[19]:

aTup=((13,5,1,11,15))
def oddTuples(aTup):
    nums=()
    for i in range(0,len(aTup),2):
        nums= nums+(aTup[i],)
    return(nums)
oddTuples(aTup)    
        


# In[20]:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
testList = [1, -4, 8, -9]        


# In[27]:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
testList = [1, -4, 8, -9]
def timesFive(a):
    return a + 1
applyToEach(testList,timesFive)  
print(testList)


# Write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary

# In[22]:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howmany(animals):
  
    A=sum(len(v) for v in animals.values())
    return(A)
howmany(animals)


# Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys

# In[34]:

aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}
def biggest(aDict):
    b=max(len(x) for x in aDict.values())
    for k,v in aDict.items():
        if len(aDict[k])==b:
            return (k)    
biggest(aDict)

