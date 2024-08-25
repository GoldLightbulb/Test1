# unpacking is the feature where you ad variable names in front of an equal sign and the specific variable you want to unpack


# unpacking a list is compatable, but you'll need to point out how many variables are associated with how many indexes are in the simple list
# so a holds 1, bholds 2, and c holds 3
simple_list = [1, 2, 3]
a, b, c = simple_list

# in the case of sets, list comphresneion is supported
new_set = {'tom', 'hill', 1}
[el for el in new_set]
