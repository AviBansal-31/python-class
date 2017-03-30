def output(name, *stuff):
    print('hi, {}'.format(name))
    for i, value in enumerate(stuff):
        print('value {0}: {1}'.format(i, value))

output('j','dog',5,'cat','lery',867)
output('jim')

def output(name, *stuff, **named_stuff):
    print('hi, {}'.format(name))
    for i, value in enumerate(stuff):
        print('value {0}: {1}'.format(i, value))
    print("your items are")
# dictionary
    for i in named_stuff:
        print('value {0}: {1}'.format(i, named_stuff[i]))
output('josh',4,'cat','lol',3.14,animal='cat',color='dog')
