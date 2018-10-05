import sslclient

def main():
    c = sslclient.client()

    c.connect()

    while True:
        pkg = c.receive()
        print pkg

if __name__ == '__main__':
  main()

