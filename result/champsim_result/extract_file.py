import shutil
import os

benchmarks = ['bzip2', 'cactusADM', 'hmmer', 'mcf', 'sphinx3']
combination = [('2048', '16'), ('4096','16'),('8192','16'),('16384','16'),('16384','8'),('4096','32')]
def delete_useless_file(benchmark):
    files = [i for i in os.listdir(f'./{benchmark}')]
    files_pick = []
    for num_set, num_way in combination:
        files_pick += [i for i in files if i.endswith(f'-s{num_set}-w{num_way}.txt')]
    print(files_pick)
    print(len(files_pick))
    try:
        os.mkdir(f'./{benchmark}-new')
    except:
        pass
    for i in files_pick:
        shutil.copyfile(f'./{benchmark}/{i}', f'./{benchmark}-new/{i}')

if __name__ == '__main__':
    for i in benchmarks:
        delete_useless_file(i)

