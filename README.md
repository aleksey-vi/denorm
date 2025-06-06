# denorm

A Python script to process and deduplicate URLs from an input file. It normalizes URLs by converting them to lowercase, preserving the scheme, netloc, and path, and cleaning query parameters (keeping only keys). The resulting unique URLs are saved to an output file.

## Features:

- Removes duplicate URLs based on normalized structure.
- Supports command-line arguments for input (-f) and output (-o) files.
- Handles malformed URLs gracefully.
- Outputs the count of unique URLs saved.

## Usage:

```
python3 normalize_urls.py -f input.txt -o output.txt
```

### example

input file:
```
cat for_test 
https://example.com/1/ololo/?param1=1&param2=2
https://example.com/1/ololo/?param1=11111&param2=2
https://example.com/1/ololo/?param1=1&param2=2222
https://example.com/1/ololo/?param1=1&param2=2
https://example.com/1/ololo/?param1=1&param3=33333
https://example.com/2/ololo/?param1=1&param2=2
https://example.com/3
```

usage:
```
python3 denorm.py -f for_test -o res
```

result:
```
cat res 
https://example.com/1/ololo/?param1=1&param2=2
https://example.com/1/ololo/?param1=1&param3=33333
https://example.com/2/ololo/?param1=1&param2=2
https://example.com/3
```
