#TASK
#Compute the sum and average value of all values inside the nested list

nested_list = [[10, 20], [30], [40, 50, 60], [], [10], [30, 40, 50, 60]]


def find_average(nested_list):
    total_sum = 0
    total_count = 0

    #sum up values and count number of elements
    for list in nested_list:
        total_sum += sum(list)
        total_count += len(list)


    #check if list is empty
    if total_count == 0:
        return total_count, None


    return total_sum, total_sum/total_count


total_sum, average = find_average(nested_list)


print(f"Total sum of values inside the nested list: {total_sum}")
print(f"Average of values inside the nested list: {average}")
