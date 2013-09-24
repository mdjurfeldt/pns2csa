
for n in 100; do

  python PyNN_CSAConnector_csa.py $n > PyNN_CSAConnector_csa_$n.log
  echo "\n\n\n\n\n"
  python PyNN_CSAConnector_libcsa.py $n > PyNN_CSAConnector_libcsa_$n.log
  echo "\n\n\n\n\n"

  python nest_CSAConnector_csa.py $n > nest_CSAConnector_csa_$n.log
  echo "\n\n\n\n\n"
  python nest_CSAConnector_libcsa.py $n > nest_CSAConnector_libcsa_$n.log
  echo "\n\n\n\n\n"

done

