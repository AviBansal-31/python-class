# week2-notes
# python week2-notes.py


# array index print
test_string = "hello world"
print(test_string)
# hell
print('"{0}"'.format(test_string[0:4]))
#hell
print('"{0}"'.format(test_string[:4]))
#hello world
print('"{0}"'.format(test_string[0:]))
#hello world
print('"{0}"'.format(test_string[:]))
#ello worl
print('"{0}"'.format(test_string[1:10]))
#hello worl
print('"{0}"'.format(test_string[:10]))
#hello worl
# except the last one
print('"{0}"'.format(test_string[:-1]))
#hello wo
# excpet rld
print('"{0}"'.format(test_string[0:-3]))
#d
print('"{0}"'.format(test_string[-1:]))
#""
print('"{0}"'.format(test_string[-3:3]))

# conditional 
name = input('please enter your name:')
if len(name) > 5:
	print ('your name is too long!')
else:
	print('your name is too short!')
print("------------------------")
if len(name) > 10 and name[:1].lower() == 'j':
    print("your name is really long")
elif len(name) > 5 or name[0].lower() =='j':
    print ('your name is too long!')
else:
    print('your name is too short')


# oepration boolean
a = None
b = ''
print("{} is {}:{}".format(a, a, a is a))
print("{} == {}:{}".format(a, a, a == a))
print("{} is {}:{}".format(a, b, a is b))
print("{} is {}:{}".format(a, b, a is not a))
print("{} != {}:{}".format(a, b, a != a))

a= "abc"
b = "abcd"
print("{} is {}:{}".format(a, b, a is b))
print("{} == {}:{}".format(a, b, a == b))
print("{} == {}:{}".format(a, b[:3], a == b[:3]))

a= "[1,2,3]"
b = "[1,2,3,4]"
print("{} is {}:{}".format(a, b, a is b))
print("{} == {}:{}".format(a, b, a == b))
print("{} == {}:{}".format(a, b[:3], a == b[:3]))
print("{} is {}:{}".format(a, b[:3], a is b[:3]))
