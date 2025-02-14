# Spotify API
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authentication
cid = '4bbeafceb28b4e98a4106c0e844e0850'
secret = '892b131c3ebf4dc49f0ef8de44eca0bc'
uri = "http://localhost:8888/callback"

# Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
	client_id=cid,
	client_secret=secret,
	redirect_uri=uri,
	scope="user-read-playback-state"
))

# Get all the track information
# This is a helper function to help me
# understand the return items of spotify api
def get_info():
	playback = sp.current_playback()
	return playback

# Check if the spotify client is opened
# return `True` if there's a song playing/paused
def check_spotify_status():
	playback = sp.current_playback()
	return playback['device']['is_active']

# Get the track information: Track Name
# return track name
def get_track_name():
	playback = sp.current_playback()
	return playback['item']['name']

# Get the track information: Artist Name
# return artist names
def get_artist_names():
    playback = sp.current_playback()
    artist_names = [artist['name'] for artist in playback['item']['artists']]    
    return ", ".join(artist_names)

# Get the track information: Duration
# return the track's duration
def get_track_duration():
	playback = sp.current_playback()
	return playback['item']['duration_ms']

# Get the track information: Progress
# return the current progress of the track
def get_track_progress():
	playback = sp.current_playback()
	return playback['progress_ms']