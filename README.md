# GenLayer AI Truth & Fact Verifier

An Intelligent Contract application built for **GenLayer v0.2.17** that utilizes multi-validator LLM consensus (`gl.exec_prompt`) to verify claims, rumors, and news headlines in a decentralized, uncensored manner.

---

## Overview

Traditional fact-checking relies on centralized intermediaries. The **GenLayer Fact Verifier** delegates the evaluation of news claims directly to GenLayer's non-deterministic consensus layer. Multiple validator nodes execute real-time LLM prompts to reach an agreed-upon verdict on claim plausibility.

---

## Key Features

- **Decentralized Fact-Checking**: Eliminates reliance on single entities for news evaluation.
- **LLM Multi-Validator Consensus**: Executes `gl.exec_prompt` across validator nodes to evaluate claim accuracy.
- **v0.2.17 Compatibility**: Built using the latest GenLayer SDK standards (`@gl.public.write` and `@gl.public.view`).
- **Interactive Web Interface**: Complete with a modern, responsive single-page frontend.

---

## Contract Architecture (`verifier.py`)

- **`verify_claim(claim_text: str) -> str`**: 
  Submits a claim to GenLayer nodes, triggers non-deterministic consensus using LLM execution, and updates internal contract state.
  
- **`get_last_result() -> str`**: 
  Retrieves the latest verified consensus result stored on-chain.

- **`get_stats() -> u256`**: 
  Returns the total counter of claim verifications processed by the contract.

---

## Project Structure

```text
├── verifier.py       # Intelligent Contract logic (GenLayer v0.2.17)
├── index.html        # Interactive Frontend UI (Hosted via GitHub Pages)
└── README.md         # Documentation and project overview
