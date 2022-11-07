from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobs = csv.reader(file, delimiter=",", quotechar='"')
        header, *datas = jobs
        result = []
        linhas = ({heade: "" for heade in header})
        for i, heade in enumerate(header):
            for f, data in enumerate(datas):
                if i == f:
                    linhas.update({heade: data[f]})
                    result.append(linhas)
                else:
                    ...
    print(f"Aqui === {len(result)}")
    return result[0:13]


read("./src/jobs.csv")
