
for jobfile in run_bench_*.jdf; do
  qsub $jobfile
done