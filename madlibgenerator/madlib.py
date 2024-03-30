# read story from a file only 
with open("madlibgenerator/story.txt","r") as f:
    story=f.read()
#print(story)

startindex=-1
targetstart="<"
targetend=">"
keys=set()

for index, char in enumerate(story):
    if char==targetstart:
        startindex=index
    if char==targetend and startindex!=-1:
        key=story[startindex:index+1]
        keys.add(key)
        startindex=-1

#print(keys)

dic={}

for key in keys:
    keyvalue=input("Enter answer for"+ key +": ")
    dic[key]=keyvalue

#print(dic)
for key in keys:
    story=story.replace(key,dic[key])

print(story)

