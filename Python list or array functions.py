array1 = [ 11, 23,  31, 5, 29, 13, 19,  7, 2, 3]
print(array1)

menu = """
Please select one of the following option:

1. Add an element.
2. Insert an element.
3. Modify an element.
4. Delete an element.
5. Arrange in ascending order.
6. Arrange in descending order.
7. Exit

Your choice: """

def add_element():
    add = """Input element to be added:"""
    input_add = int(input(add))
    array1.append(input_add)
    print(array1)


def insert_element():
    insert_element = """Input element to be added:"""
    input_insert_element = int(input(insert_element))
    insert_pos = """Input position where the element would be added to:"""
    input_insert_pos = int(input(insert_pos))
    array1.insert(input_insert_pos, input_insert_element)
    print(array1)

def modify_element():
    modify_pos = """Input element position"""
    input_modify_pos = int(input(modify_pos))
    modify_new = """Input new element:"""
    input_modify_new = int(input(modify_new))
    array1[input_modify_pos] = input_modify_new
    print(array1)

def delete_element():
    delete_element = """Input element to be deleted:"""
    input_delete_element = int(input(delete_element))
    array1.remove(input_delete_element)
    print(array1)

def arrange_ascending():
    print("Elements arranged in ascending order.")
    array1.sort()
    print(array1)

def arrange_descending():
    print("Elements arranged in descending order.")
    array1.sort()
    array1.reverse()
    print(array1)

user_input = input(menu)

while user_input != "7":
            if user_input == "1":
                    add_element()
            elif user_input == "2":
                    insert_element()
            elif user_input == "3":
                    modify_element()
            elif user_input == "4":
                    delete_element()
            elif user_input == "5":
                    arrange_ascending()
            elif user_input == "6":
                    arrange_descending()
            else:
                    print("Invalid input, please try again.")
            user_input = input(menu)