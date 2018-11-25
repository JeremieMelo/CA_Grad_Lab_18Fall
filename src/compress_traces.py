import subprocess as sp
import re
import os
num_ways = ['8', '16']
num_sets = ['2048', '8192']
l1d_prefs = ['no', 'next_line']
l2c_prefs = ['no', 'ip_stride']
llc_rpls = ['lru', 'drrip', 'srrip']
champsim_dir = '/home/jiaqi/CA_Grad_Lab/ChampSim'
bin_dir = champsim_dir+'/bin'
res_dir = './results_29M'
trace_dir = './traces'

def compress_trace():
	traces = [trace_dir+'/'+i for i in os.listdir(trace_dir) if not i.endswith('.gz')]
	for trace in traces:
		sp.call('gzip '+trace, shell=True)

if __name__ == '__main__':
	compress_trace()


