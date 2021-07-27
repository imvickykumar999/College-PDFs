try:
    print(col.Fore.RED)
    print("int operations" + col.Style.RESET_ALL)
except:
    print("int operations")

a = 3
print(type(a))

float_res = 3/2  # default division gives float
print(float_res)
print(type(float_res))

# convert float to int
float_to_int = int(float_res)
print(float_to_int)
print(type(float_to_int))

print('====================================================================================================')

try:
    print(col.Fore.RED)
    print("Float operations" + col.Style.RESET_ALL)
except:
    pass

flt = 3.14
print(type(flt))

# convert int to float
flt_2_int = float(3)
print(flt_2_int)
print(type(flt_2_int))


print('====================================================================================================')

try:
    print(col.Fore.RED)
    print("String operations" + col.Style.RESET_ALL)
except:
    pass

string = "Hello World!"

print('len of string is {}'.format(string.__len__()))
print('To upper ', string.upper())
print('To Lower ', string.lower())
print('To Title ', string.title())
print('Get index of \'ll\' in string ', string.find('ll'))



print('====================================================================================================')

try:
    print(col.Fore.RED)
    print('Complex Operations', col.Style.RESET_ALL)
except:
    pass

cmpx = 6j + 1
print(type(cmpx))

print("Imaginary : ", cmpx.imag)
print("Real : ", cmpx.real)
print("Cojugate : ", cmpx.conjugate())



print('====================================================================================================')

try:
    print(col.Fore.RED)
    print('List Operations', col.Style.RESET_ALL)
except:
    pass


lst1 = []
lst2 = []

# insert into
lst1.append(1)
lst1.append(2)

lst2.append(3)
lst2.append(4)

print('lst1', lst1)
print('lst2', lst2)

print('len of lst1', len(lst1))

# remove elements

lst1.pop()  # last item from lst1
lst2.remove(3)  # remove item 4 from lst2
print('lst1', lst1)
print('lst2', lst2)

# deletion
lst1.clear()  # empty list
print(lst1)

del lst2  # deleted from memory
try:
    print(lst2)  # will cause an error
except:
    print('lst2 deleted')



print('====================================================================================================')


try:
    print(col.Fore.RED)
    print('Tuple Operations', col.Style.RESET_ALL)
except:
    pass

tpl = (1,)

# Note : You can't perform any operaton wich modify original tuple as it is immutable
print('tuple', tpl)
print(len(tpl))



print('====================================================================================================')

try:
    print(col.Fore.RED)
    print('Dictionary Operations', col.Style.RESET_ALL)
except:
    pass


dict_ = {}

# assign value
dict_[1] = 5
dict_[2] = 3
dict_[3] = 8

# print keys
print(dict_.keys())
# print values
print(dict_.values())

# iterate through items
for item, val in dict_.items():
    print('{item} = {value}'.format(item=item, value=val))

# remove an entry
del dict_[1]
print(dict_)
