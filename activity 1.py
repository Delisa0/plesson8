my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

my_tuple=(1,"hello",3.4)
print(my_tuple)

my_tuple = ("mouse",[8,6,5],(91,2,8))
print(my_tuple)

my_tuple=('y','t','r','e','w','q')
print(my_tuple[3])
print(my_tuple[1])

n_tuple=("mouse",[8,4,6],(1,2,3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print("sliced:", my_tuple[1:3])

for letter in (my_tuple):
    print("hello", letter)