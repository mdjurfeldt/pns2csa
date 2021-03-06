
for np in 1 2 4 6 12 24 48; do

  # mpirun -np $np python PyNN_CSAConnector_csa_scaling.py 48000 $np > data/PyNN_CSAConnector_csa_strong_scaling_$np.log
  # mpirun -np $np python PyNN_CSAConnector_libcsa_scaling.py 48000 $np > data/PyNN_CSAConnector_libcsa_strong_scaling_$np.log
  # mpirun -np $np python nest_CSAConnector_csa_scaling.py 48000 $np > data/nest_CSAConnector_csa_strong_scaling_$np.log
  # mpirun -np $np python nest_CSAConnector_libcsa_scaling.py 48000 $np > data/nest_CSAConnector_libcsa_strong_scaling_$np.log
  mpirun -np $np python PyNN_FixedProbabilityConnector_scaling.py 48000 $np > data/PyNN_FixedProbabilityConnector_strong_scaling_$np.log
  mpirun -np $np python nest_RandomConvergentConnect_scaling.py 48000 $np > data/nest_RandomConvergentConnect_strong_scaling_$np.log

done
