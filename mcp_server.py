# -*- coding: utf-8 -*-
import sys, json
from client import OpenClawGenParkMemoryVault

vault = OpenClawGenParkMemoryVault()

def run_tool(name, args):
    if name == "generate_auth_token":
        t_id = args.get("tenant_id", "default_agent")
        return {"token": vault.generate_auth_token(t_id)}
    elif name == "store_memory":
        t_id = args.get("tenant_id", "")
        tok = args.get("auth_token", "")
        k = args.get("key", "")
        c = args.get("content", "")
        imp = float(args.get("importance", 0.5))
        return vault.store_memory(t_id, tok, k, c, imp)
    elif name == "query_memory_with_decay":
        t_id = args.get("tenant_id", "")
        tok = args.get("auth_token", "")
        kw = args.get("query_keyword", None)
        return {"results": vault.query_memory_with_decay(t_id, tok, kw)}
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running OpenClaw Memory Vault Self-Test...")
        t_id = "agent_x"
        tok = vault.generate_auth_token(t_id)
        s = vault.store_memory(t_id, tok, "pref", "User likes dark mode", 0.9)
        assert s["stored"] is True
        res = vault.query_memory_with_decay(t_id, tok, "dark")
        assert len(res) == 1
        assert res[0]["key"] == "pref"
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
