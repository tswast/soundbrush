Joyful = 0
Happy = 1
Sad = 2
Dark = 3
Chaotic = 4

Moods = {0:Joyful, 1:Happy, 2:Sad, 3:Dark, 4:Chaotic}

def findMood(pos):
	return Moods[int(pos)]

class MusicStroke:
	def __init__(self, pos, color)
		mood = findMood(pos)
		self.ref_y = pos.y
		self.composer = Composer(color, mood)
		self.arclen = 0
		self.prev = 0
	def tic(self, arclen, y):
		self.arclen += arclen
		offset = int(arclen / .05)

		asc = False
		if (y < self.ref_y):
			asc = True
			
		composer.tic(asc, offset - self.prev)
		self.prev = offset

	def stop(self):
		composer.stop()

