# 📌 LESSON 4 – PART 2: FEW-SHOT PROMPTING

*(Theory + Practical + Real-time + Engineering + Interview + Mini Project)*

---

## 🧠 1️⃣ THEORY — What is Few-Shot Prompting?

### Simple definition

**Few-shot prompting = teaching the model using examples inside the prompt.**

Instead of just saying *what to do*, you show:

* how inputs look
* how outputs should look

LLMs learn patterns extremely well from examples.

---

### Why it exists (real problem)

Instructions alone are often:

* misunderstood
* loosely followed
* ignored by small models (like local Ollama models)

Few-shot prompting **reduces ambiguity**.

---

### Mental model

Think of few-shot prompting like:

> “Here are 2 solved examples.
> Now solve the 3rd one the same way.”

Exactly how humans learn.

---

## 🛠️ 2️⃣ PRACTICAL — Few-Shot Prompt in LangChain

### Base setup

```python
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3", temperature=0)
```

---

### Few-shot prompt template

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an internal IT support assistant. Answer briefly."),
    
    ("human", "Question: How do I reset my company email password?"),
    ("ai", "Go to the internal portal → Security → Reset Password."),
    
    ("human", "Question: How do I request laptop access?"),
    ("ai", "Submit a ticket in the IT portal under Hardware Requests."),
    
    ("human", "Question: {question}")
])

chain = prompt | llm
```

---

### Run it

```python
response = chain.invoke({
    "question": "How do I get VPN access?"
})

print(response.content)
```

You’ll see:

* consistent style
* short answers
* less hallucination

---

## 🌍 3️⃣ REAL-TIME SCENARIO

### 🎯 Scenario: Company Internal Helpdesk Bot

Employees ask:

* IT questions
* access issues
* process-related doubts

Constraints:

* No long explanations
* No guessing
* Consistent format

Few-shot prompting ensures:

* uniform answers
* policy-safe responses
* predictable behavior

---

## ⚙️ 4️⃣ ENGINEERING POV — When to Use / Avoid Few-Shot

### ✅ Use few-shot when:

* Output format matters
* Model keeps hallucinating
* You need consistent tone
* Using smaller local models

### ❌ Avoid few-shot when:

* Prompt becomes very large
* Latency is critical
* Examples change frequently (dynamic data)

👉 In production, **few-shot = quality vs latency tradeoff**.

---

## 🐞 5️⃣ FAILURE MODE (Real Engineering Bug)

### Problem

Too many examples → slow responses.

### Fix

* Use **2–3 high-quality examples**
* Keep examples short
* Move repeated logic to system message

---

## 🎯 6️⃣ INTERVIEW QUESTIONS (With Answers)

### Q1️⃣ What is few-shot prompting?

**Answer:**
A technique where example input-output pairs are included in the prompt to guide model behavior.

---

### Q2️⃣ Why does few-shot work better than instructions alone?

**Answer:**
Because LLMs are pattern learners and follow demonstrated behavior more reliably than abstract instructions.

---

### Q3️⃣ What is the main downside of few-shot prompting?

**Answer:**
Increased prompt length, which affects latency and cost.

---

## 🧩 7️⃣ MINI REAL-TIME PROJECT (IMPORTANT)

### 🛠️ Project: **Local FAQ Assistant (Ollama + LangChain)**

This project uses **ALL skills so far**:

* ChatOllama
* Prompt templates
* System messages
* Few-shot prompting
* Debugging mindset

---

### 📋 Requirements

Build a CLI or function that:

* Answers FAQs
* Uses few-shot examples
* Says **“I don’t know”** if unsure
* Answers in **2 lines max**

---

### 🧠 Prompt Design

```python
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a company FAQ assistant. "
     "Answer in max 2 lines. "
     "If you don't know, say 'I don't know'."),
    
    ("human", "Question: What is company leave policy?"),
    ("ai", "You get 20 paid leaves per year as per HR policy."),
    
    ("human", "Question: How to apply for work from home?"),
    ("ai", "Submit a request via the HR portal."),
    
    ("human", "Question: {question}")
])
```

---

### 🧪 Run

```python
chain = prompt | llm

while True:
    q = input("Ask a question: ")
    if q.lower() == "exit":
        break
    print(chain.invoke({"question": q}).content)
```

---

## 🧠 What This Mini Project Teaches You

* How real bots are built
* Why prompt structure matters
* How to control hallucinations
* How Ollama behaves in production-like usage
* How LangChain glues everything safely

---

## 🔚 FINAL SUMMARY (Lesson 4 Complete)

* Few-shot prompting improves reliability
* Examples > instructions
* Tradeoff = latency vs accuracy
* Prompt = engineering contract
* Small models demand better prompts
