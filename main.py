from threading import Thread
from multiprocessing import Process, Manager
import time

all_words = ["own", "she", "Attended", "fake"]
all_files = [
    "files/1.txt",
    "files/2.txt",
    "files/3.txt",
    "files/4.txt",
    "files/5.txt",
    "files/6.txt",
    "files/7.txt",
    "files/8.txt",
    "files/9.txt"
]

num_treads = 3
num_processes = 3


def lookup(path: str, words: list) -> list:
    try:
        found = []
        with open(path) as f:
            file_data = f.read()
            for word in words:
                if word in file_data:
                    found.append(word)
        return found
    except OSError:
        return []


def thread_job(files: list, words: list, result: dict):
    for file in files:
        found = lookup(file, words)
        for word in found:
            if word in result:
                result[word].append(file)
            else:
                result[word] = [file]


def main_thread():
    result = {}
    threads = []
    files_per_thread = [all_files[i:i + num_treads] for i in range(0, len(all_files), num_processes)]

    start = time.time()
    for i in range(num_treads):
        thread = Thread(target=thread_job, args=(files_per_thread[i], all_words, result))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]
    end = time.time()
    print(result)
    print(f"calculation time-{end - start}")


def process_job(files: list, words: list, val: Manager):
    for file in files:
        found = lookup(file, words)
        val[file] = found


def main_process():
    files_per_process = [all_files[i:i + num_treads] for i in range(0, len(all_files), num_treads)]
    processes = []

    with Manager() as manager:
        result_per_file = manager.dict()
        start = time.time()
        for i in range(num_treads):
            process = Process(target=process_job, args=(files_per_process[i], all_words, result_per_file))
            process.start()
            processes.append(process)

        [pr.join() for pr in processes]
        end = time.time()
        result_per_word = {}
        for file in result_per_file:
            found = result_per_file[file]
            for word in found:
                if word in result_per_word:
                    result_per_word[word].append(file)
                else:
                    result_per_word[word] = [file]

        print(result_per_word)
        print(f"calculation time-{end - start}")


if __name__ == "__main__":
    main_thread()
    main_process()
