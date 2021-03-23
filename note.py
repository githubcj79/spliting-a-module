~/Documents/lab/spliting-a-module $ tree -a -I ".git|__pycache__|.gitignore" -L 3 -D
.
├── [Feb 14 16:30]  mymodule
│   ├── [Feb 14 16:23]  a.py
│   ├── [Feb 14 16:23]  b.py
│   └── [Feb 14 16:24]  __init__.py
└── [Feb 14 16:33]  test.py

1 directory, 4 files
~/Documents/lab/spliting-a-module $ python3 test.py
A.spam
B.bar
