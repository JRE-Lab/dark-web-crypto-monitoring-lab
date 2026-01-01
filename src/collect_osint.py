diff --git a/src/collect_osint.py b/src/collect_osint.py
new file mode 100644
index 0000000000000000000000000000000000000000..cc683d37fb28e34f5618037b03c00e0d19228824
--- /dev/null
+++ b/src/collect_osint.py
@@ -0,0 +1,79 @@
+from __future__ import annotations
+
+import csv
+import json
+from pathlib import Path
+
+from src.address_parser import collect_from_texts, extract_addresses
+
+
+def load_marketplace_listings(path: Path) -> list[dict[str, str]]:
+    with path.open(newline="", encoding="utf-8") as handle:
+        reader = csv.DictReader(handle)
+        return [row for row in reader]
+
+
+def load_forum_posts(path: Path) -> list[dict[str, str]]:
+    posts: list[dict[str, str]] = []
+    with path.open(encoding="utf-8") as handle:
+        for line in handle:
+            if line.strip():
+                posts.append(json.loads(line))
+    return posts
+
+
+def collect_wallets(listings: list[dict[str, str]], posts: list[dict[str, str]]) -> dict[str, list[str]]:
+    listing_wallets = collect_from_texts([listing["wallet_address"] for listing in listings])
+    post_wallets = collect_from_texts([post["content"] for post in posts])
+    all_wallets = sorted(listing_wallets.union(post_wallets))
+    return {
+        "listing_wallets": sorted(listing_wallets),
+        "post_wallets": sorted(post_wallets),
+        "all_wallets": all_wallets,
+    }
+
+
+def collect_context_map(listings: list[dict[str, str]], posts: list[dict[str, str]]) -> dict[str, list[str]]:
+    context: dict[str, list[str]] = {}
+    for listing in listings:
+        addresses = extract_addresses(listing["wallet_address"])
+        for address in addresses:
+            context.setdefault(address, []).append(
+                f"Listing {listing['listing_id']} ({listing['vendor']})"
+            )
+    for post in posts:
+        addresses = extract_addresses(post["content"])
+        for address in addresses:
+            context.setdefault(address, []).append(f"Forum post {post['post_id']} ({post['author']})")
+    return {key: sorted(set(values)) for key, values in context.items()}
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
+    listings_path = repo_root / "data" / "sample_marketplace_listings.csv"
+    posts_path = repo_root / "data" / "sample_forum_posts.jsonl"
+    output_path = repo_root / "output" / "osint_addresses.json"
+
+    listings = load_marketplace_listings(listings_path)
+    posts = load_forum_posts(posts_path)
+
+    wallets = collect_wallets(listings, posts)
+    context = collect_context_map(listings, posts)
+
+    write_output(
+        output_path,
+        {
+            "wallets": wallets,
+            "context": context,
+        },
+    )
+
+
+if __name__ == "__main__":
+    main()
