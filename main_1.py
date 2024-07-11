import argparse
import asyncio
from itertools import groupby
import os.path

import aiofiles.os


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("source")
        parser.add_argument("output")
        args = parser.parse_args()
    except SystemExit:
        print("Please provide correct args")
    else:
        all_files = asyncio.run(read_folder(args.source))
        asyncio.run(do_copy(args.output, all_files))


async def read_folder(path: str) -> list:
    result = []
    dir_list = []
    try:
        dir_list = await aiofiles.os.listdir(path)
    except OSError:
        print(f"folder {path} error")
    for item in dir_list:
        full_path = os.path.join(path, item)
        try:
            if await aiofiles.os.path.isdir(full_path):
                result.extend(await read_folder(full_path))
            elif await aiofiles.os.path.isfile(full_path):
                result.append(full_path)
        except OSError:
            print(f"item {full_path} error")
    return result


async def do_copy(output: str, files: list):
    grouped = groupby(files, lambda x: os.path.splitext(x)[1])

    tasks = [copy_file(os.path.join(output, group[0][1:]), [x for x in group[1]]) for group in grouped]
    await asyncio.gather(*tasks)


async def copy_file(destiny: str, files: list):
    await aiofiles.os.makedirs(destiny, exist_ok=True)

    for file in files:
        try:
            async with aiofiles.open(file, mode='rb') as f:
                contents = await f.read()
                filename = os.path.basename(file)
                async with aiofiles.open(os.path.join(destiny, filename), mode='wb') as f_w:
                    await f_w.write(contents)
        except OSError:
            print(f"copy {file} error")


if __name__ == "__main__":
    main()
