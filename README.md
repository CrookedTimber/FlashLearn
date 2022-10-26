# FlashLearn
 

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Development Notes](#development-notes)
- [Contact](#contact)

00_job_seeking\portfolio\FlashLearn\FlashLearn\screenshots\screenshot_1.png

![Alt text](/screenshots/screenshot_1.png?raw=true "Optional Title")

## Description

FlashLearn is a flashcards app that helps users to learn 200 of the most common words in 5 different languages. Once a card with a new word is shown, there's an 8 seconds delay before the answer is revealed. When the time runs out or, it's skipped by pressing the flip card button, users can record whether they knew the word in their language of choice. If known, the word is discarded from the card deck.

### Features:
    1. Five different languages: French, German, Italian, Portuguese, and Spanish.
    2. Users have the option to save their progress. It is possible for them to come back to challenge themselves with the remaining words at another occasion.

## Development Notes


### Built with:
    - Tkinter
    - Pandas

Having built a similar app for an online course relying heavily on procedural programming, I encountered certain limitations that I later learned could be overcome with OOP. As the number of components in the GUI grew, managing the data flow produced by the user interactions quickly becomes overly complicated and can lead to code that is hard to read and maintain. Building the main window of the app as an object, with its components among its properties, easily overcomes this issue as the as class methods are all communicated to the values that need to change according to the user's interactions. Furthermore, the navigation between windows themselves becomes effortless as it can be as simple as destroying a window of type class to invoke a new instance of a different one.


## Contact

 Name: Edgar René Ruiz López
 Email: edgarrruizl@gmail.com

