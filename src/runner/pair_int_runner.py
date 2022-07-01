from multiprocessing import Pool, cpu_count

from src.constant import runner_mult


def pair_int_type_runner(worker):
    def wrapper(int_arg, int_arg2):
        assert type(int_arg) is int
        assert type(int_arg2) is int
        count = cpu_count()
        pool = Pool(processes=count)
        workers = count * runner_mult
        args = [(int_arg, int_arg2)] * workers
        res = pool.map(worker, args)
        return sum(res) / workers, max(res), min(res)

    return wrapper
