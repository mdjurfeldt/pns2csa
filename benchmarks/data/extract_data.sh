grep -h 'CSAConnector' *runtime_*.log > data_runtime.log
grep -h 'CSAConnector' *strong_scaling_*.log > data_strong_scaling.log
grep -h 'CSAConnector' *weak_scaling_*.log > data_weak_scaling.log
grep -h 'RandomConvergent\|FixedProbability' *runtime_*.log > data_native_runtime.log
grep -h 'RandomConvergent\|FixedProbability' *scaling_*.log > data_native_scaling.log
