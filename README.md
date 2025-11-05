### eGain-SWE

## Setup/Installation

# Requirements
- Python 3.8
- A web browser

# Running the chatbot
1. Clone or unzipe the project folder
2. Open a terminal and run:
    python chatbot.py
3. In another terminal run python -m http.server/5500
4. Open http://localhost:5500/index.html.
5. Type in the terminal; you should see the browser update every ~1.5s.

To exit the chatbot anytime, type:
    exit / quit / leave / q

## Overview/Approach

# Scenario

**Technical troubleshooting -- Wi-fi connectivity issues**

This chatbot simulates a customer service assistant guiding users through diagnosing and fixing Wi-Fi problems.
It covers three realistic issue categories:

1. Can’t connect to Wi-Fi
2. Slow or unstable Wi-Fi
3. (Minor) Forgot Wi-Fi password

# Design Approach

- Decision Tree Logic:
Implemented as sequential prompts (ask() function) that branch based on user input (yes/no/keywords).
Each path models real-world troubleshooting steps: router checks, device resets, driver updates, and ISP outages.

- Error Handling:
    1. Empty / unclear responses trigger reprompts
    2. Invalid responses (not in expected set) display acceptable options

- Keyword Normalization:
“yeah,” “yep,” and “affirmative” are normalized to yes; “nah,” “nope” to no.

- Separation of Logic and UI:
The Python script handles all reasoning and prints to chatlog.txt.
A lightweight HTML log viewer (index.html) renders the conversation visually without needing servers or APIs.

# Why this approach

The focus is on:
- Showing clear problem-solving flow rather than complex NLP.
- Keeping the codebase simple, readable, and testable.
- Demonstrating how a chatbot can guide users through multi-step troubleshooting while handling invalid inputs gracefully.

## Screenshots/Examples
<img width="450" height="500" alt="Screenshot 2025-11-05 at 5 13 56 AM" src="https://github.com/user-attachments/assets/eb3f3877-ea9e-4647-86ac-b586fe86bfb7" />
<img width="450" height="500" alt="Screenshot 2025-11-05 at 4 56 51 AM" src="https://github.com/user-attachments/assets/b00fe982-9de5-4879-acb8-85e215133f5d" />
<img width="450" height="500" alt="Screenshot 2025-11-05 at 4 53 25 AM" src="https://github.com/user-attachments/assets/0fa656dd-dee6-42cd-83d2-86a817988a2d" />
<img width="450" height="500" alt="Screenshot 2025-11-05 at 4 52 36 AM" src="https://github.com/user-attachments/assets/9d6e96c0-b64a-476a-b10f-460b81151929" />


