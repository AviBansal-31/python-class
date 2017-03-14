def print_separator():     print("_________________________________________________________")
fruit = ["tomatoes", "apples", "mango", "bananas"] def output_list(my_list):
for i, item in enumerate(my_list):
print("{index}: {value}".format(index=i, value=item)) print("There was {} items in the list.".format(len(my_list)))
output_list(fruit) fruit.append("canteloup")
print_separator() output_list(fruit)
print_separator() fruit.append("tomatoes") #fruit.remove("tomatoes") fruit = list(filter(lambda item: item != 'tomatoes', fruit)) output_list(fruit)
print_separator() fruit.insert(3, 'bluberries') output_list(fruit)
print_separator()
number_list = [] for i in range(10):
number_list.append(i * 2)
output_list(number_list)
number_list = [i * 2 for i in range(10)] output_list(number_list)
del fruit[3] output_list(fruit) print_separator()
books = {  "Book 1": "Sorcerors Stone",          "Book 2": "Chamber of Secrets",          "Book 3": "Prisoner of Azkhaban",          "Book 4": "Goblet of Fire",          "Book 5": "Order of the Phoenix",          "Book 6": "Half Blood Prince",          "Book 7": "Deathly Hallows"         }
def output_dictionary(my_dict):
for key in my_dict:
print("{}: {}".format(key, my_dict[key]))
def output_dictionary_sorted(my_dict): for key in sorted(my_dict.keys()):
print("{}: {}".format(key, my_dict[key]))
def output_dictionary_sorted_value(my_dict):
for key in sorted(my_dict.keys(),key=lambda k: my_dict[k]):
print("{}: {}".format(key, my_dict[key]))
print_separator()


output_dictionary_sorted(books) print_separator() output_dictionary_sorted_value(books)
print_separator() books['Book 0'] = "Fantastic Beasts and Where to Find Them" output_dictionary_sorted(books)
print_separator() books['Book 3'] = "Best one out of the series" output_dictionary_sorted(books)
print_separator() del books['Book 0'] output_dictionary_sorted(books)
print_separator() students = {} students[0] = {'Name': 'Josh',
'Major': 'Computer Science'}
students[1] = {'Name': 'Jill',
'Major': 'Chemistry', 'Email': 'jill@test.edu'}
students[2] = 'This is just a test' students['Dummy'] = 'This is just a dummy value' output_dictionary(students) students[0]['Email'] = 'weeser@ksu.edu' print_separator() output_dictionary(students)
print_separator() my_list = [x for x in range(10) if x % 2 == 0] output_list(my_list) output_list(my_list[:2]) output_list(my_list[2:]) #my_list[2:] = [x for x in range(10, 20) if x % 2 == 0] #my_list[:2] = [x for x in range(10, 20) if x % 2 == 0] my_list[1:3] = [x for x in range(10, 20) if x % 2 == 0] output_list(my_list) print_separator()
my_list = [x + y for x in [10, 20, 30] for y in [20,40,60]] output_list(my_list) my_list = [] for x in [10, 20, 30]:
for y in [20,40,60]:
my_list.append(x + y)
output_list(my_list) print_separator()
my_list = [x + y for x in [m for m in range(10, 31, 10)]
for y in [m for m in range(20, 61, 20)]]
output_list(my_list) print_separator()
from math import sqrt n = 200 sqrt_n = int(sqrt(n)) noprime_old = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)] noprime = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)} primes = [x for x in range(2, n) if x not in noprime] output_list(primes) print(len(noprime_old)) print(len(noprime))

print_separator() my_list = [{'{},{}'.format(x,y): x + y} for x in [10, 20, 30] for y in [20,40,60]] output_list(my_list)
