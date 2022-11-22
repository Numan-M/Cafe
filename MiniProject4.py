import csv
import os
# # 1. View
def view_list(viewed_list,*keys):
    print('')
    line = ''
    i = 0
    for items in viewed_list:
        line2 = f'{i}| {items[keys[0]]}: {items[keys[1]]}\n'
        i += 1
        line += line2
    return line

# # 2. Add
def adding_to_list(name,input_val,some_list,type,*keys):
    some_list.append({keys[0]: name.title(), keys[1]: type(input_val)})
    print(f'\n{name.title()} has been added. {keys[1]} has been set to {type(input_val)}.')
    return some_list

# # 3. Rename
def renaming_list_via_index(some_list,rename_index):
    some_list_copy = some_list[rename_index].copy()
    for key,value in some_list[rename_index].items():
        value = input(f'{key}: ' )
        if value == '':
            value = some_list_copy[f'{key}']
        some_list[rename_index].update({key: value})
    return some_list



# # 4. Remove
def remove_entry(menu_name,some_list):
    removal_index = int(input(f'Which {menu_name} would you like to remove?\n>> '))
    print(f'\n{menu_name} no. {removal_index} has been removed.')
    some_list.remove(some_list[removal_index])
    return some_list


def second_menu(menu_name,menu_output,some_list,type,*keys):
    # # 0. Return
    if menu_output == 0:
        return
    # # 1. View
    if menu_output == 1:
        listings = view_list(some_list,*keys)
        print(listings)
        return main_menu(main_menu_input)
    # # 2. Add
    if menu_output == 2:
        new_entry = input(f'Enter {menu_name} {keys[0]}\n>> ')
        new_entry_input = input(f'Enter {menu_name} {keys[1]}\n>> ')
        adding_to_list(new_entry,new_entry_input,some_list,type,*keys)
        return main_menu(main_menu_input) 
    # # 3. Rename
    if menu_output == 3:
        listings = view_list(some_list,*keys)
        print(listings)
        removal_index = int(input(f'Which {menu_name} would you like to rename?\n>> '))
        renaming_list_via_index(some_list,removal_index)
        return main_menu(main_menu_input) 
    # # 4. Remove
    if menu_output == 4:
        listings = view_list(some_list,*keys)
        print(listings)
        remove_entry(f'{menu_name}',some_list)
        return main_menu(main_menu_input) 
    else:
        print('\nInvalid option.')
        return main_menu(main_menu_input) 


# # 1. View
def orders_menu_view(orders):
    i = 0
    line = ''
    for _ in orders:
        line2 = f'''
{i}.
______________________________________________________________________
Customer Name: {orders[i]["customer_name"]}
Customer Address: {orders[i]["customer_address"]}
Customer phonenumber: {orders[i]["customer_phone"]}
Courier: {orders[i]["courier"]}
Order Status: {orders[i]["status"]}
Items: {orders[i]["items"]}
______________________________________________________________________'''

        i += 1
        line += line2
    return line
        
# # 2. New Order
def new_customer_order(orders):
    customer_name = input('Enter your name\n>>')
    customer_address = input('Enter your address\n>>')
    customer_number = input('Enter your number\n>>')
    customer_order_status = 'Preparing'

    view_list(products_list,"Name","Cost")
    customer_items = []
    print('\nEnter one product. Leave blank when you have chosen your products.')
    while True:
        customer_items_input=input(">>")
        customer_items.append(customer_items_input)
        if customer_items_input == '':
            customer_items.pop()
            break
    customer_items = ','.join(set(customer_items))
    
    view_list(couriers_list,"Name","Number")
    customer_courier_index = int(input('\nPlease pick from the available couriers.\n>>'))
    
    new_order = {
    "customer_name":customer_name, 
    "customer_address": customer_address,
    "customer_phone": customer_number,
    "courier": customer_courier_index,
    "status": customer_order_status,
    "items": customer_items
    }
    orders.append(new_order)
    return orders
# # 3. Update status
def update_status(orders,status):
    update_order_status_index = int(input('\nEnter order number:\n>> '))
    print('\nWhat would you like to update the order status to?\n')
    for option in enumerate(status):
        print(f'{option[0]}. {option[1]}')

    update_order_status = int(input('\n>> '))
    print(f'\nOrder status: \'{orders[update_order_status_index]["status"]}\' has been updated to \'{status[update_order_status]}\'.')
    orders[update_order_status_index]['status'] = status[update_order_status]
    return orders

def orders_menu(orders):
    orders_menu_input = int(input(f'\n--- Orders Menu ---\n\
0. Return\n\
1. View Orders\n\
2. New Order\n\
3. Update Order Status\n\
4. Update Existing Order\n\
5. Cancel Order\n\
>> ')) 
    cls()
    # 0. Return
    if orders_menu_input == 0:
        return

    # 1. View
    if orders_menu_input == 1:
        order_listings = orders_menu_view(orders)
        print(order_listings)
        return main_menu(main_menu_input)

    # 2. New order
    if orders_menu_input == 2:
        new_customer_order(orders)
        return main_menu(main_menu_input)

    # 3. Update status
    if orders_menu_input == 3:
        orders_menu_view(orders)
        update_status(orders,('Preparing','Ready for collection','Out for delivery','Complete'))
        return main_menu(main_menu_input)

    # 4. Update Order
    if orders_menu_input == 4:
        orders_menu_view(orders)
        renaming_list_via_index('Orders',orders)
        return main_menu(main_menu_input)

    # 5. Cancel
    if orders_menu_input == 5:
        orders_menu_view(orders)
        remove_entry('Order',orders)
        return main_menu(main_menu_input)

    else:
        print('Invalid option.')
        return main_menu(main_menu_input)

products_list = []
couriers_list = []
orders_list = []

def menu_input(menu_name):
    menu_output = int(input(f'--- {menu_name} Menu ---\n\
0. Return\n\
1. View {menu_name}\'s menu\n\
2. Add a {menu_name}\n\
3. Rename a {menu_name}\n\
4. Remove a {menu_name}\n\
>> '))
    cls()
    return menu_output
def read_file(filename,loading_list):
        with open (f'{filename}.csv','r' ) as f:
                reader=csv.DictReader(f,delimiter=',',skipinitialspace = True)
                for row in reader:
                        loading_list.append(row)
        return

def write_file(filename,loading_list):
        with open(f'{filename}.csv', 'w', newline='') as f:
                keys = loading_list[0].keys()
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(loading_list)
        return


def main_menu(main_input):
    if main_input == 0:
        write_file('products',products_list)
        write_file('couriers',couriers_list)
        write_file('orders',orders_list)         
        print('\nGoodbye!')
        exit()
    elif main_input == 1:
        while True:
            product_menu_output = menu_input('Product')
            second_menu('Product', product_menu_output, products_list,float, "Name", "Cost",)
            return
    elif main_input == 2:
        orders_menu(orders_list)
        return
    elif main_input == 3:
        while True:
            courier_menu_output = menu_input('Courier')
            second_menu('Courier', courier_menu_output, couriers_list,str, "Name", "Number")
            return
    else:
        print('\nInvalid option.')
        return


        

if __name__ == '__main__':
    cls = lambda: os.system('cls')
    read_file('products',products_list)
    read_file('couriers',couriers_list)
    read_file('orders',orders_list)
    cls()
    while True:
        main_menu_input = int(input('--- Main Menu ---\n\
0. Exit\n\
1. Product Menu\n\
2. Order Menu\n\
3. Courier Menu \n\
>> '))
        cls()
        main_menu(main_menu_input)
        
        