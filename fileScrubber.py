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
			allPath = os.path.join(root, name)
			relPath = os.path.relpath(allPath, dir)
			# print (root)
			# print (relPath)
			# print (allPath)

			if relPath in fileNames:
				# print ('yes')
				# print ('files:')
				print ('Removing file:', os.path.join(root, name))
				os.remove(os.path.join(root, name))

		for name in dirs:
			allPath = os.path.join(root, name)
			relPath = os.path.relpath(allPath, dir)
			# print (relPath)
			if relPath in folderNames:
				print ('Removing folder', os.path.join(root, name))
				os.rmdir(os.path.join(root, name))
				
	return 'Scrubbing finished'
if __name__ == '__main__':
	main()