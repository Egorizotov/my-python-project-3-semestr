import json
from sys import exit

from cm_timer import cm_timer_1
from gen_random import Gen_random
from print_result import print_result
from unique import Unique


@print_result
def f1(vacancies):
    """Берём названия вакансий и оставляем уникальные (без учёта регистра)."""
    jobs = [vacancy["job-name"] for vacancy in vacancies]
    return sorted(Unique(jobs, ignore_case=True))


@print_result
def f2(jobs):
    """Оставляем только вакансии, начинающиеся со слова 'программист'."""
    return [job for job in jobs if job.lower().startswith("программист")]


@print_result
def f3(jobs):
    """Дописываем 'с опытом Python' к каждой вакансии."""
    return [job + " с опытом Python" for job in jobs]


@print_result
def f4(jobs):
    """Добавляем случайную зарплату к каждой вакансии."""
    salaries = Gen_random(len(jobs), 100_000, 200_000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(jobs, salaries)]


def main():
    # data_light.json должен лежать рядом с этим файлом
    with open("data_light.json", encoding="utf-8") as file:
        data = json.load(file)

    with cm_timer_1():
        f4(f3(f2(f1(data))))

    return 0


if __name__ == "__main__":
    exit(main())
