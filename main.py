from stats import print_report
import sys

def main ():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        print_report(file_path)

if __name__=="__main__":
    main()
