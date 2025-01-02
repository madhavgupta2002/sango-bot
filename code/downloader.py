import time
import subprocess

start_index = 1
batch_size = 15
sleep_time = 20

while True:
    command = f'yt-dlp --write-auto-sub --skip-download --sub-format srt --sub-lang en --convert-subs srt "https://www.youtube.com/@sangorealestate/videos" --playlist-start {start_index} --playlist-end {start_index + batch_size - 1} --exec "sleep 5"'
    subprocess.run(command, shell=True)
    
    start_index += batch_size
    time.sleep(sleep_time)