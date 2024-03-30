# Madlib with output in output file

#read the story.txt file 
with open("madlibgenerator/story.txt","r")as f:
    story=f.read()
#print(story)

#bc i dont need any duplicatinos
words=set()
targetstart="<"
targetend=">"
start=-1
# enumerator loop because i need index as well as char
for i, char in enumerate(story):
    if char==targetstart:
        start=i
    if char==targetend and start!=-1:
        word=story[start:i+1]
        words.add(word)
        #reset
        start=-1
#print(words)

#now setting up dictionary
answers={}
#adding input in dictionary
for word in words:
    answer=input("Enter a word for"+ word +": ")
    #inputting in dictionary 
    answers[word]=answer
    

#print(answers)
for word in words:
    story=story.replace(word,answers[word])
    
with open("madlibgenerator/outputstory.txt","w") as f:
    f.write(story)