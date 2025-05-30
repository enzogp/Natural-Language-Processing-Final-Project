# Grammar Checking Game using Finite State Automaton (FSA)

Hi! This is a small NLP project made for fun and learning as part of a university course.

## What is it?

It's a terminal-based game where you’re given a random English sentence structure (like `Det + Noun + Verb`) and your goal is to write a sentence that matches it, like “the cat eats”. The system checks your sentence using a Finite State Automaton (FSA) and tells you if it's correct.

You gain or lose points based on how well you do — it's a bit like a grammar challenge quiz!

---

## What's in this project?

- `fsa_game.py` → the main game script. Run this to play!
- `wordbank.py` → contains all the vocabulary (grouped by part of speech)
- `structures.py` → lists all possible sentence structures the game can randomly use

All files are written in plain Python, no extra libraries needed.

---

## Why we made it

We wanted to do something interactive and educational with FSA theory instead of just talking about it. This project helped us connect theoretical automata concepts with real language usage — and hopefully, it’s useful (or fun) for others too.

---

## How to play

```bash
python fsa_game.py
