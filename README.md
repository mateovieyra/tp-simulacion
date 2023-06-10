# Assignment: Simulación
---
This is the evaluative practical work of the subject "Simulacion" for Computer Science career of the National University of Rio Cuarto.

## Install dependencies.

For installing the dependencies of this project, first we must create a virtual environment, due to the project's programming language is Python.

### Python version

***Python 3.8.10 or later is recommended.***

### Create virtual environment

To create a virtual environment, run the following command on your terminal:

```
python3 -m venv venv
```

To activate the virtual environment from Linux:
```
source venv/bin/activate
```

To deactivate the virtual environment:
```
deactivate
```

### Install dependencies

For Python 3.4 or later, ```pip``` is included by default. So you must run the following command in your terminal to install the dependencies, **with your venv activated**:

```
pip install -r requirements.txt
```

Then, you will be installing on your venv the [Matplotlib](https://matplotlib.org/) library, for the experiment's plot visualization.

---

## Run project

You can execute the main function of the project by running the following command on your terminal:

```
python3 -m virus_propagation -t X -d X -b X -v X -s X -i X -r X  
```

To observe the data, you must replace all the X's characters with the corresponding parameters. These parameters are:

```
-t: Time in days of the simulation.
-d: H parameter. Step measure in hours.
-b: Beta. Per-capita infection rate.
-v: V parameter. Retirement rate.
-s: S0. Initial value of Susceptible People.
-i: I0. Initial value of Infected People.
-r: R0. Initial value of Retired People.
```

To observe the experiments, you can run the following commands: 

### Experiment 1

```
python3 -m virus_propagation -t 20 -d 1 -b 0.0022 -v 0.4477 -s 763 -i 1 -r 0
```

### Experiment 2.1

```
python3 -m virus_propagation -t 20 -d 1 -b 0.0044 -v 0.10 -s 763 -i 1 -r 0
```

### Experiment 2.2

```
python3 -m virus_propagation -t 60 -d 1 -b 0.0044 -v 0.10 -s 763 -i 1 -r 0
```

### Experiment 3.1

```
python3 -m virus_propagation -t 20 -d 1 -b 0.0011 -v 0.4477 -s 763 -i 1 -r 0
```

### Experiment 3.2

```
python3 -m virus_propagation -t 50 -d 1 -b 0.0011 -v 0.4477 -s 763 -i 1 -r 0
```

---

## Project Structure

This project contains the following main files:

- `virus_propagation.py`: This file contains the main function, the plot generator.
- `functions.py`: This file contains the functions that generates the data displayed in the plot.
- `parser_1.py`: This file contains the function that captures the input from command line.
- `requirements.txt`: This file contains the dependencies of the project.