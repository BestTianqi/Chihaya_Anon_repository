import os
import sys

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff', '.tif', '.ico', '.svg'}

def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))

    files = []
    for name in os.listdir(folder):
        _, ext = os.path.splitext(name)
        if ext.lower() in IMAGE_EXTS:
            full = os.path.join(folder, name)
            files.append((os.path.getmtime(full), name, ext))

    files.sort(key=lambda x: x[0])

    if not files:
        print("No image files found.")
        return

    if len(files) > 9999:
        print(f"Too many files: {len(files)} (max 9999)")
        return

    # First pass: rename to temporary names to avoid collisions
    tmp_names = []
    for i, (_, _, ext) in enumerate(files):
        src = os.path.join(folder, files[i][1])
        tmp = os.path.join(folder, f"_tmp_{i:04d}{ext}")
        os.rename(src, tmp)
        tmp_names.append(tmp)

    # Second pass: rename to final names
    for i, (tmp, (_, _, ext)) in enumerate(zip(tmp_names, files)):
        dst = os.path.join(folder, f"{i + 1:04d}{ext}")
        os.rename(tmp, dst)

    print(f"Renamed {len(files)} files.")

if __name__ == '__main__':
    main()
