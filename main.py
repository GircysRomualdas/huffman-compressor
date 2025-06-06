from src.compressor import compress_file, decompress_file
import sys
import os

def main():
    try:
        flag = sys.argv[1]
        path = sys.argv[2]
    except IndexError:
        print("Usage:")
        print("    python main.py compress   <file.txt>")
        print("    python main.py decompress <file.txt.huff.bin>")
        sys.exit(1)

    try:
        if not os.path.exists(path):
            raise FileNotFoundError

        match flag:
            case "compress":
                new_path, original_size, compressed_size = compress_file(path)
                print(f"[✓] Compression successful!")
                print(f"    Original file:     {path}")
                print(f"    Compressed file:   {new_path}")
                print(f"    Original size:     {original_size} bytes")
                print(f"    Compressed size:   {compressed_size} bytes")
                print(f"    Compression ratio: {compressed_size/original_size:.2%}")
            case "decompress":
                if not path.endswith(".huff.bin"):
                    raise ValueError("Error: Invalid file suffix for decompression.")

                new_path = decompress_file(path)
                size = os.path.getsize(new_path)
                print(f"[✓] Decompression successful!")
                print(f"    Input file:        {path}")
                print(f"    Output file:       {new_path}")
                print(f"    Decompressed size: {size} bytes")
            case _:
                print("Error: Invalid flag. Use 'compress' or 'decompress'")
                sys.exit(1)
    except FileNotFoundError:
        print(f"[X] Error: File '{path}' not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"[X] {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
