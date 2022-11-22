# Assemble
# Act
# Assert

from MiniProject4 import view_list, adding_to_list, renaming_list_via_index, remove_entry
from unittest.mock import patch
# 1. View
def test_viewing_product_list_with_index():
    # Assemble
    a_list_of_dicts = [{"name":"Numan","surname":"Mahmood"},{"name":"Is","surname":"Testing"}]
    # Act
    actual = view_list(a_list_of_dicts,"name","surname")
    expected = '0| Numan: Mahmood\n1| Is: Testing\n'
    # Assert
    assert actual == expected

# 2. Add
def test_add_product_to_list():
    # Assemble
    product_name = "Cola"
    product_cost = "0.6"
    products_list = []

    # Act
    actual = adding_to_list(product_name,product_cost,products_list,float,"Name","Cost")
    expected = [{"Name": "Cola", "Cost": 0.6}]
    # Assert
    assert actual == expected

# 3. Renaming
# # Test Case: 2 inputs
@patch('builtins.input',side_effect=['Chocolate',0.3])
def test_renaming_list_items(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2,},{"Name": "Croissant","Cost": 0.9,}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Chocolate","Cost": 0.3,},{"Name": "Croissant","Cost": 0.9,}]
    # Assert
    assert actual == expected

# # Test Case: 1 input
@patch('builtins.input',side_effect=['',1.3])
def test_renaming_list_items_with_one_empty_input(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Muffin","Cost": 1.3},{"Name": "Croissant","Cost": 0.9}]
    # Assert
    assert actual == expected

# # Test Case: 0 input
@patch('builtins.input',side_effect=['',''])
def test_renaming_list_items_with_two_empty_inputs(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    # Assert
    assert actual == expected
    assert mock_input.call_count == 2 
    
# 4. Remove
@patch('builtins.print')
@patch('builtins.input', side_effect = "3")
def test_removing_entry_from_list(mock_print,mock_input):
    # Assemble
    title_of_menu = 'Person'
    a_list_of_dicts = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"},
    {"Name":"Q","Number":"08793982173"}]
    
    # Act
    actual = remove_entry(title_of_menu,a_list_of_dicts)
    expected = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"}]

    # Assert
    assert actual == expected

# Test 2 

@patch('builtins.input', side_effect = "3")
@patch('builtins.print')
def test_print_removing_entry_from_list(mock_print,mock_input):
    # Assemble
    title_of_menu = 'Person'
    a_list_of_dicts = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"},
    {"Name":"Q","Number":"08793982173"}]
    
    # Act
    remove_entry(title_of_menu,a_list_of_dicts)
    
    # Assert
    mock_print.assert_called_with('\nPerson no. 3 has been removed.')
    