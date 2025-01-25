# print out list of items sepearted by a coma
def print_list_items(list):
    last_item = len(list) -1
    list_items = ''
    for index, item in enumerate(list):
        if index == last_item:
            list_items += f"and {item}"
        else:
            list_items += f"{item}, "
    
    print(list_items)

spam = ["apples", "bananas", "tofu", "cats"]
print_list_items(spam)