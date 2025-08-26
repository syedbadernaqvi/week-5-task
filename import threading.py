import threading
import requests
import time

# List of 5 URLs to download
urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.openai.com",
    "https://www.github.com"
]

def download_url(url, filename):
    response = requests.get(url)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Downloaded {url} -> {filename}")

start = time.time()
threads = []

# Start threads
for i, url in enumerate(urls):
    t = threading.Thread(target=download_url, args=(url, f"file_{i}.html"))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")