import yaml, glob, sys

for f in glob.glob("configs/*.yml"):
    try:
        yaml.safe_load(open(f))
        print(f"[OK] {f}")
    except Exception:
        print(f"[ERREUR] {f}")
        sys.exit(1)
