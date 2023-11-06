ChipPilot seeks to explore the design parameters of iEDA, which is an open source EDA toolset for physical design of integrated circuits, for better performance, power, and area a.k.a PPA. The basic idea is to leverage parallel Bayesis optimization to explore optimized configurations of iEDA and accelerate the parameter evaluation using taskflow, which is a parallel task processing engine for dependent tasks with distinct granularities, at the same time. While tasks within iEDA can vary in terms of runtime, memory, and computing resources depending on the inputs which are usually overlooked by the task processing engines, we utilize machine learning to conduct the prediction of CPUs, memory, and runtime and feed these predictions to the parallel task processing engine to further improve the speed of parameter evaluation.  

# usage

```shell
$ docker run --rm -it -v $(pwd):/ChipPilot ubuntu:20.04 bash
$ apt update
$ apt install python3
$ apt install python3-pip
$ pip install optuna
$ cd /cad_dse && python3 report.py
```# ChipPilot
