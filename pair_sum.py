def pair_sum(list):
    index=0
    jar=-1
    while (index<len(list)/2):
        print(list[index]+list[jar])
        index=index+1
        jar=jar-1
pair_sum([3,4,6,2])
