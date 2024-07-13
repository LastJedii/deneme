#!/usr/bin/env python
# coding: utf-8

# In[1]:


def flatten_list(nested_list):
    flat_list = []
    
    def flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                flatten(sub_item)
        else:
            flat_list.append(item)
    
    flatten(nested_list)
    return flat_list

# Örnek kullanım:
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten_list(input_list)
print(output_list)  # Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]


# In[2]:


def reverse_nested_list(nested_list):
    reversed_list = []
    
    for item in reversed(nested_list):
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    
    return reversed_list

# Örnek kullanım:
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested_list(input_list)
print(output_list)  # Çıktı: [[[7, 6, 5], [4, 3], [2, 1]]]


# In[ ]:




