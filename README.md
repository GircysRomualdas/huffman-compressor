# Huffman Compressor

A command-line tool that compresses and decompresses text files using the Huffman Coding algorithm.

---

## Huffman Coding

Huffman Coding is a lossless data compression algorithm. It assigns shorter binary codes to more frequent characters and longer codes to less frequent ones, reducing overall file size without losing information.

---

## Requirements

- Python 3

---

## Installation

1. Clone the repository

---

## Usage

### Compress a file
```bash
python3 main.py compress <path/to/input.txt>
```

#### Example
```bash
python3 main.py compress temp/Frankenstein.txt
```

#### Output
```bash
[✓] Compression successful!
    Original file:     temp/Frankenstein.txt
    Compressed file:   temp/Frankenstein.txt.huff.bin
    Original size:     430493 bytes
    Compressed size:   239690 bytes
    Compression ratio: 55.68%
```

---

### Decompress a file
```bash
python3 main.py decompress <path/to/input.txt.huff.bin>
```

#### Example
```bash
python3 main.py decompress temp/Frankenstein.txt.huff.bin
```
#### Output
```bash
[✓] Decompression successful!
    Input file:        temp/Frankenstein.txt.huff.bin
    Output file:       temp/Frankenstein.txt.huff
    Decompressed size: 430493 bytes

```

## Contributing
If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
