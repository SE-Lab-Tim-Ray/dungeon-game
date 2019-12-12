# Sprint <1>: 2019-11-20 to 2019-11-27

## overview
* what's supposed to happen this sprint: Last week, we presented a moving character and a randomly generated maze to our customer. 
* This sprint aims to tackle the functionality of the game, to develop drawing the maze further.
* A second objective is to continue working on the moving character and combing the two such that the moving character can navigate around the maze. 
* A third objective is to add a timer to the game and a leader board such that a user can keep track of how long they have to complete the game and their score upon completion. 
* As previously mentioned, by the end of this sprint we aim to have a working but very basic maze game. 
* The iterations of this sprint are available on Trello, in the form of screenshots linked in the backlog section of this md file.  


## review
* Team planning of code structure created by Ray (resources/images/Code Structure.jpeg)
* Made maze and character and end square
* Feasibility for sprint 1 was overestimated,and the team found that putting the whole game together was difficult such as adding timer
* issues with timer: self counting timer affects main program due to two while loops so these are going to be moved to sprint 2, also tried to merge the two while loops into one, call a function to count time get the result and add the result to score calculator 
* leaderboard and start name input screen could not be achieved in sprint 1 so will be pushed to sprint 2 
* MAJOR ISSUE in sprint 1: unit testing not set up in code base - no automated tests have been written
* for sprint 2 need to map out user stories for testing 
* Tim said too ambitious for sprint 1, lack of communication between coders caused several versions of the main to be created - should have started with main and then done the other modules 
* To improve communication pair programming shall be undertaken 
* zhou agrees in being too ambitious, never developed so a lot of research needed to be done, havent reviewed any successful cases of the game, so in sprint 2 will review other implementation methods for our game 
* ray enjoys the logic and merging and found the conclusions reached at end of sprint were interesting 
* tim felt like we shofuld have started with one small thing but we started with 3 or 4 things and tried to merge. main shouldve been written first but now we know. 
* what needs to happen next has been discussed, the one function we need to focus on is the timer and really sort it out because the fundamental concept depends on it. 
* Documentation is being caught up on for sprint 0, but Geetha and Hajar are working well together to complete both documentation for sprint 0 and sprint 1
* advised by PhD's to organise Trello and show better evidence of work in progress, work completed and backlog 
* link (cross-reference) to relevant product documents

## meeting minutes
* For a more detailed account of our customer meetings please refer to section 2.1.2 of the Team Brown Sprint Documentation PDF (resources/Documentation/Team Brown Sprint Documentation.pdf). Below is a short summary of each meeting and analysis 

### meeting <20/11/19>
* Reflect on customer meeting
* Align sprint 1 objectives with customers specific requests
* Geetha and Hajar, formalise documentation so far 
* Ray and Zhou discuss code and it’s issues that need to be agreed on with Tim to move forward. 

### meeting <20/11/19> 
* Code structure planning 
* Rough structure discussed
* Ray creates detailed plan of code structure (resources/images/Code Structure.jpeg)

### meeting <21/11/19> 
* Delegating coding roles
* decisions made: 
* Fixed maze and only moving the character around 
* 800x600 single png 
* Character 32x32 
* 25 tiles across and 18 down 
* Fixed start
* Assignments: 
* Tim designs first maze with a “win square”
* Geetha and Hajar, formalise documentation for sprint zero. 
* Ray will make a movable character
* Zhou Board and Timer

### meeting <224/11/19> 
* SCRUM on Slack (resources/images/SCRUM sprint 1 24:11:19.mov)
* New objectives set after review of completed tasks 
* Assignments:
* Geetha create meeting records with cross referencing images
* Hajar  start compiling the rest of the documentation requirements for sprint 0
* Tim code maze builder 
* Ray code Hero.py (including moving in the map)
* Zhou complete leaderboard and timer

### meeting <26/11/19> 
* Short meeting regarding merging of code and fixing of timer 
* issues with timer: self counting timer affects main program due to two while loops so these are going to be moved to sprint 2
* also tried to merge the two while loops into one, call a function to count time get the result and add the result to score calculator
* Ray and Zhou will pair programme with Tim to resolve the issue with the timer

### meeting <27/11/19> 
* Prepare for customer meetings and review progress
* Functional testing sprint 1 
* Overestimated feasibility of sprint 1 objectives. Timer and leaderboard not complete so pushed to sprint 2
* Ray, tim and zhou:  pair programme on timer and leaderboard
* Geetha: team meeting record, use cases, testing, user stories testing and cleaning MD file for both sprints
* Hajar: backlog, exception handling, sprint 1 formal documentation

