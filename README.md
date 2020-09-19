### hacker rank solutions for python

### for infy.py use the following code to convert from larger case to smaller case
  ```python
  def cap(x):
    l = ''
    for i in x:
        if i == ' ':
            l = l + ' '
        elif ord(i) >= 65 and ord(i) <= 90:
            a = ord(i) + 32
            l = l + chr(a)
    print(l)
  ```
  
