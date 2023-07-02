from hashlib import md5
from binascii import hexlify


def solver_1(message):
    password = [] 

    i = 0 
    k = 0
    while len(password) < 8:
        test_message = message + str(i)
        result = md5(test_message.encode('utf-8'))
        hexed = hexlify(result.digest()).decode()
        if hexed.startswith('00000'):
            password.append(hexed[5])
        i += 1
    return ''.join(password)


def solver_2(message):
    password = ['', '' ,'', '', '', '', '', ''] 

    i = 0 
    k = 0
    done = False
    while not done:
        test_message = message + str(i)
        result = md5(test_message.encode('utf-8'))
        hexed = hexlify(result.digest()).decode()
        if hexed.startswith('00000'):
            index = int('0x' + hexed[5], 16)
            if index < 8 and password[index] == '':
                password[index] = hexed[6]
                done = True
                for c in password:
                    if c == '':
                        done = False

        i += 1
    return ''.join(password)


def main():
    message = 'ffykfhsq' 
    print(f'Part 1 password: {solver_1(message)}')
    print(f'Part 2 password: {solver_2(message)}')
    

if __name__ == '__main__':
    main()