## backlog
* (resources/images/Trello Screenshots/Sprint 1 Backlog.jpeg)

### complete backlog tasks
* (resources/images/Trello Screenshots/Sprint 1 DONE.jpeg)

### new backlog tasks
* Count-down Timer
* Leaderboard 
* Input character name
* Start button
* Write up sprint 2 meetings 
* Write up customer meeting and analysis 
* Markdown (MD) file 
* Input all screenshots into all documents - MD and formal
* Sprint 2 use cases 
* Sprint 2 user stories 

## exception handling
* Not feasible to complete all task by end of sprint
* Timer, leaderboard and start button pushed to sprint two

## product documents

### customer meeting and analysis
* Which maze will make the game more engaging to play 
* Customer prefers randomised maze 
* Choose platform but if able to  can make platform independent 
* Sprint 0 Catch up on documentation deadline is 3 weeks away 
* Make a pip install package - how do we package a python application so it can self install all the relevant needs
* As a result of the meeting: 
* Plan of code structure created by Ray
* decision made to push unattainable tasks to sprint two

### user stories
## Original list of user stories for sprint 1 (Version 2):  
* 1: As a player, I want to be able to move because I want to complete the maze 
* 2: As a user, I want to see the intro screen and be told what to do 
* 3: As a user, I want to input my character name
* 4: As a user, I want to press the start game button 
* 5: As a user, I want to be able to see the time I have left (countdown) 
* 6: As a player I want the game to be executable on windows 
* 7: As a player after I finish the game I want to see the leaderboard

## Revised list of user stories for sprint 1 (Version 3): 
* 1: As a player, I want to input my character name 
* 2: As a player, I want to press the start game button 
* 3: As a player, I want to be able to see the time I have left (countdown) 
* 4: As a player, after I finish the game, I want to see the leaderboard
* 5: As a player, I want to be able to move my character
* 6: As a player, I want to be able to view the maze I need to traverse
* 7: As a player, I want to be able to know when I have completed the maze

## New user stories for next sprint:
* 1: As a user, I want to input my character name
* 2: As a user, I want to press the start game button 
* 3: As a user, I want to be able to see the time I have left (countdown) 
* 4: As a player after I finish the game, I want to see the leaderboard

### tests
* In review of sprint 1 on 27th November,Hajar and Geetha tested the functionality of the features the development team aimed to complete by the sprint
* 1: As a player, I want to input my character name: PASS
* 2: As a player, I want to press the start game button: FAIL
* 3: As a player, I want to be able to see the time I have left (countdown): FAIL 
* 4: As a player, after I finish the game, I want to see the leaderboard: FAIL
* 5: As a player, after I finish the game, I want to see the leaderboard: FAIL
* 6: As a player, I want to be able to move my character: PASS
* 7: As a player, I want to be able to view the maze I need to traverse: PASS
* 8: As a player, I want to be able to know when I have completed the maze: PASS

### requirements use cases
* UML SPRINT 1 (resources/images/UMLs/Sprint1.jpeg)
## Introduction Screen
* Connected to the following user stories: 
* 1: As a player, I want to input my character name 
* 2: As a player, I want to press the start game button 
* QWERTY keyboard input 

## Connected to the following user stories:
* 1: As a player, I want to input my character name 
* 5: As a player, I want to be able to move my character

## Mouse input 
* Connected to the following user stories:
* 2: As a player, I want to press the start game button

## Move character - arrow keys/ASDW
* Connected to the following user stories:
* 5: As a player, I want to be able to move my character
* 6: As a player, I want to be able to view the maze I need to traverse

##Countdown timer 
* Connected to the following user stories:
* 3: As a player, I want to be able to see the time I have left (countdown) 
* 4: As a player, after I finish the game, I want to see the leaderboard
* 7: As a player, I want to be able to know when I have completed the maze

##Leaderboard
* Connected to the following user stories:
* 1: As a player, I want to input my character name 
* 3: As a player, I want to be able to see the time I have left (countdown) 
* 4: As a player, after I finish the game, I want to see the leaderboard
* 7: As a player, I want to be able to know when I have completed the maze


### CRC cards
* (resources/images/CRC cards/dungeon crc cards v1.docx) 
* For connections to user stories please refer to section 2.2.6 of of the Team Brown Sprint Documentation PDF (resources/Documentation/Team Brown Sprint Documentation.pdf)

### user interface design
* (resources/images/1_ win.png)
* (resources/images/Start Screen V1.png)
* (resources/images/1_char.png)
* (resources/images/links.gif)



