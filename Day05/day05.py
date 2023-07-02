from hashlib import md5
from binascii import hexlify


def main():
    message = 'ffykfhsq' 
    
    password = [] 

    i = 0 
    while len(password) < 8:
        test_message = message + str(i)
        result = md5(test_message.encode('utf-8'))
        hexed = hexlify(result.digest()).decode()
        if hexed.startswith('00000'):
            password.append(hexed[5])
        i += 1
    print(i, test_message, ''.join(password), hexed)


if __name__ == '__main__':
    main()

