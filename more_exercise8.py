string_list=["delhi","delhi","mumbai","delhi","chennai","chennai"]
index=0
new=[]
while index<len(string_list):
    if string_list[index]not in new:
        new.append(string_list[index])
    index=index+1
print new
