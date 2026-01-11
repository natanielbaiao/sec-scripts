# Add IP Prefix Tool

A simple Python utility that reads a text file line by line and adds the IP address `0.0.0.0` at the beginning of each line.  
The result is written to a new file with the extension `.adl.txt`.

This tool is useful for creating DNS blocklists, ad-blocking files, or redirect lists from the following source:

https://dsi.ut-capitole.fr/blacklists/

---

## 📌 Features

- Reads large files efficiently (line by line)
- Skips empty lines
- Preserves original file
- Creates a new `.adl.txt` output file
- Cross-platform (Windows, Linux, macOS)

---

## 📂 Example

### Input file (`domains.txt`)
```
google.com
facebook.com
example.org
```

### Output file (`domains.txt.adl.txt`)
```
0.0.0.0 google.com
0.0.0.0 facebook.com
0.0.0.0 example.org
```

---

## ⚙️ Requirements

- Python 3.7 or newer

---

## 🚀 How to Use

1. Save the script as:
```
adconverter.py
```

2. Open a terminal in the same folder

3. Run:
```
python adconverter.py domains.txt
```

4. The output will be created as:
```
domains.txt.adl.txt
```

---

## 🧠 How It Works

The program:
- Opens the input file
- Reads each line
- Adds `0.0.0.0 ` in front of every non-empty line
- Writes everything into a new file

---

## 🛡 Error Handling

The script checks:
- If a file was provided
- If the file exists
- If any read/write errors occur

---




