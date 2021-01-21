

# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import os

os.environ['SPOTIPY_CLIENT_ID'] = '5a9702c739a346de80cb333b6cb65e49'
os.environ['SPOTIPY_CLIENT_SECRET'] = '71c46401434c4a2bbc7d7ae1f03b7797'

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

start = time.time()
features = sp.audio_features('6Xk5AaN4n4SnW71473GI7A')
delta = time.time() - start
print(json.dumps(features, indent=4))
print("features retrieved in %.2f seconds" % (delta,))
