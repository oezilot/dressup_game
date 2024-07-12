# Dress-Up Game

## Description
This game was created as my first school project in computer science with the aim of creating a comfortable dress up game. 
In order to do justice to my raw knowledge in this field, I adapted the original idea and created a mixture of dress up 
and an already existing shooter game. Basically what the game does is throwing clothes at a person, causing them to put on 
or take off their clothes to create a desired look.

## Objects
There are many different objects, which are divided into 3 categories. Each category has a unique appearance and unique functions.
- Player: This object is the main character and is controlled by the person behind the screen by pressing a button upwards, downwards or sideways. Using these movements, the player can dodge or collide with enemies. 
- Enemies: They can either be pieces of clothing or stars. Stars remove a random clothing item from the player, while Cloting pieces put on clothes. 
- Mirror: This marks the endgate of the play.

## Rules
The game can end in many different ways, and with each option you can either win or lose.
- Win: The goal is to reach the mirror. The player can achieve this goal naked, half-clothed (with top or bottom only) or fully clothed with top and bottom.
- Lose: If the player is naked and collides with a star or if the player is clothed and collides with another clothing piece

## Tools
- Python (pygame library)
- Self-drawn images and characters
- Sound effects for buttons, movements and a background ambiance

## Extensions
- A rating (complete outfits with top and shirt get more points than half finished outfits or nudity, time, etc.)
- Timer (how much time goes by until the player reaches the mirror?)
- Increase Speed with ongoing time
- Outfit-Templates (in the beginning its shown which outfit is in trend and with that gives off the most points)
- The music doesn't work as it should, which I was not able to fix

## Running the Game
- Windows: Download the "DressUp"-folder from the brunch called "main"!
- Linux: Download the "DressUp"-folder from the brunch called "fix-imports"!
