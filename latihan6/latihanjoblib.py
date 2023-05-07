from joblib import Parallel, delayed
def worker(num):

    print('Worker', num)
if __name__ == '__main__':

    Parallel(n_jobs=2)(delayed(worker)(i) for i in range(5))
