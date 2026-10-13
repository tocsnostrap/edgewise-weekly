"""Check an OpenTimestamps proof against its file without a local Bitcoin node.
    python scripts/ots_check.py <file> <file>.ots
Passes (exit 0, prints the block) only when BOTH hold:
  1. the proof commits to this exact file (its digest is the file's sha256);
  2. at least one Bitcoin attestation in it is real: the merkle root the proof computes equals that block's merkle
     root as reported by two independent explorers (blockstream.info and mempool.space), which must agree.
Exit 2 = still pending (no Bitcoin attestation yet). Exit 1 = anything wrong. Network or explorer trouble is a failure."""
import hashlib, json, sys, urllib.request
from opentimestamps.core.notary import BitcoinBlockHeaderAttestation
from opentimestamps.core.serialize import StreamDeserializationContext
from opentimestamps.core.timestamp import DetachedTimestampFile

EXPLORERS = ("https://blockstream.info/api", "https://mempool.space/api")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "edgewise-weekly-ots-check"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode().strip()


def merkle_root(height):
    roots = set()
    for base in EXPLORERS:
        h = get(f"{base}/block-height/{height}")
        roots.add(json.loads(get(f"{base}/block/{h}"))["merkle_root"])
    if len(roots) != 1: raise RuntimeError(f"explorers disagree on block {height}: {roots}")
    return roots.pop()


def main(path, ots):
    digest = hashlib.sha256(open(path, "rb").read()).digest()
    with open(ots, "rb") as fh: d = DetachedTimestampFile.deserialize(StreamDeserializationContext(fh))
    if d.file_digest != digest:
        print(f"FAIL: the proof is for {d.file_digest.hex()}, the file is {digest.hex()}"); return 1
    btc = [(msg, a) for msg, a in d.timestamp.all_attestations() if isinstance(a, BitcoinBlockHeaderAttestation)]
    if not btc: print("PENDING: no Bitcoin attestation yet"); return 2
    for msg, a in sorted(btc, key=lambda x: x[1].height):
        want = merkle_root(a.height)
        if msg[::-1].hex() == want:
            print(f"OK: {path} sha256 {digest.hex()} is in Bitcoin block {a.height} (merkle root {want})"); return 0
        print(f"mismatch at block {a.height}: proof {msg[::-1].hex()} vs chain {want}")
    print("FAIL: no Bitcoin attestation matched the chain"); return 1


if __name__ == "__main__":
    try: sys.exit(main(sys.argv[1], sys.argv[2]))
    except Exception as e: print(f"FAIL: {type(e).__name__}: {e}"); sys.exit(1)
