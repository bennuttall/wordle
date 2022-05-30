import json
import argparse

with open("words.json") as f:
    WORDS = json.load(f)

def starts_with(chars):
    return {
        word
        for word in WORDS
        if word.startswith(chars)
    }

def ends_with(chars):
    return {
        word
        for word in WORDS
        if word.endswith(chars)
    }

def contains(chars):
    return {
        word
        for word in WORDS
        if chars in word
    }

def main(args):
    if args.start:
        results = starts_with(args.start)
    elif args.end:
        results = ends_with(args.end)
    elif args.contains:
        results = contains(args.contains)
    
    for word in sorted(results):
        print(word.upper())
    print(len(results), "results")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', type=str)
    parser.add_argument('-e', '--end', type=str)
    parser.add_argument('-c', '--contains', type=str)
    args = parser.parse_args()
    main(args)