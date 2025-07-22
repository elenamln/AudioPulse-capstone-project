import os
import bda_boilerplate
import threading
from pathlib import Path
from datetime import datetime
import concurrent.futures

def load_url_list(file_path):
	"""Load YouTube URLs from a text file into a list."""
	try:
		with open(file_path) as f:
			return [line.strip() for line in f]
	except FileNotFoundError:
		print(f"File not found: {file_path}")
		return [] #return an empty list if the file is not found

def download_youtube_audio_with_metadata(url: str):
	"""Main function to download audio and save metadata."""
	print(f"\n🎵 Downloading: {url}")
	retry = 1
	while True:
		try:
			info = bda_boilerplate.get_video_info(url)
			metadata = bda_boilerplate.extract_metadata(info)
			json_path = bda_boilerplate.save_metadata_to_file(metadata, metadata["title"])
			print(f"✅ Done: {metadata['title']}\n📄 Metadata: {json_path}")
			log_entry(url, True)
			return
		except Exception as e:
			log_entry(url, False)
			if retry <= 5:
				print(f"🚧 Failed to download, retry attempt number: {retry}")
				retry += 1
			else:
				print(f"❌ Failed to download: {url}\n   Error: {e}")
				return


#serial execution
def download_youtube_audio_with_metadata_serial(youtube_urls):
    for url in youtube_urls:
        download_youtube_audio_with_metadata(url)

#parallel execution with ThreadPoolExecutor from lesson 6
def download_youtube_audio_with_metadata_parallel(youtube_urls, max_threads=5):
	with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
		executor.map(download_youtube_audio_with_metadata, youtube_urls)

log_lock = threading.Lock()
log_f = None

def log_init(log_dir="logs", log_file="download_log.txt"):
	"""Initialize the log directory and file."""
	global log_f
	os.makedirs(log_dir, exist_ok=True)
	log_path = os.path.join(log_dir,log_file)
	log_f = open(log_path, "a")

def log_entry(url: str, download: bool):
	"""Append a structured log entry to the log txt file with timestamp, in a JSON-like format."""
	if not log_f:
		print("Log file is not initialized. Call log_init() first.")
		return

	with log_lock:
		log_f.write(f"[{datetime.now().isoformat(timespec='seconds')}] - URL: {url} - Downloaded: {download}\n")

def log_close():
	"""Close the log file."""
	global log_f
	if log_f:
		log_f.close()
		log_f = None
	else:
		print("Log file is not open.")