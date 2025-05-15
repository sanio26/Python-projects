print("Sanio Frederic,1AY24AI099,SEC-O")
import time
import sys

def zigzag():
    indent = 0  # Number of spaces to indent
    indent_increasing = True

    try:
        while True:
            print(' ' * indent + '*')
            time.sleep(0.05)

            if indent_increasing:
                indent += 1
                if indent == 20:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        print("\nZigzag stopped.")

if __name__ == "__main__":
    zigzag()
