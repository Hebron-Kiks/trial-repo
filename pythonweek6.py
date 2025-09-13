import requests
import os
from urllib.parse import urlparse
import mimetypes
import hashlib

# Directory for images
SAVE_DIR = "Fetched_Images"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB safety limit
downloaded_hashes = set()  # Prevent duplicates

def sanitize_filename(filename):
    """Prevent directory traversal and sanitize filenames."""
    return os.path.basename(filename).replace("..", "_")

def file_hash(filepath):
    """Compute SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def fetch_image(url):
    try:
        os.makedirs(SAVE_DIR, exist_ok=True)

        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        #  Check Content-Type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (Not an image): {url}")
            return

        #  Check Content-Length
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"✗ Skipped (File too large >10MB): {url}")
            return

        #  Determine filename
        parsed_url = urlparse(url)
        filename = sanitize_filename(os.path.basename(parsed_url.path)) or "downloaded_image"
        extension = mimetypes.guess_extension(content_type.split(";")[0]) or ".jpg"
        if not os.path.splitext(filename)[1]:
            filename += extension

        filepath = os.path.join(SAVE_DIR, filename)

        #  Avoid overwriting by renaming
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            filename = f"{base}_{counter}{ext}"
            filepath = os.path.join(SAVE_DIR, filename)
            counter += 1

        #  Save in chunks & hash
        sha256 = hashlib.sha256()
        size_downloaded = 0
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(8192):
                if not chunk:
                    continue
                size_downloaded += len(chunk)
                if size_downloaded > MAX_FILE_SIZE:
                    print(f"✗ Aborted (Exceeded {MAX_FILE_SIZE} bytes): {url}")
                    f.close()
                    os.remove(filepath)
                    return
                sha256.update(chunk)
                f.write(chunk)

        file_digest = sha256.hexdigest()

        #  Prevent duplicates (check hash)
        if file_digest in downloaded_hashes:
            print(f"✗ Duplicate skipped: {filename}")
            os.remove(filepath)
            return

        downloaded_hashes.add(file_digest)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for safely collecting images from the web\n")

    # Accept multiple URLs at once
    urls = input("Enter one or more image URLs (separate with spaces): ").strip().split()

    for url in urls:
        fetch_image(url)

    print("All downloads attempted. Stay safe and connected 🌍")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye! Exiting gracefully.")
