# AI Assistant with LangGraph & LangChain 🤖

This is my **first AI mini project**, built by following a YouTube tutorial and implementing it step by step.

The project demonstrates how to build a **simple AI assistant** using **LangChain**, **LangGraph**, and **OpenAI**, with support for custom tools like a calculator and a greeting function.

---

## 🚀 Features

* Interactive command-line AI assistant
* Uses OpenAI chat models via LangChain
* Built with LangGraph’s ReAct-style agent
* Custom tools:

  * 🧮 Calculator (adds two numbers)
  * 👋 Greeting tool (greets the user by name)
* Streaming AI responses
* Environment variable support using `python-dotenv`

---

## 🛠 Technologies Used

* Python
* LangChain
* LangGraph
* OpenAI API
* python-dotenv
* uv (for dependency management)

---

## 📂 Project Structure

```
PROJECT1/
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rithikashreepV/AI-Projects.git
cd AI-Projects/PROJECT1
```

### 2️⃣ Install dependencies

```bash
uv sync
```

### 3️⃣ Set up environment variables

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never upload your `.env` file to GitHub.

---

## ▶️ Run the Project

```bash
python main.py
```

You will see:

```
Hi!!!! Im Your AI assistant.To exit type 'quit'
Tell me what are you feeling
```

Type messages to interact with the AI.
Type `quit` to exit.

---

## 🧪 Example Capabilities

* **Calculator**

  ```
  You: add 3 and 5
  Assistant: The sum of 3 + 5 is 8
  ```

* **Greeting**

  ```
  You: greet me my name is Alex
  Assistant: hello Alex nice to see you
  ```

---

## 📌 Notes

* This project is for **learning purposes**
* Built as part of my journey into AI and LLM-based applications


---

## 🌱 Future Improvements

* Add more tools
* Improve prompt handling
* Add memory support
* Build a web interface

