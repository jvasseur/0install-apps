import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import github

releases = [{
    'version': release['tag_name'].strip('v').replace('.0', '.'),
    'original-version': release['tag_name'].strip('v'),
    'released': release['published_at'][0:10]
} for release in github.releases('AlDanial/cloc')]
