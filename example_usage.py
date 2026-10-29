# -*- coding: utf-8 -*-
from client import OpenClawGenParkMemoryVault

def main():
    vault = OpenClawGenParkMemoryVault()
    print("=== OpenClaw GenPark Memory Vault ===")

    tenant = "ecommerce_advisor_agent"
    token = vault.generate_auth_token(tenant)

    # Store customer long-term memories
    vault.store_memory(tenant, token, "cust_001_budget", "Maximum budget $1500 for laptop", importance=0.85)
    vault.store_memory(tenant, token, "cust_001_brand", "Prefers lightweight ASUS or Apple models", importance=0.9)
    vault.store_memory(tenant, token, "cust_001_temp", "Currently browsing from hotel WiFi", importance=0.2)

    # Query recall with retention decay
    memories = vault.query_memory_with_decay(tenant, token, query_keyword="budget")
    print("Recalled Memories for 'budget':")
    for m in memories:
        print(f"  [{m['key']}]: '{m['content']}' (RetentionScore={m['retention_score']})")

if __name__ == "__main__":
    main()
