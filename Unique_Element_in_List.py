def unique(l):
    uni = []
    for i in range(0,len(l)):
        if l[i] not in uni:
            uni.append(l[i])
    return uni

l = [12,3,2,4,3,2,12] 
print(unique(l))

# Using Set Theory:-

def get_unique_elements(lst):
    return list(set(lst))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_elements(sample_list)
print("Sample List:", sample_list)
print("Unique List:", unique_list)