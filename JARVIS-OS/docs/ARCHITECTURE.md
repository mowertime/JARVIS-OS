# JARVIS OS Architecture

## Overview

JARVIS OS is a distributed AI orchestration system operating over LAN. It converts natural language into deterministic execution graphs that control models, tools, devices, and operating system functions.

## System Topology

```
┌──────────────────────────────────────────────────┐
│               Windows Node (Control)              │
│  ┌──────────┐  ┌──────────┐  ┌────────────────┐  │
│  │ FastAPI  │  │  Meta    │  │  Execution     │  │
│  │  Server  │◄─┤  Router  │─►│  Engine        │  │
│  └──────────┘  └──────────┘  └───────┬────────┘  │
│                                       │           │
│  ┌──────────┐  ┌──────────┐  ┌───────▼────────┐  │
│  │  Model   │  │  Memory  │  │  Tool Registry │  │
│  │ Manager  │  │  System  │  │  + Sandbox     │  │
│  └──────────┘  └──────────┘  └────────────────┘  │
│                                                   │
│  ┌────────────────────────────────────────────┐   │
│  │  Task Queue (Async Workers)               │   │
│  └────────────────────────────────────────────┘   │
└──────────────────────┬───────────────────────────┘
                       │ HTTP (POST /v1/jarvis)
                       │
┌──────────────────────▼───────────────────────────┐
│               Arch Linux Node (Interface)         │
│  ┌──────────┐  ┌──────────┐  ┌────────────────┐  │
│  │  Web UI  │  │  Voice   │  │  Agent Client  │  │
│  │ (HTML/CSS│  │  WakeWord│  │  (Session Mgr) │  │
│  │   /JS)   │  │  STT/TTS │  │                │  │
│  └──────────┘  └──────────┘  └────────────────┘  │
└──────────────────────────────────────────────────┘
```

## Node Responsibilities

### Windows Node (Control + Execution Plane)
- AI inference and model orchestration
- Natural language routing and planning
- Task decomposition and execution
- Tool execution with security sandboxing
- Memory management (episodic, semantic, working)
- Background task queue and async workers
- REST API service (FastAPI)

This node is authoritative. All reasoning and execution originates here.

### Arch Linux Node (Interface + Voice Plane)
- Wake word detection ("Hey Jarvis")
- Speech-to-text conversion
- Text-to-speech output
- Web-based user interface
- Request forwarding to Windows node

This node is stateless. It must never execute tools, perform reasoning, modify memory, or run orchestration logic.

## Request Flow

```
1. User Input (Voice or Text)
2. Arch Node captures and forwards to Windows Node
3. Meta Router analyzes intent and creates execution graph
4. Execution Engine processes steps with dependency resolution
5. Tools execute in sandboxed environment
6. Results merged and returned to Arch Node
7. Output displayed and/or spoken to user
```

## Model Stack

| Model | Role | Capabilities |
|-------|------|-------------|
| Qwen2.5 | Router/Planner | Planning, task decomposition, routing |
| Llama 3.1 | Conversation | Conversational responses only |
| DeepSeek-Coder | Code/Automation | Code generation, scripts, automation |
| Mistral 7B | Optional Critic | Validation, quality checking |

No model may directly execute actions. All tool use goes through the Execution Engine.

## Security Model

Trust hierarchy (highest to lowest):
1. Tool output
2. Execution engine state
3. Router output
4. Raw model output

Before execution:
- Validate JSON structure
- Validate schema compliance
- Enforce tool allowlists
- Sanitize shell commands
- Apply risk analysis
- Require confirmation for high-risk actions

## Memory Architecture

| Type | Storage | Content | Retention |
|------|---------|---------|-----------|
| Episodic | SQLite | Conversations, execution history, task logs | Persistent |
| Semantic | SQLite | User preferences, persistent facts, knowledge | Persistent |
| Working | SQLite | Session state, active tasks | Session-based |

## Task Lifecycle

```
RECEIVED → ROUTED → PLANNED → EXECUTING → WAITING → COMPLETED
                                                            ↘ FAILED
```

- FIFO queue with priority support
- Voice commands receive priority
- Async worker support for long-running tasks
- Retry limit: 2 attempts per step
- Failure halts pipeline execution

## Distribution Architecture

JARVIS OS Distribution is an Arch Linux-based operating system with:
- Btrfs filesystem
- Linux LTS kernel
- systemd init system
- Native JARVIS services as systemd units
- Hardware Abstraction Layer (jarvis-hal)
- Driver Manager (jarvis-driver-manager)
- Firmware Manager (fwupd integration)
- Self-healing service monitoring
