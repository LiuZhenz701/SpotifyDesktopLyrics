# For file finding
import os
# Import track info functions
import Playback_info as info
# Import settings from main file
import run

# Find the lyrics .lrc file from the local lyrics folder
# return the path to the .lrc file if it's exist
# else, return "No lyrics found!"

# Lyric file format: TrackName_ArtistNames.lrc
def find_lrc_file(track_name, artist_name):
    file_path = os.path.join(run.lyrics_folder, track_name + "_" + artist_name + ".lrc")
    return file_path if os.path.isfile(file_path) else "No lyrics found!"

# Load the lyrics .lrc file, update the timestamp from lrc form
# to spotify ms form, map the timestamp and lyric together,
# return the lyrics as a list
def load_lrc_file(lrc_path):
    if lrc_path == "No lyrics found!" : return "No lyrics found"
    lyrics = []
    with open(lrc_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('['):
                timestamp, lyric = line.strip().split(']', 1)
                timestamp = timestamp[1:]

                minutes, seconds = timestamp.split(':')
                seconds, hundredths = seconds.split('.')
                
                timestamp_ms = (int(minutes) * 60 + int(seconds)) * 1000 + int(hundredths) * 10
                lyrics.append((timestamp_ms, lyric.strip()))
    return lyrics

# Get the current lyric corresponding to the playback
def get_current_lyric(lyric_list, progress_ms):
    if lyric_list == "No lyrics found" : return "No lyrics found"
    # When lyrics is loaded
    current_lyric = None
    next_lyric = None
    # Get the lyric
    for i in range(len(lyric_list)):
        timestamp_ms, lyric = lyric_list[i]

        if timestamp_ms <= progress_ms:
            current_lyric = lyric
            next_lyric = lyric_list[i + 1][1] if i + 1 < len(lyric_list) else ""

            output_lyric = current_lyric + "\n" + next_lyric

    return output_lyric