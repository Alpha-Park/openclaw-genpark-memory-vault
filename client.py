# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Memory Vault
Standard Library only: hashlib, hmac, math, time, typing.
Cryptographically partitioned hierarchical memory vault with Ebbinghaus time-decay,
importance-weighted recall, and namespace isolation.
"""

import hashlib
import hmac
import math
import time
from typing import Dict, List, Any

class OpenClawGenParkMemoryVault:
    def __init__(self, tenant_secret: str = "openclaw-memory-vault-secret-2026"):
        self.secret = tenant_secret.encode("utf-8")
        # Map: tenant_id -> list of memory records
        self.vault: Dict[str, List[Dict[str, Any]]] = {}

    def _verify_token(self, tenant_id: str, auth_token: str) -> bool:
        expected = hmac.new(self.secret, tenant_id.encode("utf-8"), hashlib.sha256).hexdigest()[:16]
        return hmac.compare_digest(auth_token, expected)

    def generate_auth_token(self, tenant_id: str) -> str:
        return hmac.new(self.secret, tenant_id.encode("utf-8"), hashlib.sha256).hexdigest()[:16]

    def store_memory(self, tenant_id: str, auth_token: str, key: str,
                     content: str, importance: float = 0.5) -> Dict[str, Any]:
        """
        Stores an item in the tenant-isolated memory partition.
        """
        if not self._verify_token(tenant_id, auth_token):
            raise PermissionError("Invalid tenant memory access token")

        if tenant_id not in self.vault:
            self.vault[tenant_id] = []

        record = {
            "key": key,
            "content": content,
            "importance": max(0.1, min(1.0, importance)),
            "created_at": time.time(),
            "access_count": 1
        }
        self.vault[tenant_id].append(record)

        return {
            "stored": True,
            "tenant_id": tenant_id,
            "key": key,
            "total_memories": len(self.vault[tenant_id])
        }

    def query_memory_with_decay(self, tenant_id: str, auth_token: str,
                                query_keyword: str = None) -> List[Dict[str, Any]]:
        """
        Retrieves memories scored by Ebbinghaus retention:
        Score = importance * exp(-delta_hours / 24.0) * log(1 + access_count)
        """
        if not self._verify_token(tenant_id, auth_token):
            raise PermissionError("Invalid tenant memory access token")

        records = self.vault.get(tenant_id, [])
        now = time.time()
        scored = []

        for rec in records:
            if query_keyword and query_keyword.lower() not in rec["content"].lower() and query_keyword.lower() not in rec["key"].lower():
                continue

            delta_hours = (now - rec["created_at"]) / 3600.0
            retention = rec["importance"] * math.exp(-delta_hours / 24.0) * math.log(1.0 + rec["access_count"])
            rec["access_count"] += 1

            scored.append({
                "key": rec["key"],
                "content": rec["content"],
                "retention_score": round(retention, 4),
                "importance": rec["importance"],
                "access_count": rec["access_count"]
            })

        scored.sort(key=lambda x: x["retention_score"], reverse=True)
        return scored
