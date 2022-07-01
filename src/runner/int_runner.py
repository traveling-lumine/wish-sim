from multiprocessing import Pool, cpu_count


def runner_wrapper(worker):
    def wrapper(*arg):
        count = cpu_count()
        pool = Pool(processes=count)
        workers = count * 10_000
        args = [arg] * workers
        res = pool.map(worker, args)
        return sum(res) / workers, max(res), min(res)

    return wrapper
