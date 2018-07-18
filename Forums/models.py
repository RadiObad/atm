class Member():
	"""This class provides a way to store member name and age"""

	def __init__(self, name, age):
		self.id = 0
		self.name = name
		self.age = age

	def __str__(self):
		return '{} has {} years'.format(self.name, self.age)
class Post():
	"""This class provides a way to store post title and content"""

	def __init__(self, title, content):

		self.id = 0
		self.title = title
		self.content= content

	def __str__(self):
		return	'{} : {}'.format(self.title, self.content)
