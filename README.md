# 🔐 Password Guessing Game

A fun terminal-based word guessing game built with Python. Pick a difficulty, get a hint, and try to guess the hidden word!

---

## 🎮 How to Play

1. Run the script
2. Choose a difficulty level: `easy`, `medium`, or `hard`
3. You'll be told how many letters the word has
4. Type your guess — after each wrong attempt you'll get a hint showing which letters are in the correct position
5. Keep guessing until you crack it!

---

## 🧠 Difficulty Levels

| Level | Words |
|-------|-------|
| 🟢 Easy | banana, car, aeroplane, house, mother |
| 🟡 Medium | bottle, blackboard, cherry, formula, planet |
| 🔴 Hard | avalanche, diamond, cosmos, earth, mountain |

---

## 💡 Example Gameplay

```
-------- Welcome to Password Guessing Game --------
MODES: EASY | MEDIUM | HARD
Please enter the difficulty level: hard

I'm thinking of a 6 letter word. Good luck!

Enter your guess: castle
HINT: c_____

Enter your guess: cosmos
✨ CONGRATULATIONS! You guessed it in 2 tries! ✨

--- GAME OVER ---
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Run the game

```bash
python3 password_guessing_game.py
```

---

## 📁 Project Structure

```
password-guessing-game/
└── password_guessing_game.py   ← main game file
```

---

## 🛠️ Built With

- Python 3
- `random` module (standard library — no installs needed!)

---

## 🌱 Future Ideas

- Add a maximum attempts limit
- Reveal a letter as a hint after X wrong guesses
- Add more words to each difficulty tier
- Track and display a high score

---

## 👨‍💻 Author

**Arzaan**  
