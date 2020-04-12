import socket

def servbyport(lower=0, upper=100):
    if lower >= 0 and upper <= 65535:

        ports = range(lower, upper + 1)
        empty_ports = []
        for port in ports:
            try:
                serv = socket.getservbyport(port)
                print(f'PORT {port}: {serv}')
            except OSError as e:
                empty_ports.append(port)
        print(f'\nthe following ports are empty:')
        print(empty_ports)

    else:
        print("valid ports are between 0 - 65535")


if __name__ == '__main__':
    servbyport(0, 100)



