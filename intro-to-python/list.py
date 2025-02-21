li = [1,2,3,4,5,6,7,8,9]

#append an element=> adds that element to the end of the list
li.append(123)
print(li) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 123]

#insert=>the first element is after which which element you want to add the second element inside the parenthesis
li.insert(4,8)
print(li) #[1, 2, 3, 4, 8, 5, 6, 7, 8, 9, 123]

#you can turn a tuple into a list and vise-versa
tu= (1,2,3,4,5)
print(list(tu)) #[1, 2, 3, 4, 5]

#extend is used in lists when you want to add more than 1 element to that list
li.extend([15,22,44]) 