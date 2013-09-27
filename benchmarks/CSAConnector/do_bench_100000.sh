
for n in 100000; do

  python PyNN_CSAConnector_csa.py $n > data/PyNN_CSAConnector_csa_$n.log
  # Does not work at the moment, due to restrictions in libcsa
  # python PyNN_CSAConnector_libcsa.py $n > data/PyNN_CSAConnector_libcsa_$n.log
  python nest_CSAConnector_csa.py $n > data/nest_CSAConnector_csa_$n.log
  python nest_CSAConnector_libcsa.py $n > data/nest_CSAConnector_libcsa_$n.log

done
