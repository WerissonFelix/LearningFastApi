''' 

The key here is the await. It tells Python that it has to wait for get_burgers(2)
to finish doing its thing before storing the results in burgers. With that, Python
will know that it can go and do something else in the meanwhile
(like receiving another request).

For await to work, it has to be inside a function that supports this asynchronicity.
To do that, you just declare it with async def:

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    return burgers
    
'''

# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    return 


''' 

With async def, Python knows that, inside that function, it has to be aware
of await expressions, and that it can "pause" ⏸ the execution of that function
and go do something else before coming back.

This won't work, because get_burgers was defined with: async def
burgers = get_burgers(2)


@app.get('/burgers')
async def read_burgers():
    burgers = await get_burgers(2)
    return burgers
    
note: We can only use await inside of functions created with async def.
'''
