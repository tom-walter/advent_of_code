#!/bin/bash
set -euo pipefail

# load environment file
if [ -f ".env" ]; then
    source .env
else
    echo "Error: .env file not found!"
    exit 1
fi

if [ -z "${AOC_COOKIE:-}" ]; then
    echo "Error: AOC_COOKIE variable missing in .env"
    exit 1
fi

# input params
YEAR=${1:?Usage: ./downloader.sh YEAR DAY}
DAY_NUM=${2:?Usage: ./downloader.sh YEAR DAY}

# zero-padding for day
DAY=$(printf "%02d" "$DAY_NUM")

# destination file
OUTFILE="${YEAR}/d${DAY}.txt"

# make sure the directory exists
mkdir -p "${YEAR}"

echo "Downloading AoC Input for year=${YEAR} day=${DAY}"

curl -s "https://adventofcode.com/${YEAR}/day/${DAY_NUM}/input" \
    -H "Cookie: session=${AOC_COOKIE}" \
    -o "${OUTFILE}"

echo "Successfully saved at ${OUTFILE}"
exit 0
