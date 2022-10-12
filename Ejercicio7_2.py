import time

def go_home():
    now = time.localtime().tm_hour

    if now >= 19:
        print(f"Son las {now}. Es hora de irse a casa")
    else:
        print(f"Queda {17 - now} hora(s) de trabajo")


if '__main__' == __name__:
    go_home()
