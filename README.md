# Custom Gobuster/Gobuster Clone

Custom Gobuster is a Python script for scanning a target URL with a wordlist to discover existing paths. It uses the requests library to make HTTP requests and provides a simple retry mechanism for failed connections.

## Features

- Scans a target URL with a specified wordlist
- Handles errors and retries failed connections
- Displays scanning progress
- User-friendly exit on Ctrl+C (KeyboardInterrupt)

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/custom-gobuster.git
    cd custom-gobuster
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python custom.py <target_url> <wordlist_path>

