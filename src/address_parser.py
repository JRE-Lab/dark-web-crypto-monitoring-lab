diff --git a/src/address_parser.py b/src/address_parser.py
new file mode 100644
index 0000000000000000000000000000000000000000..b28bbbb3cf0d97932327118875cd24eecc4b6dd5
--- /dev/null
+++ b/src/address_parser.py
@@ -0,0 +1,20 @@
+from __future__ import annotations
+
+import re
+from typing import Iterable
+
+BTC_REGEX = re.compile(r"\b(bc1[0-9a-z]{25,39}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b")
+ETH_REGEX = re.compile(r"\b0x[a-fA-F0-9]{40}\b")
+
+
+def extract_addresses(text: str) -> set[str]:
+    btc_hits = BTC_REGEX.findall(text)
+    eth_hits = ETH_REGEX.findall(text)
+    return {address for address in btc_hits + eth_hits}
+
+
+def collect_from_texts(texts: Iterable[str]) -> set[str]:
+    addresses: set[str] = set()
+    for text in texts:
+        addresses.update(extract_addresses(text))
+    return addresses
