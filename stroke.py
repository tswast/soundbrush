
class Mood:
	"""Represents music 'moods'. These map to portions of the canvas.
	The composer class decides what these mean in terms of music."""
	Joyful = 0
	Happy = 1
	Sad = 2
	Dark = 3
	Chaotic = 4
	

def findMood(pos):
	return int(pos * 5)

class MusicStroke:
	"""Represents a 'stroke' in on our musical canvas.
	This is created upon the start of the stroke, and tic() is
	called every tic. This parses the data and passes it to the composer."""
	def __init__(self, y, color):
		mood = findMood(pos)
		self.ref_y = y
		self.composer = Composer(color, mood)
		self.arclen = 0
		self.prev = 0
	def tic(self, arclen, y):
		self.arclen += arclen
		offset = int(arclen / .05) - self.prev

		if (y < self.ref_y):
			offset = -offset
			
		composer.tic(offset)
		self.prev = offset

	def stop(self):
		composer.stop()

