from pathlib import Path

from yt_dlp import YoutubeDL

base_dir = Path(__file__).resolve().parent
output_dir = base_dir / 'output'
output_dir.mkdir(exist_ok=True)

with open(base_dir / 'list.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file if line.strip()]

for index, url in enumerate(urls, start=1):
    downloader = YoutubeDL({
        'cookiefile': str(base_dir / './cookies/x.com_cookies.txt'),
        'ignoreerrors': True,
        'outtmpl': str(output_dir / f'{index}.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    })

    downloader.download([url])