# Overview
This is a repo with projects relating to chapters in the book "Game Programming Patterns" by Robert Nystrom.

## Command Patterns

### What is it ?
**Command Pattern** is a behavioral design pattern that turns a request into a stand-aline object the contains all information about the request.

This Transformation lets you pass requests as a method arguments, delay or queue a requests's exection, and support undoable operations.

## Flyweight Patterns

## What is it ?
**Flyweight** is a structural design pattern that lets you fit more obejcts into the avaible aount of RAM by sharing common parts of state between mutltiple objects instead of keeping all the data in each object.

## Observer Pattern

## What is it ?
**Observer** is a behavioral design pattern that lets you define a subscription mechanisim to notify multiple objects about any event that happen to the object they're observing

### Project
Build a tiny dodge game where you move a square, and falling circles either help you or hurt you. The game itself is boring on purpose. The real exercise is one rule: the things that cause events are never allowed to know who cares about them.

When the player gets hit, it doesn’t update the health bar, play a flash, or check for achievements. It just announces “I got hurt.” Whoever wants to react, whether the health bar, the score, or some effect, has signed up to hear that announcement.

How I’d want you to approach it:

First, build it the “wrong” way: have collisions directly update the score and health. Notice how tangled it gets, and how many places you’d have to edit to add something new.

Then refactor so collisions only announce what happened, and other systems listen. Pay attention to how that changes who depends on whom.

Finally, test yourself by adding a brand-new feature, like an achievement popup or a screen flash, without touching the player or the falling objects at all. If you can do that, you understand observers.

Questions to keep asking yourself:

Who knows about whom? Draw the arrows.
Could I delete the HUD and still have the game run?
What should happen if something stops listening, like a one-time achievement or a temporary shield?
What information should an announcement carry, and what should it leave out?

By the end of the day, you should be able to explain in one sentence why the observer pattern exists, using your own game as the example.
