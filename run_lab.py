diff --git a/run_lab.py b/run_lab.py
new file mode 100644
index 0000000000000000000000000000000000000000..1fb24f357cea920c0f10802f077f0cf91ba7c7c4
--- /dev/null
+++ b/run_lab.py
@@ -0,0 +1,26 @@
+from __future__ import annotations
+
+import shutil
+from pathlib import Path
+
+from src import collect_osint, generate_report, trace_transactions
+
+
+def main() -> None:
+    repo_root = Path(__file__).resolve().parent
+    output_dir = repo_root / "output"
+
+    if output_dir.exists():
+        shutil.rmtree(output_dir)
+    output_dir.mkdir(parents=True, exist_ok=True)
+
+    collect_osint.main()
+    trace_transactions.main()
+    generate_report.main()
+
+    report_path = output_dir / "risk_report.md"
+    print(f"Report generated: {report_path}")
+
+
+if __name__ == "__main__":
+    main()
