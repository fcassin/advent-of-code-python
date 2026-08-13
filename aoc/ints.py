import re


def extract(line):
    return [int(val) for val in re.findall("-?[\\d]+", line)]


def extract_one(line):
    return int(re.search("-?[\\d]+", line).group(0))


def extract_contiguous(line):
    yield from map(int, line.strip())
