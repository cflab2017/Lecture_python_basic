"""mytool CLI 진입점"""
import argparse

def main():
    parser = argparse.ArgumentParser(prog="mytool")
    parser.add_argument("--name", default="World")
    parser.add_argument("--version", action="version", version="mytool 0.1.0")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
