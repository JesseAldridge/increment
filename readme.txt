increment or decrement numerically prefixed files in a directory


python ../increment.py 1 +
                       ^ ^ 
                       | |
                       | direction (increment or decrement)
                       pivot (increment after index)

The above command will change this:
```
00_foo.txt
01_bar.txt
02_baz.txt
```
to this:
```
00_foo.txt
02_bar.txt
03_baz.txt
```

This is useful for inserting or removing a file from the sequence.


INSTALL:

ln -s $(PWD)/increment.py /usr/local/bin/increment
