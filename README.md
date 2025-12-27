# 🧶 Granny’s Tote of Tiny Tales

Granny’s Tote of Tiny Tales is inspired by the old Bengali folk tales called *Thakumaar Jhuli*.

It is a child-safe, conversational bedtime storytelling system that generates, evaluates, and refines gentle stories for children aged 5–10 using a Storyteller LLM and an LLM Judge.

The system is designed to feel like a warm conversation with “Granny,” while silently enforcing quality, emotional safety, and narrative structure in the background.

---

## ✨ What this project does

- Generates bedtime-appropriate stories for children aged 5–10
- Supports conversational interaction (e.g. “make it shorter”, “change the ending”)
- Uses explicit story arcs for better narrative quality
- Uses an LLM-as-a-Judge to evaluate and improve stories before showing them to the user
- Keeps safety and quality checks invisible to the child

---

## 🧠 System design overview

The system uses a two-agent architecture coordinated by a story loop:

- **Storyteller Agent (“Granny”)**
  - Creative, conversational, memory-aware
  - Generates or revises stories using a fixed, child-safe story arc

- **Judge Agent**
  - Stateless evaluator
  - Scores stories on age-appropriateness, emotional safety, clarity, and creativity
  - Provides structured feedback used for refinement

The judge never speaks to the user — it operates silently as a quality gate.

---

## 🔁 Story flow (high level)

User
↓
Intent Detection (new story vs modify)
↓
Storyteller Agent (story arc enforced)
↓
Judge Agent (quality & safety check)
↓
(Optional refinement loop)
↓
Final story shown to user


---

## 📖 Story arcs

Every story follows the same 4-stage arc, enforced through prompting:

1. **Setup** – Introduce character and cozy setting  
2. **Gentle Challenge** – A small, non-scary problem or curiosity  
3. **Resolution** – Solved through kindness, courage, or curiosity  
4. **Warm Ending** – Calm reassurance and a gentle lesson  

This improves consistency, emotional safety, and bedtime suitability.

---

## 🗂️ Project structure

grannys-tale-tote/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── app/
│ ├── main.py
│ ├── agents/
│ │ ├── storyteller.py
│ │ └── judge.py
│ ├── pipeline/
│ │ └── story_loop.py
│ ├── prompts/
│ │ ├── storyteller_prompt.py
│ │ └── judge_prompt.py
│ ├── state/
│ │ └── conversation.py
│ └── utils/
│ ├── llm_client.py
│ └── intent.py
│
└── diagrams/
└── system_flow.mmd


---

## ▶️ How to run the application

1. Clone the repository


git clone <your-repo-url>
cd grannys-tale-tote


2. Create and activate a virtual environment


python -m venv .venv
source .venv/bin/activate


3. Install dependencies


pip install -r requirements.txt


4. Add your OpenAI API key to the '.env' file at the repo root

OPENAI_API_KEY=your_key_here


5. Run the chatbot

python -m app.main



Type natural language prompts like:
- Tell me a bedtime story about a shy dragon
- Can you make it shorter?
- Change the ending to be happier

Type `good night`, `bye`, or `exit` to end the session.

---

## 🛡️ Safety & quality considerations

- No violence, fear, or cruelty allowed
- Explicit bedtime tone enforced via prompting
- Judge agent runs at low temperature for consistency
- Revision loops are bounded to prevent runaway generation
- Control flow (exit, intent detection) is handled in code, not by the model

---

## 🤖 Why an LLM Judge?

The judge simulates a human reviewer:
- Ensures stories are age-appropriate
- Improves clarity and emotional tone
- Makes the system safer without reducing creativity

This mirrors real-world content review workflows while remaining fully LLM-native.

---

## ⏱️ What I would build next (with 2 more hours)

- Persist conversation state across sessions
- Make it production ready by adding a testing framework and deployment module.

---
