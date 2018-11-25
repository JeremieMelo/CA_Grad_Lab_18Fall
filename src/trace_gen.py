import subprocess as sp
bzip2_start = [8070001932, 18120004274,3090000819,23790005563,51780011854]
bzip2_end = [8100001938,18150004329,3120000820,23820005573,51810011856]
mcf_start = [57840010926,116520019948,267660041304,95160014702]
mcf_end = [57870010926,116550019968,267690041306,95190014707]
cactusADM_start = [278250248589,2280152045099,186330166230]
cactusADM_end = [278280248592,2280182045141,186360166263]
hmmer_start = [40980020068,317520157280,368940182854,342870169847]
hmmer_end = [41010020085,317550157302,368970182863,342900169848]
sphinx3_start = [1641630399809,137700030560,1045680248842,1038870247205,2087850516085]
sphinx3_end = [1641660399816,137730030563,1045710248843,1038900247221,2087880516098]
pintool = '/home/jiaqi/CA_Grad_Lab/pinplay-3.5/pin'
tracer_so = '/home/jiaqi/CA_Grad_Lab/ChampSim/tracer/obj-intel64/champsim_tracer.so'
trace_dir = '/home/jiaqi/CA_Grad_Lab/lab/traces'

data = {'bzip2':{'start':bzip2_start, 'end':bzip2_end, 'run_cmd' : './bzip2_base.amd64-m64-gcc43-nn ./input.source'},
		'mcf':{'start':mcf_start, 'end':mcf_end, 'run_cmd' : './mcf_base.amd64-m64-gcc43-nn ./inp.in'},
		'cactusADM':{'start':cactusADM_start, 'end':cactusADM_end, 'run_cmd' : './cactusADM_base.amd64-m64-gcc43-nn ./benchADM.par'},
		'hmmer':{'start':hmmer_start, 'end':hmmer_end, 'run_cmd' : './hmmer_base.amd64-m64-gcc43-nn ./nph3.hmm ./swiss41'},
		'sphinx3':{'start':sphinx3_start, 'end':sphinx3_end, 'run_cmd' : './sphinx_livepretend_base.amd64-m64-gcc43-nn ./ctlfile ./ ./args.an4'}}

def gen_trace(benchmark, simpoint):
	run_cmd = simpoint['run_cmd']
	starts = simpoint['start']
	ends = simpoint['end']
	for start, end in zip(starts, ends):
		skip = str(start)
		length = str(end-start)
		trace_file = ''.join([trace_dir,"/",benchmark,'-',skip,'-trace'])
		command = ''.join([pintool,' -ifeellucky ','-t ',tracer_so,' -o ',trace_file,' -s ',skip,' -t ',length,' -- ',run_cmd])
		print(command)
		sp.call(command, shell=True)
if __name__ == '__main__':
	benchmark = 'sphinx3'
	gen_trace(benchmark, data[benchmark])

