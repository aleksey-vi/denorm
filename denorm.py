from pprint import pprint
from typing import TypeAlias
from urllib.parse import urlparse, ParseResult
import argparse

def main(input_file: str, output_file: str):
    with open(input_file, "r") as fp:
        lines = fp.readlines()

    lines: list[str] = list(map(lambda x: x.lower(), lines))

    def get_clean_query_params(query):
        query_params: list[str] = []
        for param in query:
            try:
                key, _ = param.split("=", 1)
            except ValueError as e:
                continue
            query_params.append(f"{key}=")
        return query_params

    uniq_urls = []
    url_set = set()

    for line in lines:
        url = line.strip()
        parse_result: ParseResult = urlparse(url)

        query_params_list = parse_result.query.split("&")

        clear_line = f"{parse_result.scheme}://{parse_result.netloc}"
        if parse_result.path != "":
            clear_line += parse_result.path
        if parse_result.query != "":
            clear_line += "?"
            clear_line += "&".join(get_clean_query_params(query_params_list))

        if clear_line not in url_set:
            uniq_urls.append(url)
            url_set.add(clear_line)

    with open(output_file, "w") as outfile:
        for url in uniq_urls:
            outfile.write(url + "\n")

    print(f"Сохранено {len(uniq_urls)} уникальных URL в файл '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and deduplicate URLs from an input file.")
    parser.add_argument("-f", "--input-file", required=True, help="Path to the input file containing URLs")
    parser.add_argument("-o", "--output-file", required=True, help="Path to the output file for unique URLs")
    args = parser.parse_args()

    main(args.input_file, args.output_file)