books["book 0"] = "fantastic beasts"
output_dictionary_sorted(books)
books["book 3"] = "best one"
output_dictionary_sorted(books)
del books["book 0"]
output_dictionary_sorted(books)
students = {}
students[0] = {"name":"josh", "major":"cs"}
students[1] = {"name":"jill","major":"chem","email":"abc@ksu.com"}
students[2] = "a test"
students["test"] = "just a value"
output_dictionary(students)
students[0]['email']="wss@ksu.com"
output_dictionary(students)
my_list = [x for x in range(10) if x %2 ==0]
output_list(my_list)
output_list(my_list)
output_list(my_list[:2])
output_list(my_list[2:])
my_list[2:] = [x for x in range(10,20) if x %2 ==0]
output_list(my_list)
my_list[1:3] = [x for x in range(10,20) if x %2 ==0]
output_list(my_list)
my_list = [x+y for x in range(10,20,30) for y in range(20,40,60)]
output_list(my_list)
my_list = []
for x in [10,20,30]:
    for y in in [20,40,60]:
        my_list.append(x+y)
my_list = [x+y for x in [m for m in range(10,31,10)]
                for y in [m ofr m in range(20,61,20)]]
output_list(my_list)



from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
noprime = [j for i in range(2,sqrt_n) for j in range(i*2,n,i)]
primes = [x for x in range(2,n) if x ont in noprime]
output_list(noprime)
