import urllib.request, json

ALBUMS = [
    ('5N02UgOIMOoqw2nx325THW', 'Министерство зла'),
    ('0w6tLBjcY74a5vcf8ImgBA', 'Повидали'),
    ('3APdbLopUzWcF8h6UO9zdS', 'Федералы'),
    ('3hxOzJhncIvkkYafvwu5MR', 'За одним столом'),
]

covers = {}
for album_id, name in ALBUMS:
    url = f'https://open.spotify.com/oembed?url=https://open.spotify.com/album/{album_id}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            img_url = data['thumbnail_url']
            # Заменяем на максимальное разрешение
            img_url = img_url.replace('/ab67616d00004851', '/ab67616d0000b273')
            covers[album_id] = img_url
            print(f'✓ {name}: {img_url}')
    except Exception as e:
        print(f'✗ {name}: {e}')

# Обновить HTML
with open('tetrishonot.html', 'r', encoding='utf-8') as f:
    html = f.read()

for album_id, name in ALBUMS:
    if album_id not in covers:
        continue
    img_url = covers[album_id]
    old = f'href="https://open.spotify.com/album/{album_id}" target="_blank">\n      <div class="disc-cover-placeholder">♪</div>'
    new = f'href="https://open.spotify.com/album/{album_id}" target="_blank">\n      <img class="disc-cover" src="{img_url}" alt="{name}" />'
    html = html.replace(old, new)

with open('tetrishonot.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✓ HTML обновлён!')
