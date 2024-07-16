import os
import subprocess

# Function to download YouTube Shorts using yt-dlp
def download_youtube_shorts(channel_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Updated command to use yt-dlp with improved format selection and post-processing
    command = [
        'yt-dlp',
        '--ignore-errors',
        '--format', 'bestvideo+bestaudio/best',
        '--output', f'{output_dir}/%(autonumber)s.%(ext)s',
        '--no-check-certificate',
        '--no-playlist',
        '--match-filter', 'duration < 60',
        '--verbose',
        '--merge-output-format', 'mp4',
        '--postprocessor-args', '-c:v libx264 -c:a aac',
        f'{channel_url}/shorts'
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error downloading shorts: {e}')

if __name__ == '__main__':
    # Replace with the channel URL from which you want to download shorts
    channel_url = 'https://www.youtube.com/channel/UCqmHA1HFPaI_lRUgoznUKmg'

    # Replace with the directory where you want to save the downloaded shorts
    output_dir = './downloaded_shorts'

    download_youtube_shorts(channel_url, output_dir)
