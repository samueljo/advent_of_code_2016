import hashlib

def get_password(door_id):
    password = ''
    idx = 0
    while len(password) < 8:
        md5 = hashlib.md5(door_id + '{}'.format(idx)).hexdigest()
        if md5[:5] == '00000':
            password += md5[5]
        idx += 1

    return password

def get_password_2(door_id):
    password = ['0'] * 8
    count = 0
    idx = 0
    while count < 8:
        md5 = hashlib.md5(door_id + '{}'.format(idx)).hexdigest()
        if md5[:5] == '00000' and ord(md5[5]) < 56:
            if password[int(md5[5])] == '0':
                password[int(md5[5])] = '{}'.format(md5[6])
                count += 1
        idx += 1

    return ''.join(password)

# print get_password('abc')
# print get_password('cxdnnyjw')
print get_password_2('abc')
print get_password_2('cxdnnyjw')
