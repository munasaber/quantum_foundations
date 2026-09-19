import qiskit_nature
import qiskit
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mapppers import ParityMapper
from qiskit_nature.second_q.circuit import HartreeFock


###First: We construct the initial Hydrogen molecule that are positioned 0.74 Angstrom apart, in line with the bond length of a Hydrogen molecule, and run the electronic structure calculation

driver=PySCFDriver(atom='H 0.0 0.0 0.0; H 0.0 0.0 0.74')
electronic_structure_calc=driver.run()

###Second: We map this hydrogen molecule onto qubits (4 qubits; 2 spin states and 2 spatial orbitals)
mapping=ParityMapper()

###Third: We construct the initial state for the quantum circuit
initial=HartreFock(electronic_structure_calc.num_spatial_orbitals, electronic_structure_calc.num_particles, mapping)

###Fourth: We construct the ansatz (the search circuit)


###Fifth: Perform VQE


###Sixth: execute and check results

