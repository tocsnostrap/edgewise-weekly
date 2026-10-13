"""Exit 0 only if <proof.ots> is a detached OpenTimestamps proof for the sha256 <hex> (header check, no library).
    python scripts/ots_digest.py proof.ots <sha256 hex>"""
import sys
MAGIC = b"\x00OpenTimestamps\x00\x00Proof\x00\xbf\x89\xe2\xe8\x84\xe8\x92\x94"
d = open(sys.argv[1], "rb").read(); want = bytes.fromhex(sys.argv[2])
ok = d[:len(MAGIC)] == MAGIC and d[len(MAGIC)] == 1 and d[len(MAGIC) + 1] == 0x08 and d[len(MAGIC) + 2:len(MAGIC) + 34] == want
print("proof digest", "matches" if ok else "DOES NOT match", sys.argv[2]); sys.exit(0 if ok else 1)
