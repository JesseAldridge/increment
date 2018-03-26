import sys, os, re, shutil

pivot = int(sys.argv[1])
direction = sys.argv[2] if len(sys.argv) > 2 else '+'

dir_path = os.getcwd()
paths = os.listdir(dir_path)
paths_with_numbered_filenames = sorted([path for path in paths if re.match('^[0-9]+', path)])

def increment_path(path, value):
  match = re.match('^([0-9]+)(.+)', path)
  if match is None:
    return
  num_str, base_path = match.group(1), match.group(2)
  num = int(num_str)
  num += value
  new_path = '{}{}'.format(str(num).zfill(2), base_path)
  shutil.move(path, new_path)

for path in paths_with_numbered_filenames[pivot:]:
  if direction == '+':
    increment_path(path, 1)
  else:
    increment_path(path, -1)
