# CP1404 Assignment 2: Reading Tracker 2.0 by Zar Chi Oo
Name:Zar Chi Oo
Date:12/1/2023
Brief Project Description:Reading Tracker Program Assignment 2
GitHub URL:https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-2-ZarChi123.git

_At the end of the project, complete the project reflection below by answering the questions (replace the ... parts)._
_Note that to get high marks for this, your reflection should match the "exemplary" description from the rubric:_

> The project reflection is complete and describes development and learning well, shows careful thought, highlights insights made during code development.


## 1. How long did the entire project (assignment 2) take you?
...  
Note: You may like to use the WakaTime plugin, which tracks exactly how long you spend in code. See http://wakatime.com (but note that the free version only has a 7-day history)

I started my project on 12 January 2023 and continuously work on it progressively until the due date.Each time I work on my project,I focus on chunks of projects.Each time I work on this project, it took me about 5hours 16 minutes according to WakaTime to complete each chunk of the project.I work on the assingment for 11 days , not continiously therefore it took me total of about 55hours + to complete the whole project.

## 2. What are you most satisfied with?
I was most satisfied with my GUI program about how it turned out.AFter careful intricate testing on each function of the project , when the output turns out right,
I get a very good satisfaction.When working on my main.py, I was really happy knowing that my spinner and buttons turn out to align well and the colour of the buttons also matched the sample output.

## 3. What are you least satisfied with?
I was least statisfied with my debugging skills for the project because it took me a few days to really think about and trace back what could possibly went wrong in my code. Moreover, I was quite worried about my kivy layout to construct my GUI program and I have messed up a few times but later the kivy demos helped me alot and I came to match the sample shown in the assingment instructions file.Overall, I am not satisfied with my kivy program as it took me a few days to complete the GUI structure but when I was able to successfully debug it, I felt happy.I also faced challenges while making the buttons dynamic and adding new book because the for loop which I used for creating the buttons causing errors but this was handled later by using a change state function.

## 4. What worked well in your development process?
I tried to use SRP, to write the code and try to cooperate with exception handling,list comprehension and all the new concepts my lecturer has taught me to
as well as meet the  requirements.I was able to do all those with the time given which works well in the development process. I also cooperated using classes well which help me able to focus well and make debugging easier.

## 5. What about your process could be improved the next time you do a project like this?
I felt like although my project turned out to match the sample output, I think I wasted too much time and my coding process was uneffective because to solve one error, it took me several days to figure out which can be improved by solving more problems and trying out new projects online or extra resources provided by lecturer.


## 6. Describe what learning resources you used and how you used them.
I use the lecture slides uploaded in learnJCU, for further understanding I also make use of websites such as stackoverflow to find the meaning of the errors I faced and use the knowledge of how other coders solved these issues to overcome my own.
The another great resource that helped me with the GUI part was the kivy demos which my lecturer has uploaded which samples the different parts of kivy such as using spinner and creating buttons.Based on these demos, I have constructed my own kivy/GUI program.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
The challenge that I faced mainly was that my program keeps crashing in the main.py while working on my GUI program which I used exception handling to fix these errors.Another challenge I faced was debugging the code for exception handling was that when the file name has been changed to another, and when the GUI is being run again, the exception handling does not work which took me some time to figure out why the text"unable to look book.csv" could not show even though there was no obvious errors in the code,no pycharm alerts or any errors in console.I try to change the code abit to fix but I have to trace back every single detail concerning with the def build function.To my surprise, the problem occured because in the program book_collection.py load book function , I used exception handling and used exception handling again for the same def build method.This particular use of two exeption handling for the same task occured as a nested function which caused an error.But it was solved when I removed the exception handling in the book_collection.py's load book function and only apply the exception  handling for the main.py .
## 8. Briefly describe your experience using classes and if/how they improved your code.
Using classes have been extremely helpful in improving my code.Not only it increase reusability of objects in the program, it also provide a structure which makes coding more organise and divide them into multiple logical chunks which makes it more manageable for me as I can easily work on it without taking a whole complex code and try to code it in one go.It also enable polymorphisim because when I use the classes it allow the objects I create to be treated as a common type making it easier to write the code and I was also able to resue these codes in other different areas.It also makes debugging alot easier as I can easily identify what went wrong and I can only focus on that particular class and try to find out the errors regarding this class
