from urllib import request
import json

def convert(release):
    original_version = release['tag_name'].strip('v')
    version = original_version.replace('beta.', 'rc').replace('alpha.', 'pre')
    stability = 'testing' if release['prerelease'] else 'stable'
    released = release['published_at'][0:10]
    return {'version': version, 'original-version': original_version, 'stability': stability, 'released': released}

data = request.urlopen('https://api.github.com/repos/kubernetes/kubernetes/releases').read().decode('utf-8')
releases = [convert(release) for release in json.loads(data)]
