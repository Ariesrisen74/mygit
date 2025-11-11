"""
Core Git wrapper functionality
"""
import subprocess
import sys
from .colors import Colors


class GitWrapper:
    """Base class for Git operations"""

    def __init__(self):
        self.check_git_installed()

    def run_command(self, command, capture_output=False, check_error=True):
        """Execute a shell command"""
        try:
            if capture_output:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=check_error
                )
                return result.stdout.strip()
            else:
                result = subprocess.run(command, shell=True, check=check_error)
                return result.returncode == 0
        except subprocess.CalledProcessError as e:
            if check_error:
                self.print_error(f"Command execution error: {e}")
            return None

    def check_git_installed(self):
        """Check if Git is installed"""
        result = self.run_command("git --version", capture_output=True, check_error=False)
        if result is None:
            self.print_error("Git is not installed! Please install Git and try again.")
            sys.exit(1)

    def is_git_repo(self):
        """Check if we're inside a Git repository"""
        result = self.run_command(
            "git rev-parse --is-inside-work-tree",
            capture_output=True,
            check_error=False
        )
        return result == "true"

    def get_current_branch(self):
        """Get current branch name"""
        return self.run_command("git branch --show-current", capture_output=True)

    def get_repo_status(self):
        """Get repository status"""
        return self.run_command("git status --short", capture_output=True)

    def get_changed_files(self):
        """Get list of changed files with their status
        Returns a list of tuples: [(status, filepath), ...]
        Status codes: M=modified, A=added, D=deleted, ??=untracked, etc.
        """
        status_output = self.run_command("git status --porcelain", capture_output=True)
        if not status_output:
            return []

        files = []
        for line in status_output.split('\n'):
            if line.strip():
                # Format: 'XY filename' where X and Y are status codes (2 chars)
                # Then comes space(s), then filename
                status = line[:2]
                # Take everything after status and strip leading spaces
                filepath = line[2:].lstrip()
                files.append((status, filepath))

        return files

    def select_files_interactive(self):
        """Interactive file selection
        Returns list of selected file paths, or None if cancelled/no files
        """
        files = self.get_changed_files()
        if not files:
            return None

        print(f"\n{Colors.BOLD}Changed files:{Colors.ENDC}")

        # Display files with numbers
        status_symbols = {
            'M': f"{Colors.CYAN}[M]{Colors.ENDC}",  # Modified
            'A': f"{Colors.GREEN}[A]{Colors.ENDC}",  # Added
            'D': f"{Colors.FAIL}[D]{Colors.ENDC}",   # Deleted
            '??': f"{Colors.WARNING}[?]{Colors.ENDC}",  # Untracked
            'R': f"{Colors.CYAN}[R]{Colors.ENDC}",   # Renamed
        }

        for i, (status, filepath) in enumerate(files, 1):
            # Remove spaces from status for cleaner display
            clean_status = status.strip()
            status_symbol = status_symbols.get(clean_status, f"[{clean_status}]")
            print(f"  {Colors.BOLD}{i}.{Colors.ENDC} {status_symbol} {filepath}")

        print(f"\n{Colors.BOLD}Select files to add:{Colors.ENDC}")
        print(f"  - Enter numbers separated by spaces (e.g., 1 3 5)")
        print(f"  - Enter 'a' or 'all' to select all files")
        print(f"  - Enter '0' to cancel")

        selection = input(f"\n{Colors.CYAN}Your selection: {Colors.ENDC}").strip().lower()

        if selection == '0':
            return None

        if selection in ['a', 'all']:
            return [filepath for _, filepath in files]

        # Parse individual selections
        try:
            indices = [int(x.strip()) for x in selection.split()]
            selected_files = []

            for idx in indices:
                if 1 <= idx <= len(files):
                    selected_files.append(files[idx - 1][1])
                else:
                    self.print_warning(f"Invalid number: {idx}")

            if not selected_files:
                self.print_error("No valid files selected!")
                return None

            return selected_files
        except ValueError:
            self.print_error("Invalid input format!")
            return None

    # Print utilities
    def print_header(self, text):
        """Print header"""
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.ENDC}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")

    def print_success(self, text):
        """Print success message"""
        print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")

    def print_error(self, text):
        """Print error message"""
        print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

    def print_info(self, text):
        """Print info message"""
        print(f"{Colors.CYAN}ℹ {text}{Colors.ENDC}")

    def print_warning(self, text):
        """Print warning message"""
        print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")
