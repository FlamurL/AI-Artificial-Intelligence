if __name__ == '__main__':

    my_dic = {
        "Ana": "01/17/1991", 
        "Bob": "01/17/3333", 
        "David": "01/17/2022",  
        "Peter": "01/17/1111"
    }

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for key in my_dic.keys():
        print(key)

    i1 = input("Who's birthday do you want to know?\n")

    birthday = my_dic.get(i1)  
    if birthday:
        print(f"{i1}'s birthday is on {birthday}")
    else:
        print("We do not have information about this person's birthday.")
