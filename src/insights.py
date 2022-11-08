from src.jobs import read


def get_unique_job_types(path):
    datas = read(path)

    novo = []
    for job in datas:
        if job["job_type"] not in novo:
            novo.append(job["job_type"])
    return novo


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    datas = read(path)

    industries = []
    for job in datas:
        if job["industry"] not in industries and job["industry"] != '':
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    datas = read(path)

    list_max = []
    for job in datas:
        if job["max_salary"] not in datas and job["max_salary"].isnumeric():
            to_number = int(job["max_salary"])
            list_max.append(to_number)

    return (max(list_max))
    pass


def get_min_salary(path):
    datas = read(path)

    list_min = []
    for job in datas:
        if job["min_salary"] not in datas and job["min_salary"].isnumeric():
            to_number = int(job["min_salary"])
            list_min.append(to_number)

    return (min(list_min))
    pass


def matches_salary_range(job, salary):
    if (
        "max_salary" not in job or
        "min_salary" not in job or
        type(job["max_salary"]) != int or
        type(job["min_salary"]) != int or
        type(salary) != int or
        job["max_salary"] < job["min_salary"]
    ):
        raise ValueError('Dados inválidos')
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            ...
    return filtered_jobs

# for job in jobs:
#         try:
#             if matches_salary_range(job, salary) is True:
#                 filtered_jobs.append(job)
#         except ValueError:
#             print(ValueError)
#         finally:
#             return filtered_jobs

# if (
#         "max_salary" not in job or
#         "min_salary" not in job or
#         isinstance(job["max_salary"], int) is False or
#         isinstance(job["min_salary"], int) is False or
#         isinstance(salary, int) is False or
#         job["max_salary"] < job["min_salary"]
#     ):
#         raise ValueError('Dados inválidos')
#     return job["min_salary"] <= salary <= job["max_salary"]
