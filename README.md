# Python-Quiz-App-using-JSON
A simple quiz application built with Python that reads questions from a `JSON` file, randomizes them, and lets the user take a multiple-choice quiz. It calculates and displays the final score at the end.

## What It Does

- Loads a set of quiz questions from a JSON file
- Randomly selects a set number of questions
- Asks the user to pick answers from multiple options
- Calculates and displays the total score

## Features

- Random question selection using `random.sample()`
- Clean multiple-choice display with numbered options
- Score tracking
- Reads from external file `questions.json` for easy question updates

## Folder Structure

quiz-app/
├── quiz.py
├── questions.json
└── README.md


Example `questions.json`:
```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "options": ["London", "Paris", "Berlin", "Madrid"],
      "answer": "Paris"
    },
    {
      "question": "Which language is used for web apps?",
      "options": ["Python", "JavaScript", "HTML", "All of the above"],
      "answer": "All of the above"
    }
  ]
}
