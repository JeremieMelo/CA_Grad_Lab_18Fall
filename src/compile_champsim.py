import subprocess as sp
import re
num_ways = ['4', '8', '16']
num_sets = ['2048', '8192']
l1d_prefs = ['no', 'next_line']
l2c_prefs = ['no', 'ip_stride']
llc_rpls = ['lru', 'drrip', 'srrip']
champsim_dir = '/home/jiaqi/CA_Grad_Lab/ChampSim'
    
def compile_champsim():
	build_sh = champsim_dir + '/build_champsim.sh'
	for l1d_pref in l1d_prefs:
		for l2c_pref in l2c_prefs:
			for llc_rpl in llc_rpls:
				command = ''.join([build_sh,' bimodal ',l1d_pref,' ',l2c_pref,' ',llc_rpl,' ', '1'])
				print(command)
				sp.call(command, shell=True)
				rename_exe(l1d_pref, l2c_pref, llc_rpl, '8192', '16')
def rename_exe(l1d_pref, l2c_pref, llc_rpl,num_set, num_way):
	old_name = ''.join([champsim_dir,'/bin/','bimodal-',l1d_pref,'-',l2c_pref,'-',llc_rpl,'-1core'])
	new_name = ''.join([old_name,'-s',num_set,'-w',num_way])
	command = ''.join(['mv ',old_name,' ',new_name])
	print(command)
	sp.call(command, shell=True)
if __name__ == '__main__':
	compile_champsim()


