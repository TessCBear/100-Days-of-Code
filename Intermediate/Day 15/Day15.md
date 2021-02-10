# Day 15 of 100 Days of Code 
## Coffee Machine

There was no lesson today teaching a new concept, but I felt the jump in level for the project. The project today was to build a digital coffee machine. It should offer three drinks to choose from, check if it has the correct resources, if the user has paid enough and then output "coffee" and change where needed or state that it has too little resources etc.

It was quite a challenge to do everything and so I built it in stages. The first step was to get the machine asking for and outputting orders and using the correct amount of resources. Then I had to make it check if it had enough resources (so that it didn't have -200*ml* of milk, for example). Finally, I implemented the payment and change system.

My code was rewritten a few times. The most significant change was to convert from a massive function to a *while* loop. Although it probably wouldn't affect my code, I didn't want to run into a stacking issue where the computer runs out of memory from too much recursion.

I'm proud that I was able to implement this and of how far I've come!