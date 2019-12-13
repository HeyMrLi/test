# def filter_list(l):
#     new_list = []
#     for index in l:
#         if index is int:
#             new_list.append(index)
#         return new_list
# #   'return a new list with the strings filtered out'

# print(filter_list([1,2,'a','b']),[1,2])
# print(filter_list([1,'a','b',0,15]),[1,0,15])
# print(filter_list([1,2,'aasf','1','123',123]),[1,2,123])

def is_square(n):
    # root = n ** (1/2)
    # print(root)
    # if (n**(1/2)) % 1 == 0:
    #     return True
    if n >= 0:
        return (n**0.5) % 1 == 0
    return False # fix me

    # return n >= 0 and (n**0.5) % 1 == 0

print(is_square(4))
print(is_square(1327898974))
