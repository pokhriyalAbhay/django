# Initial tuple with integers, decimals, and strings
initial_tuple = (1, 2.5, 'hello', 3, 4.8, 'world', 7, 9.1)
# Step 2: Convert the tuple to a list
temp_list = list(initial_tuple)
# Step 3: Filter out all decimal values
filtered_list = [item for item in temp_list if not isinstance(item, float)]
# Step 4: Add three new character string values
filtered_list.extend(['a', 'b', 'c'])
# Step 5: Convert the list back to a tuple
modified_tuple = tuple(filtered_list)
# Print the final modified tuple
print(modified_tuple)