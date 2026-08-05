import time

from app.application import Application


def main():
    app = Application()

    try:
        app.run()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        app.stop()


if __name__ == "__main__":
    main()