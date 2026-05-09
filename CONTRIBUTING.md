# Contributing Guidelines

Thanks for your interest in contributing! Please follow these rules to help keep the project clean and maintainable.

## 📁 Documentation

- All project documentation should be placed in the `/docs` folder.
- If you write instructions, notes, or guides, please move them there instead of leaving them in source files or root-level scripts.
- To maintain consistency and ensure clear communication among all contributors, **please write all code, comments, documentation, commit messages, and Pull Request descriptions exclusively in English**.  
  This helps keep the project accessible and easy to understand for the entire international community of developers.  
  Thank you for your cooperation!

## ⚙️ Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/example/your-repo-name.git
   cd installable_python_project
   ```

2. Install dependencies using [PDM](https://pdm-project.org/en/latest/):

   ```bash
   pdm install -d
   ```

   > The `-d` flag ensures both regular and development dependencies are installed.

3. You're ready to develop and run the project.

## 🧭 Path Management

To ensure clean, maintainable, and cross-platform-compatible path handling, use `pathlib` instead of `os.path` or `sys.path`. For example:

```python
from pathlib import Path

# Get the current file path
current_file = Path(__file__)

# Navigate to the project root (adjust as needed)
project_root = current_file.parent.parent

# Define a subdirectory path
data_dir = project_root / "data"

# Create the directory if it doesn't exist
data_dir.mkdir(parents=True, exist_ok=True)
```

This approach avoids less readable alternatives like:

```python
import os
import sys

# Get the directory of the current file
base_dir = os.path.dirname(__file__)

# Define the relative path to the 'src' directory
relative_src_path = '../src'

# Create the absolute path to the 'src' directory
src_path = os.path.abspath(os.path.join(base_dir, relative_src_path))

# Insert the 'src' directory at the beginning of sys.path
sys.path.insert(0, src_path)
```

pathlib leads to cleaner, more portable, and idiomatic Python code.

## 🧪 Testing

- All tests must be written and run using **pytest**.
- Ensure your tests cover new features or bug fixes.
- Run `pytest` locally before submitting your Pull Request to verify that everything passes.
- Use descriptive test names and keep tests isolated and independent.

To run tests, use:

```bash
pytest
```

## ✅ Submitting Changes

- Use descriptive commit messages.
- Open a Pull Request with a clear description of your change.
- Link to related issues if applicable.

Thank you for helping improve the project!
