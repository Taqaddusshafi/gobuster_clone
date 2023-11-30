import sys
import requests
from requests.exceptions import RequestException
from time import sleep

def gobuster(url, wordlist):
    try:
        # Check if the file was not selected
        if not wordlist:
            raise ValueError("Wordlist not provided.")
        
        # Check if the website data is not given
        if not url:
            raise ValueError("Target URL not provided.")

        with open(wordlist, 'r') as file:
            total_paths = sum(1 for _ in file)
            file.seek(0)  # Reset file pointer to the beginning for iteration
            
            for index, line in enumerate(file, start=1):
                path = line.strip()
                full_url = url + '/' + path
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                    response = requests.get(full_url, headers=headers)
                    
                    if response.status_code != 404:
                        print(f"[{response.status_code}] {full_url}")
                    
                    # Show scanning progress
                    print(f"Scanning progress: {index}/{total_paths}", end='\r')

                except RequestException as e:
                    print(f"Error connecting to {full_url}: {e}")
                    
                    # Add a retry mechanism
                    retry_count = 3
                    while retry_count > 0:
                        print(f"Retrying... ({retry_count} attempts left)")
                        sleep(1)  # Add a short delay before retrying
                        try:
                            response = requests.get(full_url, headers=headers)
                            if response.status_code != 404:
                                print(f"[{response.status_code}] {full_url}")
                                break
                        except RequestException as e:
                            print(f"Error on retry: {e}")
                        retry_count -= 1

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nUser exited. Exiting the script.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python custom.py <target_url> <wordlist_path>")
        sys.exit(1)

    target_url = sys.argv[1]
    wordlist_path = sys.argv[2]

    gobuster(target_url, wordlist_path)
