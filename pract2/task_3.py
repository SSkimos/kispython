def generate_groups():
    print("IVBO")
    for i in range(1, 8):
        print('IVBO-0' + str(i) + '-20')
    print("IKBO")
    for i in range(1, 30):
        if (i < 10):
            print('IKBO-0' + str(i) + '-20')
        else:
            print('IKBO-' + str(i) + '-20')
    print("INBO")
    for i in range(1, 13):
        if (i < 10):
            print('INBO-0' + str(i) + '-20')
        else:
            print('INBO-' + str(i) + '-20')
    print("IMBO")
    for i in range(1, 2):
        if (i < 10):
            print('IMBO-0' + str(i) + '-20')
        else:
            print('IMBO-' + str(i) + '-20')

generate_groups()