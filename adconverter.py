import sys
import os

#written by Nataniel Baiao 
#This script basically opens a domains file and output as mikrotik adlist domain null format

def main():
    if len(sys.argv) != 2:
        print("Usar: python adconverter.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        print("Arquivo nao encontrado")
        sys.exit(1)
    
    # Create output filename
    output_file = input_file + ".adl.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as infile, \
             open(output_file, "w", encoding="utf-8") as outfile:

            for line in infile:
                stripped = line.strip()
                if stripped:  # avoid blank lines
                    outfile.write("0.0.0.0 " + stripped + "\n")

        print(f"Feito! Output written to: {output_file}")

    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
