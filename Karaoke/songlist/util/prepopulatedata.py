import csv
from songlist.models import Track, Artist

def file_opener():

	data_write = []

	
	with open('songlist/util/hamcat.csv','r', encoding="Latin-1") as file:
		data = csv.reader(file, delimiter=',')
		for row in data:
			
			rowList = [] 
			song_number, title, name, album  = row
			if song_number:
				song_number = song_number
			else: 
				song_number = " "

			if title:
				title = title
			else:
				title = " "

			if name:
				name = name
			else: 
				name = " "

			if album:
				album = album
			else: 
				album = ' '


			rowList.extend([song_number, title, name, album])
			data_write.append(rowList)

			

		return data_write

file_opener()

def insert_data_in_db():
	data = file_opener()
	# print(data)
	for song_number, title, name, album in data:
		print(song_number, title, name, album)
		try:
			a = Artist.objects.get(name=name)
			print("writing",a)
			s = Track.objects.create(
				song_number = song_number,
				title = title,
				artist=a,
				# album = 1,

				)
			s.save(force_insert=True)
		except Exception:
		# 	print("Not getting",name)
			pass

insert_data_in_db()	

# def insert_data_in_db():
# 	data = file_opener()
# 	# print(data)
# 	for song_number, title, name, album in data:
# 		print(song_number, title, name, album)
# 		try:
# 			s = Artist.objects.create(
# 			# song_number = song_number,
# 			# title = title,
# 				name=name,
# 			# album = "Unknown",

# 				)
# 		# s.save(force_insert=True)
# 		except Exception:
# 		# 	print(name)
# 			pass

# insert_data_in_db()	