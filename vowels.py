vowel = ["a","e","i","o","u"]
char = "gokul"
count=0
vowel_list=[]
for i in char:
    if i in vowel:
        count+=1
        vowel_list.append(i)
print(vowel_list,count)
