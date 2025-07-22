import time
import fun

if __name__ == "__main__":

	# initialize the log file
	fun.log_init()

	# ask the user for the url file
	path = input("Enter the path to the file containing YouTube URLs: ")
	youtube_urls = fun.load_url_list(path)

	mode = input("Enter 's' for serial execution or 'p' for parallel execution: ").strip().lower()
	if mode not in ['s', 'p']:
		print("Invalid mode. Please enter 's' for serial or 'p' for parallel.")
		exit(1)

	if mode == "s":
		# call the function to download YouTube audio with metadata using serial execution
		start = time.perf_counter()
		fun.download_youtube_audio_with_metadata_serial(youtube_urls)
		end = time.perf_counter()
		print(f'Serial: {end - start} second(s).')
	else:
		# call the function to download YouTube audio with metadata using parallel execution
		start = time.perf_counter()
		fun.download_youtube_audio_with_metadata_parallel(youtube_urls)
		end = time.perf_counter()
		print(f'Parallel: {end - start} second(s).')

	fun.log_close()