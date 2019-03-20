import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('action', action="store")

    args = parser.parse_args()
