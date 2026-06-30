import re
import glob

for fname in glob.glob("dist/*.svg"):
    content = open(fname).read()

    h = re.search(r'height="(\d+)"', content)
    if not h:
        continue

    old_h = int(h.group(1))
    new_h = old_h - 35

    content = re.sub(r'height="\d+"', 'height="' + str(new_h) + '"', content, count=1)

    vb = re.search(r'viewBox="([\d. ]+)"', content)
    if vb:
        parts = vb.group(1).split()
        if len(parts) == 4:
            parts[3] = str(new_h)
            content = re.sub(r'viewBox="[\d. ]+"', 'viewBox="' + " ".join(parts) + '"', content)

    open(fname, "w").write(content)
    print("Removed legend from", fname)
