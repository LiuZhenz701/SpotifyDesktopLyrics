# For UI
import tkinter as tk
# For lyrics
import Lyrics_loader as lrcLoader
# For track status
import Playback_info as info

class LyricsApp:
	def __init__(self, root):
		self.root = root
		# Set basic stats
		self.root.title("Desktop Lyrics") # window title (useless)
		self.root.geometry("800x100") # window size 
		self.root.configure(bg="black") # background color setting
		self.root.attributes('-transparentcolor', "black") # set transparent color
		self.root.overrideredirect(True) # remove tab border
		self.root.attributes("-topmost", True) # always on top

		# Initialize labels
		# Track name + artist name
		self.title_label = tk.Label(root, text="No Track Playing", font=("Arial", 11), fg="red", bg="black")
		self.title_label.pack(pady=4)
		# Lyrics
		self.lyrics_label = tk.Label(root, text="Can't Find Lyrics", font=("Arial", 18), fg="red", bg="black")
		self.lyrics_label.pack(pady=4)
		# Track name variable
		self.current_track = ""
		# Lyric file
		self.lyric = []

		# Update the window
		self.load_lyric()
		self.update_window()
		
		# Load the lyrics file
	def load_lyric(self):
		if self.current_track != info.get_track_name():
			self.current_track = info.get_track_name()
			lyric_addr = lrcLoader.find_lrc_file(self.current_track, info.get_artist_names())
			self.lyric = lrcLoader.load_lrc_file(lyric_addr)
		
		

		# Update the display window 
	def update_window(self):
		# If spotify is initialized
		if info.check_spotify_status():
			# Check if track changed
			if self.current_track != info.get_track_name():
				self.load_lyric() # Reload new lyric
			# Update the display window		
			current_lyric = lrcLoader.get_current_lyric(self.lyric, info.get_track_progress()) # variable for current line
			self.title_label.config(text=self.current_track)
			self.lyrics_label.config(text=current_lyric)
			
		self.root.after(50, self.update_window)
				
if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsApp(root)
    root.mainloop()