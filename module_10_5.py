import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open (name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # start_time_1 = time.time()
    # for filename in filenames:
    #     read_info(filename)
    # finish_time_1 = time.time() - start_time_1
    # print(f'{finish_time_1} линейный')

    start_time_2 = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    finish_time_2 = time.time() - start_time_2
    print(f'{finish_time_2} многопроцессный')

