# Lyntr Username Checker

A simple Python script to check if usernames are claimed or unclaimed on Lyntr.

## Description

This script checks if usernames are available on Lyntr by querying their API. It reads a list of usernames from a file, checks each username, and outputs the results to a text file. The script also provides color-coded terminal output to indicate the status of each username.

## Features

- Check if a username is claimed or unclaimed.
- Save results to a text file.
- Color-coded terminal output for easy reading.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vanvansz/lyntr-username-checker.git
   cd lyntr-username-checker
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests colorama
   ```

## Usage

1. **Prepare a List of Usernames**:

   Create/find a wordlist file with one username per line(e.g., `wordlist.txt`).

2. **Run the Script**:
   ```bash
   python checker.py
   ```

3. **Follow the Prompt**:

   Enter the path to the wordlist file when prompted.

4. **View Results**:

   The results will be saved in `results.txt` with each username and its status.

## Example
```bash
Enter the path to the usernames file: wordlist.txt
Username checking complete. Results saved to results.txt.
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Made by

Made by lxckwyd on Discord.
