import qiskit_nature
import qiskit
from qiskit_nature.second_q.drivers import PySCFDriver

"""
First we construct the initial Hydrogen molecule that are positioned 0.74 Angstrom apart, in line with the bond length of a Hydrogen molecule, and run the electronic structure calculation
"""
driver=PySCFDriver(atom='H 0.0 0.0 0.0; H 0.0 0.0 0.74')
electronic_structure_calc=driver.run()

