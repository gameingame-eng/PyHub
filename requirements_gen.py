import os
import ast
import sys
import pkgutil
import importlib.util

# -----------------------------
# Detect standard library modules
# -----------------------------
def get_stdlib_modules():
    stdlib = set(sys.builtin_module_names)
    for _, name, _ in pkgutil.iter_modules():
        try:
            spec = importlib.util.find_spec(name)
            if spec and "site-packages" not in (spec.origin or ""):
                stdlib.add(name)
        except Exception:
            pass
    return stdlib

STDLIB = get_stdlib_modules()

# -----------------------------
# Extract imports from a file
# -----------------------------
def extract_imports_from_file(path):
    imports = set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=path)
    except Exception:
        return imports

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])

    return imports

# -----------------------------
# Walk the repo and collect imports
# -----------------------------
def scan_repo(root="."):
    all_imports = set()
    for folder, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(folder, file)
                all_imports |= extract_imports_from_file(path)
    return all_imports

# -----------------------------
# Filter out stdlib + local modules
# -----------------------------
def filter_external(imports):
    external = set()
    for module in imports:
        if module in STDLIB:
            continue
        if os.path.isdir(module):
            continue
        external.add(module)
    return external

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    imports = scan_repo(".")
    external = sorted(filter_external(imports))

    print("\nDetected external dependencies:\n")
    for dep in external:
        print(dep)

    # Write to requirements.txt
    with open("requirements.txt", "w", encoding="utf-8") as f:
        for dep in external:
            f.write(dep + "\n")

    print("\nrequirements.txt updated successfully.\n")
