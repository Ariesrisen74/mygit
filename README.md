# MyGit - Convenient Git Wrapper

A user-friendly command-line wrapper for Git that simplifies common Git operations with an interactive menu interface.

## Author
Oleksandr Izotov

## Features

- 🚀 **Full Sync** - Add, commit, and push in one command with **interactive file selection**
- 💾 **Quick Commit** - Add and commit without pushing with **interactive file selection**
- ✅ **Interactive File Picker** - Select files using arrow keys and checkboxes (Space to toggle, Enter to confirm)
- 🆕 **Project Initialization** - Initialize new Git projects with .gitignore
- 📥 **Clone Repository** - Easy repository cloning
- 🔄 **Pull Changes** - Quick pull from remote
- ↩️ **Reset Changes** - Reset or clean working directory
- 📊 **Status Display** - View repository status
- 📁 **Directory Navigation** - Navigate between projects easily

## Project Structure

```
mygit/                        # Root project directory
├── mygit/                    # Main package directory
│   ├── __init__.py           # Package initialization
│   ├── __main__.py           # Entry point for python -m mygit
│   ├── colors.py             # ANSI color codes
│   ├── git_wrapper.py        # Core Git wrapper functionality
│   ├── ui.py                 # User interface and menu
│   └── commands/             # Command modules
│       ├── __init__.py
│       ├── sync.py           # Sync commands (commit, push, pull)
│       ├── repository.py     # Repository management
│       ├── status.py         # Status commands
│       └── navigation.py     # Directory navigation
├── mygit.py                  # Main executable script
├── README.md                 # This file
└── .gitignore                # Git ignore rules
```

## Installation

First, clone or download this repository:
```bash
git clone <repository-url>
cd mygit
```

Install required Python packages:
```bash
pip3 install -r requirements.txt
```

### Option 1: Run directly from project directory
```bash
# Navigate to the project directory
cd /path/to/mygit
python3 mygit.py
```

### Option 2: Run as Python module
```bash
cd /path/to/mygit
python3 -m mygit
```

### Option 3: Create an alias (recommended for convenience)
Add to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
# Replace /path/to/mygit with the actual absolute path to the project
alias mygit='python3 /path/to/mygit/mygit.py'
```

Then reload your shell configuration:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

Now you can run `mygit` from anywhere!

### Option 4: Install globally with symbolic link
This makes the command available system-wide:

```bash
# First, get the absolute path to mygit.py
cd /path/to/mygit
pwd  # This shows the absolute path

# Create symbolic link (replace with your actual path)
sudo ln -s /absolute/path/to/mygit/mygit.py /usr/local/bin/mygit

# Example: if your project is in /home/username/projects/mygit
# sudo ln -s /home/username/projects/mygit/mygit.py /usr/local/bin/mygit
```

**Important**: Use the full absolute path, not `~` (tilde), as it may not expand correctly with `sudo`.

To verify the installation:
```bash
mygit --help  # Should show the program
```

If you need to remove or fix the link:
```bash
sudo rm /usr/local/bin/mygit
```

## Usage

Simply run the program and follow the interactive menu:

```bash
mygit
```

### Quick Links
The navigation feature includes customizable quick links. You can modify them in `mygit/commands/navigation.py` to match your directory structure. Default examples:
- Personal projects folder
- University/work projects folder
- Home directory
- Documents folder

To customize, edit the `navigate_directory()` function in `navigation.py`.

### Example Workflow

1. Navigate to your project directory (option 8)
2. Make changes to your code
3. Choose "Full sync" (option 1)
4. **Select files interactively**:
   - Use ↑/↓ arrow keys to navigate
   - Press Space to select/deselect files
   - Press Enter to confirm selection
5. Enter commit message
6. Done! Selected files are added, committed, and pushed

### Interactive File Selection

When you choose "Full sync" or "Just commit", you'll see an interactive menu like this:

```
Select files to add:
Use ↑/↓ arrows to navigate, Space to select, Enter to confirm

❯ ◯ [M] mygit/commands/sync.py
  ◉ [M] mygit/git_wrapper.py
  ◯ [?] new_file.txt
```

- **Arrow keys** (↑/↓) - Navigate through files
- **Space** - Toggle file selection (◯ = unselected, ◉ = selected)
- **Enter** - Confirm selection and proceed
- **Ctrl+C** - Cancel operation

Status indicators:
- `[M]` - Modified file
- `[A]` - Added/staged file
- `[D]` - Deleted file
- `[?]` - Untracked/new file
- `[R]` - Renamed file

## Requirements

- Python 3.6+
- Git
- Python packages (install via `pip3 install -r requirements.txt`):
  - inquirer>=3.4.0 (for interactive file selection)

## Clean Code Principles

This project follows clean code principles:
- **Separation of Concerns**: Commands, UI, and core functionality are separated
- **Single Responsibility**: Each module has a single, well-defined purpose
- **DRY (Don't Repeat Yourself)**: Common functionality is centralized
- **Modularity**: Easy to extend with new commands
- **Readability**: Clear naming and documentation

## License

Free to use and modify for personal and educational purposes.

## Contributing

This is a personal project, but suggestions are welcome!
