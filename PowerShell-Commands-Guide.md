# PowerShell Commands Reference

## Navigation
- `pwd` - Show current directory path
- `cd <path>` - Change directory
- `cd ..` - Go up one directory
- `ls` or `dir` - List files and folders
- `ls *.py` - List only Python files

## File Operations
- `New-Item <filename>` - Create new file
- `New-Item -ItemType Directory <foldername>` - Create new folder
- `Remove-Item <filename>` - Delete file
- `Remove-Item -Recurse <foldername>` - Delete folder and contents
- `Copy-Item <source> <destination>` - Copy file
- `Move-Item <source> <destination>` - Move/rename file
- `Get-Content <filename>` - Read file contents
- `Set-Content <filename> -Value "text"` - Write to file

## Python & Virtual Environment
- `python --version` - Check Python version
- `py -0` - List all installed Python versions
- `python -m venv .venv` - Create virtual environment
- `.\.venv\Scripts\Activate.ps1` - Activate virtual environment
- `deactivate` - Deactivate virtual environment
- `pip install <package>` - Install Python package
- `pip list` - List installed packages
- `python <filename.py>` - Run Python script

## System Information
- `$env:PATH` - Show PATH environment variable
- `$env:VIRTUAL_ENV` - Show active virtual environment path
- `Get-Command python` - Find where Python executable is located
- `Get-ExecutionPolicy` - Check PowerShell execution policy

## Process Management
- `Get-Process` - List running processes
- `Stop-Process -Name <processname>` - Stop a process
- `Ctrl+C` - Cancel/stop current command

## Useful Shortcuts
- `Tab` - Auto-complete command/path
- `Up Arrow` - Previous command
- `Ctrl+C` - Cancel running command
- `Clear` or `cls` - Clear terminal screen
- `Exit` - Close terminal

## VS Code Specific
- `code .` - Open current folder in VS Code
- `code <filename>` - Open file in VS Code

## Tips
- Use quotes around paths with spaces: `cd "C:\My Folder"`
- Use `\` for paths (not `/` like Linux)
- PowerShell is case-insensitive
- Use `-Force` flag to force operations (e.g., delete without confirmation)
