import os
import csv

def main(dir, csvfileName):
	fileNames = []
	folderNames = []

	with open(csvfileName, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
		next(reader)

		for row in reader:
			if row[1] == 'file':
				fileNames.append(row[0])
			if row[1] == 'folder':
				folderNames.append(row[0])

	for root, dirs, files in os.walk(dir):
		for name in files:
			if name in fileNames:
				# print ('yes')
				# print ('files:')
				print ('Removing file:', os.path.join(root, name))
				os.remove(os.path.join(root, name))

		for name in dirs:
			if name in folderNames:
				print ('Removing folder', os.path.join(root, name))
				os.removedirs(os.path.join(root, name))
				
	return 'Scrubbing finished'
if __name__ == '__main__':
	main()