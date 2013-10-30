
for np in 1 2 4 6 12 24 48; do

  nn=`python get_num_neurons_weak_scaling.py $np`

  mpirun -np $np python PyNN_CSAConnector_csa_scaling.py $nn $np > data/PyNN_CSAConnector_csa_weak_scaling_$np.log
  mpirun -np $np python PyNN_CSAConnector_libcsa_scaling.py $nn $np > data/PyNN_CSAConnector_libcsa_weak_scaling_$np.log
  mpirun -np $np python nest_CSAConnector_csa_scaling.py $nn $np > data/nest_CSAConnector_csa_weak_scaling_$np.log
  mpirun -np $np python nest_CSAConnector_libcsa_scaling.py $nn $np > data/nest_CSAConnector_libcsa_weak_scaling_$np.log
  mpirun -np $np python PyNN_FixedProbabilityConnector_scaling.py $nn $np > data/PyNN_FixedProbabilityConnector_scaling_$np.log
  mpirun -np $np python nest_RandomConvergentConnect_scaling.py $nn $np > data/nest_RandomConvergentConnect_scaling_$np.log

done
