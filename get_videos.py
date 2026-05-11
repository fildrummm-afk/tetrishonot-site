import urllib.request, re, json

CHANNEL_ID = 'UCO9RXxVEbfmZ7fqOHflrTyA'

# RSS-фид YouTube — всегда возвращает последние 15 видео канала
url = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req) as r:
    xml = r.read().decode('utf-8')

# Парсим XML вручную
video_ids   = re.findall(r'<yt:videoId>([^<]+)</yt:videoId>', xml)
titles      = re.findall(r'<title>([^<]+)</title>', xml)
titles = titles[1:]  # первый <title> — это название канала

videos = []
for vid_id, title in zip(video_ids, titles):
    videos.append({'id': vid_id, 'title': title})
    print(f'  {vid_id}  —  {title}')

print(f'\nНайдено видео: {len(videos)}')

with open('videos.json', 'w', encoding='utf-8') as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print('✓ Сохранено в videos.json')
