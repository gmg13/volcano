import heapq

# let's try and create something, a function, which is able to generate
# selection runs for a large input sequence
# 
# Some points to consider
# 1. How do we do the memory management? In particular do we know in 
#    which memory would the heap be allocated? heap or stack?
# 2. We will need to parallely merge the selections, with py
#    the only way to do that is to use processpool
# 3. continuing on memory management issue, how do we enable optimistic
#    predictive buffering of memory? How do induce python runtime?
# 4. 
def replsel():
    pass