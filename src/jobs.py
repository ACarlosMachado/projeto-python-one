from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        result = []
        for job in jobs:
            result.append(job)
        return result


read("./src/jobs.csv")
