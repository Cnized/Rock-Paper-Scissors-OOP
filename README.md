# Rock‑Paper‑Scissors (OOP)  🎮✊✋✌️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A simple **Rock‑Paper‑Scissors game** implemented in Python using an **object‑oriented design**. Play against the computer, track your score, and enjoy a clean, modular code structure.

---

## 📌 Project Repository

**GitHub:** [Cnized/Rock‑Paper‑Scissors‑OOP](https://github.com/Cnized/Rock-Paper-Scissors-OOP)

---

## ✨ Features

- Classic **Rock‑Paper‑Scissors** gameplay.
- **Object‑oriented design** with a `RockPaperScissors` class encapsulating game logic.
- Score tracking:
  - ✅ **Win:** +10 points  
  - ❌ **Lose:** -5 points (score never goes below 0)  
  - 🤝 **Draw:** No score change
- Keeps track of your **player name** during the session.
- Input validation ensures only valid moves (`rock`, `paper`, `scissors`) are accepted.
- Ability to **play multiple rounds** until you choose to quit.

---

## 🚀 Usage

### Clone the Repository
```bash
git clone https://github.com/Cnized/Rock-Paper-Scissors-OOP.git
cd Rock-Paper-Scissors-OOP
```

### Run the Game
```bash
python rock_paper_scissors.py
```

---

## 🎮 How to Play

1. When prompted, enter your **name** (it stays constant for the session).
2. Input your move: `rock`, `paper`, or `scissors`.
3. The computer will randomly choose its move.
4. The game will display both choices and the result (win/lose/draw), along with your updated score.
5. You can choose to play again or type `no` to quit.

---

## 📂 Project Structure

```
Rock‑Paper‑Scissors‑OOP/
│
├── src/
│   └── rock_paper_scissors.py     # Main game implementation
├── README.md                      # Project documentation
└── LICENSE                        
```
## 📝 Example Gameplay


Enter your name: (Choose wisely, you can't change it during the game) Alex
Enter a Valid choice: ( ['rock', 'paper', 'scissors'] ) rock
User choice: rock, Computer choice: scissors
Alex is the Winner!
 score: 10

Do you want to play again? (Press any key to continue, 'no' to quit.)


---

## 🔮 Potential Improvements

Here are some ways to enhance the project:

- Support **best-of‑3** or **best‑of‑5** formats.
- **Persist high scores** in a file or database.
- Create a **graphical user interface** using Tkinter or Pygame.
- Implement **multiplayer support**, possibly via network or local play.
- Refactor to use **enums**, **strategy patterns**, or modular game states.
- Add **unit tests** for validation, score updates, and game logic.

---

## 📜 License

This project can be licensed under the **MIT License**—feel free to add a `LICENSE` file to apply.

---
## 👨‍💻Author
💻 Built with ❤️ by Kian Kheiri N. ([@Cnized](https://github.com/Cnized))


*Happy coding and may your choices be ever in your favor!*

