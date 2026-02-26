# neoclawd
Ultra-light multi-agent system with free models (DeepSeek, Ollama, Qveris.ai) - optimized for 2013 iMac with Core i5 8GB RAM
┌─────────────────────────────────────────────────────────────┐
│                      NEOCLAWD SYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        Frontend (Lightweight Web UI)                 │  │
│  │  - React/Vue.js minimal build (lightweight)          │  │
│  │  - Agent orchestration dashboard                     │  │
│  │  - Multi-model switching interface                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↓                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │     Agent Router & Orchestration Layer               │  │
│  │  - Route tasks to available models                   │  │
│  │  - Model availability checker                        │  │
│  │  - Cost optimizer (free tier preference)             │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↓                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        Multi-Model Backend Layer                     │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │  │
│  │  │ DeepSeek    │  │ Ollama      │  │ OpenRouter  │ │  │
│  │  │ (Free tier) │  │ (Free local)│  │ (Free tier) │ │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↓                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │     Data Analysis Module (Qveris.ai API)            │  │
│  │  - Lightweight API client                            │  │
│  │  - Query builder & response parser                   │  │
│  │  - Results caching (reduce API calls)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
