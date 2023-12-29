import json
from pathlib import Path
from shutil import copy2
from datetime import datetime

stories_file = 'your_instagram_activity/content/stories.json'

with open(stories_file) as fh:
    data = json.load(fh)

target_dir = Path('stories_saved')
target_dir.mkdir()

for j, story in enumerate(data['ig_stories']):
    uri = story['uri']
    ts = story['creation_timestamp']    
    dt = datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')

    src = Path(uri)
    if not src.suffix:
        # in my files the missing suffixes were videos, might be different for you
        print(j, story, 'missing suffix, probably video')
    dest = target_dir / f'{dt}{src.suffix}'
    i = 0
    while dest.exists():
        i += 1
        dest = target_dir / f'{dt}_{i}{src.suffix}'
    copy2(src, dest)
