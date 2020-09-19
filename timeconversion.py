def timeConversion(s):
    if s[-2:] == 'PM':
        a = s.replace('PM','')
        a = a.split(':')
        if a[0] != '12':
            a[0] = str(int(a[0])+12)
        s = ':'.join(a)
    elif s[-2:] == 'AM':
        b = s.replace('AM','')
        b = b.split(':')
        if b[0] == '12':
            b[0] == '00'
        s = ':'.join(b)
    return s
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()