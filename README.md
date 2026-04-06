# 🚀 GenAI Evaluation & Testing Framework

A production-style framework to evaluate, test, and validate Generative
AI systems (RAG pipelines, LLM responses, and AI agents) using automated
metrics, adversarial testing, and structured reporting.

------------------------------------------------------------------------

## 📌 Problem Statement

Generative AI systems often produce: - ❌ Hallucinated responses - ❌
Unreliable outputs - ❌ Vulnerability to prompt injection - ❌ Lack of
measurable quality metrics

There is a critical need for systematic testing and evaluation
frameworks to ensure reliability, safety, and performance.

------------------------------------------------------------------------

## 💡 Solution

This project provides an end-to-end GenAI testing framework that:

-   Evaluates LLM responses using quantifiable metrics
-   Detects hallucinations and prompt injection risks
-   Runs adversarial and edge-case test scenarios
-   Generates structured HTML reports
-   Supports CLI-based and config-driven execution

------------------------------------------------------------------------

## 🧱 Architecture

User Query → Retriever (FAISS) → Context\
→ Generator (LLM/Mock) → Response\
→ Evaluation Engine → Scores + Verdict\
→ Prompt Test Suite → Batch Testing\
→ HTML Report → Visualization

------------------------------------------------------------------------

## ⚙️ Features

### ✅ RAG Pipeline

-   Document ingestion and chunking
-   FAISS-based vector search
-   Context-aware response generation

### 📊 Evaluation Engine

-   Relevance scoring
-   Faithfulness (context grounding)
-   Hallucination detection
-   Prompt injection detection
-   Final verdict classification

### 🧪 Prompt Testing

-   Adversarial inputs (prompt injection)
-   Ambiguous queries
-   Edge cases (empty, out-of-context)
-   Batch test execution

### 📄 Reporting

-   HTML dashboard (Playwright-style)
-   Color-coded verdicts (Pass/Fail/Warning)
-   Timestamped reports for traceability

### ⚙️ CLI + Config Support

-   Run test suite or single query
-   YAML-based configuration
-   CI/CD ready execution

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   LangChain (modular ecosystem)
-   FAISS (vector database)
-   OpenAI / Mock LLM
-   YAML (config-driven execution)

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone the Repository

git clone
https://github.com/madhuri2510/genai-evaluation-framework.git
cd genai-evaluation-framework

------------------------------------------------------------------------

### 2. Setup Virtual Environment

python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

------------------------------------------------------------------------

### 3. Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

### 4. Configure Environment Variables

Create `.env` file:

OPENAI_API_KEY=your_api_key_here

------------------------------------------------------------------------

### 5. Run Test Suite

python main.py --mode test

------------------------------------------------------------------------

### 6. Run Single Query

python main.py --mode single

------------------------------------------------------------------------

## 📊 Sample Output

=== EVALUATION === { "relevance": 0.7, "faithfulness": 0.85,
"hallucination": false, "prompt_injection": false }

=== FINAL VERDICT === ✅ PASS: Response is reliable

------------------------------------------------------------------------

## 📁 Project Structure

genai-evaluation-framework/ │ ├── rag/ ├── evaluation/ ├──
prompt_testing/ ├── reports/ ├── utils/ ├── data/ ├── config.yaml ├──
main.py

------------------------------------------------------------------------

## 🧠 Key Highlights

-   Modular architecture
-   Focus on AI quality and safety
-   Combines QA + GenAI engineering
-   CI/CD ready design

------------------------------------------------------------------------

## 🎯 Use Cases

-   RAG system validation\
-   LLM output quality assessment\
-   Prompt injection testing\
-   AI safety evaluation\
-   GenAI QA automation

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   RAGAS integration\
-   Advanced hallucination detection\
-   Analytics dashboard\
-   Multi-model comparison\
-   CI/CD pipeline integration

------------------------------------------------------------------------

## 👩‍💻 Author

Madhuri Goswami\
Principal QA Engineer \| GenAI Testing Enthusiast

------------------------------------------------------------------------

## ⭐ If you found this useful

Give a ⭐ to support the project!
