
for n in 100000; do

  python PyNN_CSAConnector_csa_runtime.py $n > data/PyNN_CSAConnector_csa_runtime_$n.log
  python PyNN_CSAConnector_libcsa_runtime.py $n > data/PyNN_CSAConnector_libcsa_runtime_$n.log
  python nest_CSAConnector_csa_runtime.py $n > data/nest_CSAConnector_csa_runtime_$n.log
  python nest_CSAConnector_libcsa_runtime.py $n > data/nest_CSAConnector_libcsa_runtime_$n.log
  python PyNN_FixedProbabilityConnector_runtime.py $n > data/PyNN_FixedProbabilityConnector_runtime_$n.log
  python nest_RandomConvergentConnect_runtime.py $n > data/nest_RandomConvergentConnect_runtime_$n.log

done
