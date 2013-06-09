#environment constants:
self.name = 'defaultEnvironment'
self.width = self.height = 100 #physical dimensions of environment grid

#time-dependent functions:
self.influence_PA = list()

#environment maps (location dependent functions):
self.temperature = [[[20]*self.width]*self.height]	#array of temperatures in degrees Celcius
