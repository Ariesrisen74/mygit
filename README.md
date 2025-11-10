# MyGit - Convenient Git Wrapper

A user-friendly command-line wrapper for Git that simplifies common Git operations with an interactive menu interface.

## Author
Oleksandr Izotov

## Features

- 🚀 **Full Sync** - Add, commit, and push in one command
- 💾 **Quick Commit** - Add and commit without pushing
- 🆕 **Project Initialization** - Initialize new Git projects with .gitignore
- 📥 **Clone Repository** - Easy repository cloning
- 🔄 **Pull Changes** - Quick pull from remote
- ↩️ **Reset Changes** - Reset or clean working directory
- 📊 **Status Display** - View repository status
- 📁 **Directory Navigation** - Navigate between projects easily

## Project Structure

```
mygit-project/
├── mygit/
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
└── .gitignore               # Git ignore rules
```

## Installation

### Option 1: Run directly from project directory
```bash
cd ~/mygit-project
python3 mygit.py
```

### Option 2: Run as Python module
```bash
cd ~/mygit-project
python3 -m mygit
```

### Option 3: Create an alias (recommended)
Add to your `~/.bashrc`:
```bash
alias mygit='python3 ~/mygit-project/mygit.py'
```
Then reload:
```bash
source ~/.bashrc
```

Now you can run `mygit` from anywhere!

### Option 4: Install globally
```bash
sudo ln -s ~/mygit-project/mygit.py /usr/local/bin/mygit
```

## Usage

Simply run the program and follow the interactive menu:

```bash
mygit
```

### Quick Links
The navigation feature includes quick links to:
- `~/personal` - Personal projects
- `~/university` - University projects
- `~/ (Home)` - Home directory
- `~/Documents` - Documents folder

### Example Workflow

1. Navigate to your project directory (option 8)
2. Make changes to your code
3. Choose "Full sync" (option 1)
4. Enter commit message
5. Done! Changes are added, committed, and pushed

## Requirements

- Python 3.6+
- Git

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
