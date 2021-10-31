import statistics
nums = [[1, 2, 6], [7, 8, 9], [100, 5, 2]]
print([max(sub_list) for sub_list in nums])
print(([min(sub_list) for sub_list in nums]))
print([(sub_list , f'avg={statistics.mean(sub_list)}') for sub_list in nums])