diff --git a/src/generate_report.py b/src/generate_report.py
new file mode 100644
index 0000000000000000000000000000000000000000..67f0aaf985ad5b8b003a2289db845f9f6b9c8b06
--- /dev/null
+++ b/src/generate_report.py
@@ -0,0 +1,111 @@
+from __future__ import annotations
+
+import json
+from datetime import datetime, timezone
+from pathlib import Path
+
+from src.risk_scoring import score_addresses
+
+
+def load_json(path: Path) -> dict[str, object]:
+    with path.open(encoding="utf-8") as handle:
+        return json.load(handle)
+
+
+def format_totals(totals: dict[str, dict[str, float]]) -> list[str]:
+    rows: list[str] = []
+    for address, amounts in sorted(totals.items()):
+        incoming = amounts.get("incoming_btc", 0.0)
+        outgoing = amounts.get("outgoing_btc", 0.0)
+        tx_count = int(amounts.get("tx_count", 0))
+        rows.append(f"| `{address}` | {incoming:.4f} | {outgoing:.4f} | {tx_count} |")
+    return rows
+
+
+def main() -> None:
+    repo_root = Path(__file__).resolve().parents[1]
+    osint_path = repo_root / "output" / "osint_addresses.json"
+    summary_path = repo_root / "output" / "transaction_summary.json"
+    report_path = repo_root / "output" / "risk_report.md"
+
+    osint_payload = load_json(osint_path)
+    summary_payload = load_json(summary_path)
+
+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
+    wallets = osint_payload["wallets"]["all_wallets"]
+    totals = summary_payload["totals_by_address"]
+    matched = summary_payload["matched_transactions"]
+    scored = score_addresses(osint_payload["context"], totals)
+
+    lines = [
+        "# Dark-Web Crypto Monitoring Lab Report",
+        "",
+        f"Generated: {timestamp}",
+        "",
+        "## Observed Wallets",
+        f"Total wallets observed: {len(wallets)}",
+        "",
+    ]
+    for wallet in wallets:
+        context = osint_payload["context"].get(wallet, [])
+        context_str = "; ".join(context) if context else "No context"
+        lines.append(f"- `{wallet}` — {context_str}")
+
+    lines.extend(
+        [
+            "",
+            "## Matched Transactions",
+            f"Total matched transactions: {len(matched)}",
+            "",
+            "| Tx ID | From | To | Amount (BTC) | Timestamp | Notes |",
+            "| --- | --- | --- | --- | --- | --- |",
+        ]
+    )
+
+    for tx in matched:
+        lines.append(
+            "| {tx_id} | `{from_address}` | `{to_address}` | {amount_btc} | {timestamp} | {notes} |".format(
+                **tx
+            )
+        )
+
+    lines.extend(
+        [
+            "",
+            "## Address Flow Summary",
+            "",
+            "| Address | Incoming (BTC) | Outgoing (BTC) | Tx Count |",
+            "| --- | --- | --- | --- |",
+        ]
+    )
+    lines.extend(format_totals(totals))
+
+    lines.extend(
+        [
+            "",
+            "## Risk Scoring",
+            "",
+            "Scores blend OSINT context count, transaction count, and total BTC volume.",
+            "",
+            "| Address | Contexts | Tx Count | Incoming (BTC) | Outgoing (BTC) | Score | Tier |",
+            "| --- | --- | --- | --- | --- | --- | --- |",
+        ]
+    )
+    for entry in scored:
+        lines.append(
+            "| {address} | {context_count} | {tx_count} | {incoming_btc:.4f} | {outgoing_btc:.4f} | {score:.2f} | {tier} |".format(
+                address=f"`{entry.address}`",
+                context_count=entry.context_count,
+                tx_count=entry.tx_count,
+                incoming_btc=entry.incoming_btc,
+                outgoing_btc=entry.outgoing_btc,
+                score=entry.score,
+                tier=entry.tier,
+            )
+        )
+
+    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
+
+
+if __name__ == "__main__":
+    main()
