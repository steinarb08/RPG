class Elements:

	def __init__(self):
		self._physical = 0
		self._fire = 0
		self._water = 0
		self._air = 0
		self._darkness = 0
		self._light = 0


	def GetPhysical(self):
		return self._physical
	def GetFire(self):
		return self._fire
	def GetWater(self):
		return self._water
	def GetAir(self):
		return self._air
	def GetDarkness(self):
		return self._darkness
	def GetLight(self):
		return self._light


	def SetPhysical(self,n):
		self._physical = n
	def SetFire(self,n):
		self._fire = n
	def SetWater(self,n):
		self._water = n
	def SetAir(self,n):
		self._air = n
	def SetDarkness(self,n):
		self._darkness = n
	def SetLight(self,n):
		self._light = n
	def SetAll(self,n):
		self._physical = n
		self._fire = n
		self._water = n
		self._air = n
		self._darkness = n
		self._light = n


	def AddPhysical(self,n):
		self._physical += n
	def AddFire(self,n):
		self._fire += n
	def AddWater(self,n):
		self._water += n
	def AddAir(self,n):
		self._air += n
	def AddDarkness(self,n):
		self._darkness += n
	def AddLight(self,n):
		self._light += n
	def AddAll(self,n):
		self._physical += n
		self._fire += n
		self._water += n
		self._air += n
		self._darkness += n
		self._light += n