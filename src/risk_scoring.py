diff --git a/src/risk_scoring.py b/src/risk_scoring.py
new file mode 100644
index 0000000000000000000000000000000000000000..51179548cc3d13ce9a0f6b5c444fe4a01327e4a4
--- /dev/null
+++ b/src/risk_scoring.py
@@ -0,0 +1,61 @@
+from __future__ import annotations
+
+from dataclasses import dataclass
+from typing import Iterable
+
+
+@dataclass(frozen=True)
+class AddressRisk:
+    address: str
+    context_count: int
+    tx_count: int
+    incoming_btc: float
+    outgoing_btc: float
+    score: float
+    tier: str
+
+
+def score_address(
+    address: str,
+    contexts: Iterable[str],
+    incoming_btc: float,
+    outgoing_btc: float,
+    tx_count: int,
+) -> AddressRisk:
+    context_count = len(list(contexts))
+    volume = incoming_btc + outgoing_btc
+    score = round((context_count * 1.5) + (tx_count * 1.0) + (volume * 2.0), 2)
+    if score >= 6.0:
+        tier = "High"
+    elif score >= 3.0:
+        tier = "Medium"
+    else:
+        tier = "Low"
+    return AddressRisk(
+        address=address,
+        context_count=context_count,
+        tx_count=tx_count,
+        incoming_btc=incoming_btc,
+        outgoing_btc=outgoing_btc,
+        score=score,
+        tier=tier,
+    )
+
+
+def score_addresses(
+    context_map: dict[str, list[str]],
+    totals: dict[str, dict[str, float]],
+) -> list[AddressRisk]:
+    scored: list[AddressRisk] = []
+    for address, contexts in context_map.items():
+        stats = totals.get(address, {})
+        scored.append(
+            score_address(
+                address,
+                contexts,
+                float(stats.get("incoming_btc", 0.0)),
+                float(stats.get("outgoing_btc", 0.0)),
+                int(stats.get("tx_count", 0)),
+            )
+        )
+    return sorted(scored, key=lambda entry: entry.score, reverse=True)
