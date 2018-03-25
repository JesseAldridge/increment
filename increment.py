import sys, os, re, shutil

pivot = int(sys.argv[1])
direction = sys.argv[2] if len(sys.argv) > 2 else '+'

dir_path = os.getcwd()
paths = os.listdir(dir_path)
paths_with_numbered_filenames = sorted([path for path in paths if re.match('^[0-9]+', path)])

def increment_path(path, value):
  num_str, base_path = os.path.basename(path).split('_', 1)
  num = int(num_str)
  num += value
  new_path = '{}_{}'.format(str(num).zfill(2), base_path)
  shutil.move(path, new_path)

for path in paths_with_numbered_filenames[pivot:]:
  if direction == '+':
    increment_path(path, 1)
  else:
    increment_path(path, -1)
