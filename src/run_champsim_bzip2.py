import subprocess as sp
import re
import os
num_ways = ['8', '16']
num_sets = ['2048', '8192']
l1d_prefs = ['no', 'next_line']
l2c_prefs = ['no', 'ip_stride']
llc_rpls = ['lru', 'drrip', 'srrip']
champsim_dir = '/home/jiaqi/CA_Grad_Lab/ChampSim'
work_dir = '/home/jiaqi/CA_Grad_Lab/lab'
bin_dir = champsim_dir+'/bin'
res_dir = work_dir + '/results_29M'
trace_dir = work_dir + '/traces'

def run_champsim(benchmark):
	res_path = res_dir+'/'+benchmark
	sp.call('mkdir -p '+res_path, shell=True)
	traces = [trace_dir+'/'+i for i in os.listdir(trace_dir) if i.startswith(benchmark) and i.endswith('.gz')]
	for trace in traces:
		trace_name = trace.split('/')[-1][:-3]
		for num_way in num_ways:
			for num_set in num_sets:
				for l1d_pref in l1d_prefs:
					for l2c_pref in l2c_prefs:
						for llc_rpl in llc_rpls:
							binary = ''.join([bin_dir,'/','bimodal-',l1d_pref,'-',l2c_pref,'-',llc_rpl,'-1core','-s',num_set,'-w',num_way])
							binary_name = binary.split('/')[-1]
							command = ''.join(['(',binary,' -warmup_instructions 1000000 -simulation_instructions 29000000 -traces ',trace,')',' &> ',res_path,'/',trace_name,'+',binary_name,'.txt'])
							print(command)
							sp.call(command, shell=True)
					
def rename_exe(l1d_pref, l2c_pref, llc_rpl,num_set, num_way):
	old_name = ''.join([champsim_dir,'/bin/','bimodal-',l1d_pref,'-',l2c_pref,'-',llc_rpl,'-1core'])
	new_name = ''.join([old_name,'-s',num_set,'-w',num_way])
	command = ''.join(['mv ',old_name,' ',new_name])
	print(command)
	sp.call(command, shell=True)
if __name__ == '__main__':
	run_champsim('bzip2')


