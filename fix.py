import re
import random

videos = [
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4',
    'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
]

with open('aura_luxury_e_commerce.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    return f'<source src="{random.choice(videos)}#t=0.001"'

new_content = re.sub(r'<source src="https://cdn\.coverr\.co/videos/[^"]+"', replacer, content)

with open('aura_luxury_e_commerce.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done!')
