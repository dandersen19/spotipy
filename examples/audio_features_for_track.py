

# shows acoustic features for one track given ID

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'ID_HERE' # add Spotify CLIENT ID here
os.environ['SPOTIPY_CLIENT_SECRET'] = 'SECRET_HERE' # add Spotify CLIENT SECRET here

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True

start = time.time()
features = sp.audio_features('6Xk5AaN4n4SnW71473GI7A') # replace with track ID
delta = time.time() - start
print(json.dumps(features, indent=4))
print("features retrieved in %.2f seconds" % (delta,))
