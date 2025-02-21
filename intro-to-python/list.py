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
li.extend([15,22,44]) #[1, 2, 3, 4, 8, 5, 6, 7, 8, 9, 123, 15, 22, 44]
print(li)


#index gets u the index where that element is first found
print(li.index(1)) #0

#count counts how many times that element is found on the list
print(li.count(1)) #1

#remove =>removes the element on that list
li.remove(1)
print(li)  #[2, 3, 4, 8, 5, 6, 7, 8, 9, 123, 15, 22, 44]

#sort =>sorts the elements
#reverse => reverses the list
