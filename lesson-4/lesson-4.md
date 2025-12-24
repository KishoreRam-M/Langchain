# 📌 LESSON 4 — Prompt Templates

*(Theory + Practical + Real-Time Use Case + Engineering POV + Interview)*

---

## 🧠 1️⃣ THEORY — What Problem Prompt Templates Solve

### Core problem in real systems

LLMs don’t fail like normal code.

They fail by:

* sounding confident
* giving wrong answers
* not throwing errors

**Prompt templates exist to make LLM behavior predictable and debuggable.**

---

## 🛠️ 2️⃣ PRACTICAL — Base Setup (Ollama Only)

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3", temperature=0)
```

---

## 🌍 3️⃣ REAL-TIME SCENARIO (Very Important)

### 🎯 Scenario: Internal Company Knowledge Assistant

**Problem**

* Company employees ask technical questions
* Answers must be:

  * accurate
  * short
  * role-aware
* Wrong answers = production incidents

---

## 🧠 4️⃣ ENGINEERING DESIGN (Prompt Role)

In production, **prompt = contract**.

Prompt defines:

* tone
* length
* assumptions
* allowed behavior

You **never** trust raw user input.

---

## 🛠️ 5️⃣ PRACTICAL — Production-Style Prompt Template

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an internal engineering assistant. "
     "Answer concisely. "
     "If unsure, say 'I don't know'."),
    ("human", "Question: {question}")
])

chain = prompt | llm
```

```python
response = chain.invoke({
    "question": "What is LangChain?"
})

print(response.content)
```

---

## 🔍 6️⃣ DEBUGGING VIEW (Engineering Habit)

```python
formatted = prompt.invoke({
    "question": "What is LangChain?"
})

print(formatted)
```

### Why engineers do this

* This is **exactly** what the model sees
* 90% bugs are visible here
* No guessing

---

## ⚙️ 7️⃣ ENGINEERING POV — Tradeoffs

### Why not raw strings?

* ❌ No validation
* ❌ Silent failures
* ❌ No reuse

### Why prompt templates?

* ✅ Fail fast
* ✅ Safer refactors
* ✅ Better observability
* ✅ Easy audits (important in enterprises)

---

## 🧪 8️⃣ FAILURE MODE (Real Production Bug)

### Bad system prompt ❌

```text
"You are an expert. Explain everything."
```

Result:

* Long answers
* High latency
* Hallucinations

### Fixed prompt ✅

```text
"You are an engineering assistant. Answer in 3 bullet points. If unsure, say you don’t know."
```

👉 Prompt quality directly affects:

* latency
* accuracy
* reliability

---

## 🧠 9️⃣ INTERVIEW QUESTIONS (With Ideal Answers)

### Q1️⃣ Why are prompt templates important in production LLM systems?

**Answer:**
They enforce structure, validate inputs, reduce silent failures, and make LLM behavior predictable and debuggable.

---

### Q2️⃣ What’s the difference between system and human messages?

**Answer:**
System messages control model behavior and constraints, while human messages provide task-specific input.

---

### Q3️⃣ Where do most LLM bugs originate?

**Answer:**
In prompt design and prompt-data wiring, not in the model itself.

---

## 🧩 🔟 CTA — What You Should BUILD Now

### Mini-Task (Very Important)

Build a **local FAQ bot** using Ollama:

* Prompt rules:

  * Answer only from provided text
  * Say “I don’t know” if missing
* Input:

  * User question
* Output:

  * Short factual answer

This is **90% of real-world LLM work**.

---

## 🚀 🔚 SUMMARY (Engineer-Level)

* Prompt templates = contracts
* System messages control behavior
* Debug formatted prompts, not guesses
* Small models need better prompts
* Production failures start at prompt level

---

## 🎓 CHECKPOINT (Answer Briefly)

1️⃣ Why is prompt considered a “contract” in production systems?
2️⃣ What is the FIRST thing you inspect when an answer is wrong?
3️⃣ Why should an LLM be allowed to say “I don’t know”?

