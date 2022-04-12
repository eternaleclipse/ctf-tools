#!/usr/bin/env python3
# Read file and generate new files with flipped bit for each offset

import sys


def flip_bit(buf: bytearray, i: int):
    byte_offset = i // 8
    bit_offset = i % 8
    byte = buf[byte_offset]
    byte ^= (1 << bit_offset)
    buf[byte_offset] = byte
    return buf


def main():
    if len(sys.argv) != 2:
        print("Usage: flip_bits.py <src_file>")
        sys.exit(1)

    _, src_path = sys.argv

    with open(sys.argv[1], 'rb') as f:
        data = bytearray(f.read())
        num_bits = len(data) * 8

        print(f'Read {len(data)} bytes == {num_bits} bits')
        print(f'Generating {num_bits} files with flipped bit for each offset')

        for i in range(num_bits):        
            dst_path = f'{src_path}_{i}'
            with open(dst_path, 'wb') as out_file:
                out_file.write(flip_bit(data[:], i))

        print('Done.')


if __name__ == '__main__':
    main()
