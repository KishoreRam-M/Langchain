# 📌 LESSON 2 — Getting Started with LangChain (Ollama-Only)

---

## 1️⃣ What is this lesson about?

This lesson is about building your **first working LangChain pipeline** using:

* a **local LLM (Ollama)**
* a **prompt**
* a **chain (pipeline)**
* a **clean mental model**

No agents yet
No memory yet
No RAG yet

Just **core foundations**.

---

## 2️⃣ Why does this lesson exist?

Most beginners fail because they:

* copy code
* don’t know **who talks to whom**
* don’t know **what runs where**
* don’t know **what LangChain actually controls**

This lesson fixes that.

After this lesson, you will be able to explain:

> “LangChain does NOT run models. It orchestrates steps.”

---

## 3️⃣ Big-Picture Mental Model (Very Important)

### Think in layers

```
┌──────────────────────────┐
│ Your Python Code         │
└───────────┬──────────────┘
            │
┌───────────▼──────────────┐
│ LangChain                │  ← orchestration
│ (prompts, chains)        │
└───────────┬──────────────┘
            │
┌───────────▼──────────────┐
│ ChatOllama               │  ← adapter
└───────────┬──────────────┘
            │ HTTP
┌───────────▼──────────────┐
│ Ollama Server (local)    │  ← runtime
└───────────┬──────────────┘
            │
┌───────────▼──────────────┐
│ LLM Model (llama3 etc.)  │
└──────────────────────────┘
```

LangChain **never touches the model directly**.

---

## 4️⃣ Step 1 — Install Required Packages

### Why these packages?

* `langchain-core` → base abstractions
* `langchain-ollama` → Ollama adapter

### Install

```bash
pip install langchain langchain-ollama
```

If Ollama is not running:

```bash
ollama run llama3
```

Leave it running.

---

## 5️⃣ Step 2 — Create the LLM Object

### Code

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)
```

---

### What is happening here?

#### ❓ Is this calling the model?

❌ No.

This only:

* stores configuration
* prepares an interface
* knows **where to send requests**

Actual inference happens **later**.

---

### Temperature (engineering meaning)

| Value | Effect                 |
| ----- | ---------------------- |
| 0.0   | deterministic, factual |
| 0.7   | balanced               |
| 1.0   | creative, risky        |

For:

* RAG → `0`
* Agents → `0–0.3`
* Creative writing → `0.7+`

---

## 6️⃣ Step 3 — Understand Messages (Chat Models)

LangChain uses **chat-style messages**, not raw strings.

### Message roles

* `system` → rules, behavior
* `human` → user input
* `ai` → model output

This matches how modern LLMs work internally.

---

## 7️⃣ Step 4 — Create a Prompt Template

### Why prompt templates?

Hard-coded strings break when:

* inputs change
* steps grow
* chains get reused

Templates give:

* structure
* safety
* reusability

---

### Code

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in simple words.")
])
```

---

### What `{topic}` means

It is a **placeholder**, not a variable yet.

LangChain will:

1. validate inputs
2. inject values
3. format messages

This prevents prompt bugs.

---

## 8️⃣ Step 5 — Build Your First Chain (LCEL)

This is the **core LangChain idea**.

### Code

```python
chain = prompt | llm
```

### Read this slowly:

```
prompt  →  llm
```

Meaning:

* take formatted prompt
* send it to the model
* get response

This `|` operator is called **LCEL (LangChain Expression Language)**.

---

## 9️⃣ Step 6 — Invoke the Chain

### Code

```python
response = chain.invoke({
    "topic": "LangChain"
})

print(response.content)
```

---

### What happens internally (step-by-step)

1. `{topic}` = `"LangChain"`
2. Prompt is formatted
3. Messages are created
4. Sent to ChatOllama
5. HTTP request → Ollama
6. Tokens generated
7. Tokens streamed back
8. Final message returned

---

## 10️⃣ What Exactly Is `response`?

`response` is **NOT a string**.

It is an **AIMessage object**.

That’s why we use:

```python
response.content
```

This design supports:

* metadata
* tool calls
* streaming
* future extensions

---

## 11️⃣ System Design View

This is now a **real system**, not a script.

```
User Input
   ↓
Prompt Template
   ↓
Chain
   ↓
LLM (Ollama)
   ↓
Structured Response
```

You can:

* add another prompt
* add a parser
* add memory
* add tools

Without rewriting everything.

---

## 12️⃣ Common Beginner Mistakes (Important)

### ❌ Mistake 1: Treating LangChain as magic

LangChain just moves data between components.

### ❌ Mistake 2: Thinking `ChatOllama` runs models

It only **calls** Ollama.

### ❌ Mistake 3: Ignoring message objects

Chat models are **not strings**.

---

## 13️⃣ Production Considerations (Early but Critical)

Even at this stage:

* Each `.invoke()` = **one LLM call**
* Ollama = CPU-bound
* Long prompts = slow inference
* Chains hide complexity → log everything later

---

## 14️⃣ Interview Questions (Lesson-Level)

### Q1: What does LangChain control vs Ollama?

**Answer:**
LangChain controls orchestration; Ollama runs the model.

### Q2: What is LCEL?

**Answer:**
A declarative way to compose LLM pipelines using `|`.

### Q3: Why use prompt templates?

**Answer:**
They enforce structure, prevent injection bugs, and enable reuse.
