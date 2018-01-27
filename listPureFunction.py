a_k = ['banana', 'apple', 'pear', 'lemon']
def double_stuff(a_list):
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

b_k = double_stuff(a_k)
print(a_k)
print(b_k)
