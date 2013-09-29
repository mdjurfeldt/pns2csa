#PBS -l nodes=1:ppn=48
#PBS -q medium
#PBS -o /users/eppler/CSA/CSAConnector/${PBS_JOBID}.o
#PBS -e /users/eppler/CSA/CSAConnector/${PBS_JOBID}.e

. /users/eppler/CSA/CSAConnector/enable.sh
cd /users/eppler/CSA/CSAConnector
bash do_bench_runtime_scaling.sh
