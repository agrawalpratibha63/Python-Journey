#================================================================
                   #Day10 question Practice
#==============================================================

#Question1. Longest  unique substring.
#A data scientist is analyzing text streams and needs to determine the longest substring without repeating characters
s=input("enter the string")
new_str=""
max_length=0
for current_str in s:
    if current_str  in new_str:
        split_index=new_str.index(current_str)
        new_str=new_str[split_index+1:]
    new_str=new_str+current_str
    if len(new_str)>max_length:
        max_length=len(new_str)
print("Length of longest unique substring:",max_length)