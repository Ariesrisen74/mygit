"""
Synchronization commands (commit, push, pull)
"""
from ..colors import Colors


class SyncCommands:
    """Git synchronization commands"""

    def full_sync(self, wrapper):
        """Full synchronization: add + commit + push"""
        wrapper.print_header("FULL SYNCHRONIZATION")

        if not wrapper.is_git_repo():
            wrapper.print_error("This is not a Git repository!")
            return

        # Show status
        from .status import StatusCommands
        StatusCommands().show_status(wrapper)

        # Check if there are changes
        status = wrapper.get_repo_status()
        if not status:
            wrapper.print_warning("No changes to commit")
            return

        # Select files to add using interactive checkbox menu
        selected_files = wrapper.select_files_checkbox()
        if selected_files is None or len(selected_files) == 0:
            wrapper.print_info("Operation cancelled or no files selected")
            return

        # Get commit message
        print(f"\n{Colors.BOLD}Enter commit message:{Colors.ENDC}")
        commit_msg = input(f"{Colors.CYAN}> {Colors.ENDC}").strip()

        if not commit_msg:
            wrapper.print_error("Commit message cannot be empty!")
            return

        # Execute operations
        print()
        wrapper.print_info("Adding selected files...")

        # Add files one by one with proper escaping
        for file in selected_files:
            # Escape file path for shell
            escaped_file = file.replace('"', '\\"')
            if not wrapper.run_command(f'git add "{escaped_file}"'):
                wrapper.print_error(f"Failed to add: {file}")
                return

        wrapper.print_success(f"Added {len(selected_files)} file(s)")

        wrapper.print_info("Creating commit...")
        # Escape commit message
        escaped_msg = commit_msg.replace('"', '\\"')
        if not wrapper.run_command(f'git commit -m "{escaped_msg}"'):
            return

        wrapper.print_info("Pushing to remote...")
        if wrapper.run_command("git push"):
            wrapper.print_success("Full synchronization completed!")
        else:
            wrapper.print_warning("Push failed. You might need to pull first?")

    def just_commit(self, wrapper):
        """Just commit: add + commit"""
        wrapper.print_header("CREATE COMMIT")

        if not wrapper.is_git_repo():
            wrapper.print_error("This is not a Git repository!")
            return

        # Show status
        from .status import StatusCommands
        StatusCommands().show_status(wrapper)

        # Check if there are changes
        status = wrapper.get_repo_status()
        if not status:
            wrapper.print_warning("No changes to commit")
            return

        # Select files to add using interactive checkbox menu
        selected_files = wrapper.select_files_checkbox()
        if selected_files is None or len(selected_files) == 0:
            wrapper.print_info("Operation cancelled or no files selected")
            return

        # Get commit message
        print(f"\n{Colors.BOLD}Enter commit message:{Colors.ENDC}")
        commit_msg = input(f"{Colors.CYAN}> {Colors.ENDC}").strip()

        if not commit_msg:
            wrapper.print_error("Commit message cannot be empty!")
            return

        # Execute operations
        print()
        wrapper.print_info("Adding selected files...")

        # Add files one by one with proper escaping
        for file in selected_files:
            # Escape file path for shell
            escaped_file = file.replace('"', '\\"')
            if not wrapper.run_command(f'git add "{escaped_file}"'):
                wrapper.print_error(f"Failed to add: {file}")
                return

        wrapper.print_success(f"Added {len(selected_files)} file(s)")

        wrapper.print_info("Creating commit...")
        # Escape commit message
        escaped_msg = commit_msg.replace('"', '\\"')
        if wrapper.run_command(f'git commit -m "{escaped_msg}"'):
            wrapper.print_success("Commit created!")

    def pull_changes(self, wrapper):
        """Pull changes"""
        wrapper.print_header("PULL CHANGES")

        if not wrapper.is_git_repo():
            wrapper.print_error("This is not a Git repository!")
            return

        branch = wrapper.get_current_branch()
        wrapper.print_info(f"Pulling changes for branch {branch}...")

        if wrapper.run_command("git pull"):
            wrapper.print_success("Changes pulled successfully!")

    def reset_changes(self, wrapper):
        """Reset changes"""
        wrapper.print_header("RESET CHANGES")

        if not wrapper.is_git_repo():
            wrapper.print_error("This is not a Git repository!")
            return

        # Show status
        from .status import StatusCommands
        StatusCommands().show_status(wrapper)

        print(f"\n{Colors.WARNING}WARNING! This will discard all uncommitted changes!{Colors.ENDC}")
        print(f"{Colors.BOLD}Choose action:{Colors.ENDC}")
        print(f"  1. Reset file changes (git reset --hard)")
        print(f"  2. Remove untracked files (git clean -fd)")
        print(f"  3. Do both")
        print(f"  0. Cancel")

        choice = input(f"\n{Colors.CYAN}Your choice: {Colors.ENDC}").strip()

        if choice == "1":
            if wrapper.run_command("git reset --hard"):
                wrapper.print_success("Changes reset!")
        elif choice == "2":
            if wrapper.run_command("git clean -fd"):
                wrapper.print_success("Untracked files removed!")
        elif choice == "3":
            if wrapper.run_command("git reset --hard") and wrapper.run_command("git clean -fd"):
                wrapper.print_success("All changes reset and untracked files removed!")
        elif choice == "0":
            wrapper.print_info("Cancelled")
        else:
            wrapper.print_error("Invalid choice!")
