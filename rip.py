from dataclasses import dataclass
from genericpath import isfile
import sys, getopt

@dataclass
class CoverLetter:
    date: str = ''
    boss_title:str = ''
    attention:str = ''
    location:str = ''
    job_title:str = ''
    name:str = ''
    def len(self):
        return len(self.date) + len(self.boss_title) + len(self.attention) + len(self.location) + len(self.job_title) + len(self.name)

def parseInput(argv):
   inputfile = ''
   outputfile = ''
   cl = CoverLetter()
   try:
      opts, _ = getopt.getopt(argv,"hi:o:d:b:a:l:j:n",["ifile=","ofile=","date=","boss_title=","attention=","location=", "job_title=","name="])
   except getopt.GetoptError:
      print('Please enter an input and output file')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("--date", "-d"):
         cl.date = arg
      elif opt in ("--boss_title", "-b"):
         cl.boss_title = arg
      elif opt in ("--attention", "-a"):
         cl.attention = arg
      elif opt in ("--location", "-l"):
         cl.location = arg         
      elif opt in ("--job_title", "-j"):
         cl.job_title = arg
      elif opt in ("--name"):
         cl.name = arg               
   return inputfile, outputfile, cl

def main(argv):
    inputFile, outputFile, cl = parseInput(argv)
    if inputFile == '' or outputFile == '':
        print('Please enter an input and output file')
        sys.exit(2)
    if not isfile(inputFile): 
        print("Input file {inputFile} does not exist ".format(inputFile = inputFile))
        sys.exit(2)    
    if isfile(outputFile): 
        print("Output file {outputFile} already exists ".format(outputFile = outputFile))
        sys.exit(2)
    if cl.len() < 1: 
        print("Please input a date, boss_title, attention, location, job_title and name.")
        sys.exit(2)
    f = open(inputFile)
    p = f.read().format(date = cl.date, boss_title = cl.boss_title, attn = cl.attention, location = cl.location, job_title = cl.job_title, name = cl.name)
    nf = open(outputFile, "x")
    nf.write(p)
    f.close()
    nf.close()
    print("Check output file for cover letter: {output_file}".format(output_file = outputFile))


if __name__ == "__main__":
   main(sys.argv[1:])
