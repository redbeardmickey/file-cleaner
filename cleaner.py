from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

import fileScrubber

class fileScrubberGUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.parent = master
		self.pack()
		self.initUI()

	def openFile(self):
		# pass
		self.file_opt = options = {}
		options['defaultextension'] = '.csv'
		options['filetypes'] = [('text files', '.csv')]
		# options['initialdir'] = 'C:\\'
		# options['initialfile'] = 'myfile.txt'
		options['parent'] = self.parent
		options['title'] = 'Select CSV file'
		self.csvfile = askopenfilename(**self.file_opt)
		return self.fileLabelText.set(self.csvfile)

	def openTargetDir(self):
		self.directory = askdirectory()
		return self.targetDirLabelText.set(self.directory)
		# pass

	def scrubFile(self):
		self.scrubStatusLabelText.set('Scrubbing...')
		return self.scrubStatusLabelText.set(fileScrubber.main(self.directory, self.csvfile))
		# pass

	def initUI(self):
		self.parent.title("FileScrubberGUI")
		self.targetDirLabelText = StringVar()
		self.targetDirLabelText.set('Please select a target directory')

		self.targetDirLabel = Label(self, textvariable=self.targetDirLabelText).grid(row=0, column=0, columnspan=2, pady=(10, 10), padx=(10, 10), sticky="W")
		self.targetDirBtn = Button(self, text='Select Directory', command=self.openTargetDir).grid(row=0, column=2, pady=(10, 10), padx=(10, 10), sticky="WE")

		self.fileLabelText = StringVar()
		self.fileLabelText.set('Please select the csv file')
		self.fileLabel = Label(self, textvariable=self.fileLabelText).grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=(10, 10), sticky="W")
		self.fileBtn = Button(self, text='Select File', command=self.openFile).grid(row=1, column=2, pady=(0, 10), padx=(10, 10), sticky="WE")

		self.scrubStatusLabelText = StringVar()
		self.scrubStatusLabelText.set('')
		self.scrubStatusLabel = Label(self, textvariable=self.scrubStatusLabelText).grid(row=2, column=0, columnspan=2, padx=(10, 10), pady=(0, 10), sticky="W")
		self.scrubBtn = Button(self, text='Scrub', command=self.scrubFile).grid(row=2, column=2, padx=(10, 10), pady=(0, 10), sticky="WE")

		self.exitBtn = Button(self, text='Quit', command=self.parent.destroy).grid(row=3, column=2, padx=(10, 10), pady=(0, 10), sticky="WE")

def main():
	root = Tk()
	app = fileScrubberGUI(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()