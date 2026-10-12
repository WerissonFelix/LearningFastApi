''' 

Generic types are types that can take type parameters, like list[str]

'''

def process_items(items: list[int]):
    for item in items:
        print(item)

'''  
That means: The variable items is a list, and each of items in this list is a int.

And the editor can provide support even while processing items from the list
'''

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

""" 
This means the variable items_t is a tuple with 3 items, two int and one str

and the variable items_s is a set and each of its items is of type bytes

"""

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

''' 

This means the variable prices is a dict and the keys are of type str, 
and the values are of type float

We can declare several types for a variable, using |

That means the variable can be any of several types
'''


def process_item(item: int | str): # item can be an int or an str 
    print(item)
    
def say_hi(name: str | None = None): # item can be an str or an None.
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")

