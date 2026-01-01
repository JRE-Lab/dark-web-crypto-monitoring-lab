diff --git a/output/risk_report.md b/output/risk_report.md
new file mode 100644
index 0000000000000000000000000000000000000000..ba56823ba0cb084376dcb9e95c657e33a2d90574
--- /dev/null
+++ b/output/risk_report.md
@@ -0,0 +1,46 @@
+# Dark-Web Crypto Monitoring Lab Report
+
+Generated: 2025-12-31 09:23:12Z
+
+## Observed Wallets
+Total wallets observed: 5
+
+- `0x9bA0f7C2e5dD8fB20a2D8F5F9b3c6e7A1b2C3d4E` — Forum post P-903 (cinderfox); Listing L-1003 (SilverHaze)
+- `1JpY6bZ2qJ3GmP9Yp1FQzT1k9t5sYzT2b1` — Forum post P-901 (voidsignal); Listing L-1002 (IronKrait)
+- `3Eo1f3J3wLkz4ZQy2YJ5dZ4M1xV9h7J8J9` — Forum post P-903 (cinderfox); Listing L-1004 (NoirCobalt)
+- `bc1q2g2y5kpy0nsc5k8v4n7z9t7p5v0p0u2d3k9m4a` — Forum post P-902 (neondrift); Listing L-1001 (ShadowLotus)
+- `bc1q6l2l9ts2q9l9h4p0m7w8m8c9r8g2s2f4x5v6w7` — Listing L-1005 (CrimsonEcho)
+
+## Matched Transactions
+Total matched transactions: 5
+
+| Tx ID | From | To | Amount (BTC) | Timestamp | Notes |
+| --- | --- | --- | --- | --- | --- |
+| TX-0001 | `bc1q2g2y5kpy0nsc5k8v4n7z9t7p5v0p0u2d3k9m4a` | `3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5` | 0.18 | 2024-05-13T15:10:00Z | Listing payment |
+| TX-0002 | `1JpY6bZ2qJ3GmP9Yp1FQzT1k9t5sYzT2b1` | `3Eo1f3J3wLkz4ZQy2YJ5dZ4M1xV9h7J8J9` | 0.42 | 2024-05-14T10:01:22Z | Vendor payout |
+| TX-0003 | `3Eo1f3J3wLkz4ZQy2YJ5dZ4M1xV9h7J8J9` | `bc1q6l2l9ts2q9l9h4p0m7w8m8c9r8g2s2f4x5v6w7` | 0.11 | 2024-05-14T21:55:04Z | Affiliate share |
+| TX-0004 | `bc1q6l2l9ts2q9l9h4p0m7w8m8c9r8g2s2f4x5v6w7` | `1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY` | 0.07 | 2024-05-15T08:30:00Z | Funds consolidation |
+| TX-0005 | `1JpY6bZ2qJ3GmP9Yp1FQzT1k9t5sYzT2b1` | `bc1q2g2y5kpy0nsc5k8v4n7z9t7p5v0p0u2d3k9m4a` | 0.05 | 2024-05-16T12:05:45Z | Refund flow |
+
+## Address Flow Summary
+
+| Address | Incoming (BTC) | Outgoing (BTC) | Tx Count |
+| --- | --- | --- | --- |
+| `1JpY6bZ2qJ3GmP9Yp1FQzT1k9t5sYzT2b1` | 0.0000 | 0.4700 | 2 |
+| `1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY` | 0.0700 | 0.0000 | 1 |
+| `3Eo1f3J3wLkz4ZQy2YJ5dZ4M1xV9h7J8J9` | 0.4200 | 0.1100 | 2 |
+| `3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5` | 0.1800 | 0.0000 | 1 |
+| `bc1q2g2y5kpy0nsc5k8v4n7z9t7p5v0p0u2d3k9m4a` | 0.0500 | 0.1800 | 2 |
+| `bc1q6l2l9ts2q9l9h4p0m7w8m8c9r8g2s2f4x5v6w7` | 0.1100 | 0.0700 | 2 |
+
+## Risk Scoring
+
+Scores blend OSINT context count, transaction count, and total BTC volume.
+
+| Address | Contexts | Tx Count | Incoming (BTC) | Outgoing (BTC) | Score | Tier |
+| --- | --- | --- | --- | --- | --- | --- |
+| `3Eo1f3J3wLkz4ZQy2YJ5dZ4M1xV9h7J8J9` | 2 | 2 | 0.4200 | 0.1100 | 6.06 | High |
+| `1JpY6bZ2qJ3GmP9Yp1FQzT1k9t5sYzT2b1` | 2 | 2 | 0.0000 | 0.4700 | 5.94 | Medium |
+| `bc1q2g2y5kpy0nsc5k8v4n7z9t7p5v0p0u2d3k9m4a` | 2 | 2 | 0.0500 | 0.1800 | 5.46 | Medium |
+| `bc1q6l2l9ts2q9l9h4p0m7w8m8c9r8g2s2f4x5v6w7` | 1 | 2 | 0.1100 | 0.0700 | 3.86 | Medium |
+| `0x9bA0f7C2e5dD8fB20a2D8F5F9b3c6e7A1b2C3d4E` | 2 | 0 | 0.0000 | 0.0000 | 3.00 | Medium |
