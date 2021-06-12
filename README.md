# Turtle-Game
A game programmed using python's turtle library. The goal of the game is to make users learn things about programming while playing a game.


**The game is designed and tested only for Windows Devices.**

It can run on linux but on online compilers like Repl.it it is laggy and has no sound. This happens because it uses the threading library to spawn new threads each time it plays a sound.



# Adding Questions:  

### GameMode1  
To add a new question you add a new element to self.questions array.
The new element must follow the format:
```pytohn
[["question", "\n[1]option1", "\n[2]option2", "\n[3]option3","\n[4]option4",  correctOption(a number from 1 to max alternatives)], [ObjectPoint, "Files/Images/image_you_want_to_appear_asObject"], 0]
```

You can wirte 1 to 4 alternatives for each question.
If you want pass a costum class instead of ObjectPoint to handle the question checkpoint.
```python
self.questions=[[["How can the Fox get all the coins?", "\n[1]Using an if statement", "\n[2]Using 10 nested if statements", "\n[3]Using a for loop until 10", 3], [coinsArray, None], 0],
                        [["How can the fox check if the light is green.", "\n[1]Using an if statement", "\n[2]Using a for loop", "\n[3]Using an array", 1], [ObjectPoint, "Files/Images/stoplight@0.25x.gif"], 0],
                        [["What do we get if we convert the number 65 to a character? \nprint(chr(65))", "\n[1]The number 65", "\n[2]An error", "\n[3]The letter A", 3], [ObjectPoint, "Files/Images/ascii.gif"], 0],
                        [["Did you know that computer codes had an important role in ending WWII", "https://www.iwm.org.uk/history/how-alan-turing-cracked-the-enigma-code"], [ObjectPoint, 'Files/Images/facts.gif'], 1]]
self.factsNum=1 # facts must always be inserted at the end
```
If you add a fact make sure you add it at the end of the array and update the value of ```self.factsNum=1```  
The format of adding a fact is:  
```[[shortFact, websiteLink], [ObjectPoint, "Files/Images/image_you_want_to_appear_asObject"], 1]]```

### GameMode2    
Adding questions to this game mode is easie. You just write and array where the first element is the question, the other 1 to 4 elements are the alternatives and the last one is the correct alternative (a number 1-4)
```
self.questions = [
    ["How do you access the first element of an array?", "\n[1] array[]", "\n[2] array[0]", "\n[3] array[1]", 2],
    ["The action of doing something over and over again, repeating code?", "\n[1] Program", "\n[2] Bug", "\n[3] Loop", "\n[4] Code", 3],
    ["A set of instructions that can be performed with or without a computer:", "\n[1] Bug", "\n[2] Debug", "\n[3] Loop", "\n[4] Algorithm", 4],
    ["An error, or mistake, that prevents the program from being run correctly:", "\n[1] Bug", "\n[2] Debug", "\n[3] Loop", "\n[4] Algorithm", 1],
    ["Finding and fixing errors or mistakes in programs:", "\n[1] Sequencing", "\n[2] Debugging", "\n[3] Looping", "\n[4] Decomposing", 2]
]
```
# Database  
The database is just an unencrypted JSON file. If running on windows it is placed under the folder ```C:/Users/getpass.getuser/AppData/Local/PythonGame```. Otherwise it is saved in the Files forder in working directory.
