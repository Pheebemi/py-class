# def add(a, b):
#     return a + b 
# print(add(1,2,3))

# def add(*args):
#     print(type(args))
# add(1,2,3)

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total 
# print(add(1,2,3,6))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name('dr', 'Emmanuel', 'Lemuel')

# def address(**kwargs):
#     print(type(kwargs))

# address(street="123", state="taraba", zip="12345" )
# def address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# address(street="123",
#          state="taraba", 
#          zip="12345" )


def shippin_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('state')} {kwargs.get('zip')}")

shippin_label("Dr.", "Emmanuel","Lemuel",
                street="123",
                state="taraba", 
                zip="12345")