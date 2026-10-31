---
name: openclaw-genpark-memory-vault
description: OpenClaw GenPark cryptographically partitioned hierarchical memory vault with Ebbinghaus time-decay and HMAC namespace isolation.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'generate_auth_token', 'description': 'Generate an HMAC authentication token for a tenant partition.'}
  - {'name': 'store_memory', 'description': 'Store an importance-weighted memory record in the vault.'}
  - {'name': 'query_memory_with_decay', 'description': 'Query memories ranked by time-decay retention score.'}
---

# Openclaw Genpark Memory Vault

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Memory Vault**.
Your primary directive is to execute: OpenClaw GenPark cryptographically partitioned hierarchical memory vault with Ebbinghaus time-decay and HMAC namespace isolation.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'generate_auth_token', 'description': 'Generate an HMAC authentication token for a tenant partition.'}`
- `{'name': 'store_memory', 'description': 'Store an importance-weighted memory record in the vault.'}`
- `{'name': 'query_memory_with_decay', 'description': 'Query memories ranked by time-decay retention score.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'generate_auth_token', 'description': 'Generate an HMAC authentication token for a tenant partition.'}`
- `{'name': 'store_memory', 'description': 'Store an importance-weighted memory record in the vault.'}`
- `{'name': 'query_memory_with_decay', 'description': 'Query memories ranked by time-decay retention score.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
