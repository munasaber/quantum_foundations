import qiskit_nature
import qiskit
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import ParityMapper
from qiskit_nature.second_q.circuit.library import HartreeFock
from qiskit_nature.second_q.circuit.library import UCCSD
from qiskit_aer.primitives import EstimatorV2
from qiskit_algorithms.optimizers import SPSA
from qiskit_algorithms import VQE
from qiskit_nature.second_q.algorithms import GroundStateEigensolver

###First: We construct the initial Hydrogen molecule that are positioned 0.74 Angstrom apart, in line with the bond length of a Hydrogen molecule, and run the electronic structure calculation
driver=PySCFDriver(atom='H 0.0 0.0 0.0; H 0.0 0.0 0.74')
electronic_structure_calc=driver.run()

###Second: We map this hydrogen molecule onto qubits (4 qubits; 2 spin states and 2 spatial orbitals)
mapping=ParityMapper()

###Third: We construct the initial state for the quantum circuit
initial=HartreeFock(electronic_structure_calc.num_spatial_orbitals, electronic_structure_calc.num_particles, mapping)

###Fourth: We construct the ansatz (the search circuit) with the UCC ansatz
ansatz=UCCSD(electronic_structure_calc.num_spatial_orbitals, electronic_structure_calc.num_particles, mapping, reps=1, initial_state=initial, generalized=False, preserve_spin=True, include_imaginary=False)

###Fifth: Perform VQE and transforms the fermions to qubits
estimator=EstimatorV2(options={"default_precision": 1e-2})
optimizer=SPSA(maxiter=50)
vqe=VQE(estimator, ansatz, optimizer)
algorithm_orchestration=GroundStateEigensolver(mapping, vqe)

###Sixth: Execute 
result=algorithm_orchestration.solve(electronic_structure_calc)


###Seventh: Check results
