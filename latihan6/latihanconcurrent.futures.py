import concurrent.futures

def worker(num):
    print('Worker', num)
    
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

        for i in range(5):
            executor.submit(worker, i)