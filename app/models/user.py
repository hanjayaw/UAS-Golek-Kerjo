class User:
	def __init__(self): ## konstruktor
		self.nama = "Web Development"
		self.username = ""

	def getName(self): ## method untuk mengambil nama
		return self.nama

	def getUsername(self):
		return self.username

	#https://www.edureka.co/blog/self-in-python/#:~:text=The%20self%20is%20used%20to,to%20refer%20to%20instance%20attributes.
	def checkAccess(self, nama_user, kata_sandi):
		#need some code here, use logical verification
		#.....
		#.....
		#before this
		self.username = nama_user
		return 1