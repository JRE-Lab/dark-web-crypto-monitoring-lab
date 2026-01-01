diff --git a/src/trace_transactions.py b/src/trace_transactions.py
new file mode 100644
index 0000000000000000000000000000000000000000..20d8fe812037a3e31f0f3a70a576efc40b265f5e
--- /dev/null
+++ b/src/trace_transactions.py
@@ -0,0 +1,70 @@
+from __future__ import annotations
+
+import csv
+import json
+from collections import defaultdict
+from pathlib import Path
+
+
+def load_transactions(path: Path) -> list[dict[str, str]]:
+    with path.open(newline="", encoding="utf-8") as handle:
+        reader = csv.DictReader(handle)
+        return [row for row in reader]
+
+
+def load_osint_wallets(path: Path) -> dict[str, object]:
+    with path.open(encoding="utf-8") as handle:
+        return json.load(handle)
+
+
+def correlate_transactions(wallets: set[str], transactions: list[dict[str, str]]) -> list[dict[str, str]]:
+    matched: list[dict[str, str]] = []
+    for tx in transactions:
+        if tx["from_address"] in wallets or tx["to_address"] in wallets:
+            matched.append(tx)
+    return matched
+
+
+def summarize_by_address(matched: list[dict[str, str]]) -> dict[str, dict[str, float]]:
+    totals: dict[str, dict[str, float]] = defaultdict(
+        lambda: {"incoming_btc": 0.0, "outgoing_btc": 0.0, "tx_count": 0}
+    )
+    for tx in matched:
+        amount = float(tx["amount_btc"])
+        totals[tx["to_address"]]["incoming_btc"] += amount
+        totals[tx["to_address"]]["tx_count"] += 1
+        totals[tx["from_address"]]["outgoing_btc"] += amount
+        totals[tx["from_address"]]["tx_count"] += 1
+    return dict(totals)
+
+
+def write_output(path: Path, payload: dict[str, object]) -> None:
+    path.parent.mkdir(parents=True, exist_ok=True)
+    with path.open("w", encoding="utf-8") as handle:
+        json.dump(payload, handle, indent=2, sort_keys=True)
+
+
+def main() -> None:
+    repo_root = Path(__file__).resolve().parents[1]
+    osint_path = repo_root / "output" / "osint_addresses.json"
+    tx_path = repo_root / "data" / "sample_blockchain_transactions.csv"
+    output_path = repo_root / "output" / "transaction_summary.json"
+
+    osint_payload = load_osint_wallets(osint_path)
+    wallets = set(osint_payload["wallets"]["all_wallets"])
+
+    transactions = load_transactions(tx_path)
+    matched = correlate_transactions(wallets, transactions)
+    totals = summarize_by_address(matched)
+
+    write_output(
+        output_path,
+        {
+            "matched_transactions": matched,
+            "totals_by_address": totals,
+        },
+    )
+
+
+if __name__ == "__main__":
+    main()
