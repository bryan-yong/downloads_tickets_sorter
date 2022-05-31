#Purpose is to filter items in the downloads folder and to automatically sort the items into designated directories
#If the directory does not exsist, then it should create said directory

import os, shutil, glob, datetime

# Scans downloads folder and moves downloaded tickets into their respective directories
def main():
  os.chdir(os.path.expanduser('~/Downloads'))
  for file in glob.glob('*.pdf'):
    if 'Request' in file:
      move(file)
      print(file + ' was moved.\n----------------------------')

# gets creation date/time of file and converts it from Unix time to date time
def get_create_date(file):
  mtime = os.stat(file).st_birthtime
  time_stamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
  return time_stamp

# moves file to designated directory, if directory doesn't exist then it creates the directory
def move(file):
  dst_main = os.path.expanduser('~/Desktop/Tickets/')
  src_file = os.path.expanduser('~/Downloads/') + file

  time_stamp = get_create_date(file)
  year, month = time_stamp[0:4], time_stamp[5:7]

  dst = dst_main + str(year + '/' + month + '.' + year + '/')
  if os.path.exists(dst) is True: shutil.move(src_file, dst)
  else: 
    os.mkdir(dst)
    shutil.move(src_file, dst)



try:
  main()
except:
  print('Something broke.')
