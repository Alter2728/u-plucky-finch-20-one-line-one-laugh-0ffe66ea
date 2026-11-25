import os

TEXT = "My to-do list is just a guilt museum with excellent lighting."


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert 1 <= len(content) <= 200, len(content)
    assert "\n" not in content and "\r" not in content
    assert content.strip()


if __name__ == "__main__":
    main()
