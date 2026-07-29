"""This module contains functions for solving the question of using a Hadamard test circuit to calculate the real part of the expectation value of a Pauli-Z gate acting on a qubit in the excited state"""


def Hadamard_test(qubit: np.array, operator: np.array):
    """
    This function applies an operator to the qubit to get the expectation value (for a Pauli-Z gate the circuit should give an expectation value of -1).
    
    Inputs
    ------
    qubit : np.array
        Initial qubit
    operator : np.array
        User defined operator (base assumption is Pauli-Z gate operator)
    """
    #ancillary probe qubit
    ancillary_qubit=np.array([[1],[0]])
    hadamard_op=1/np.sqrt(2)*np.array([[1,1],[1,-1]])
    initial_state= np.kron(ancillary_qubit, qubit)
    
    #initial Hadamard operation
    H_cross_ancillary=np.kron(hadamard_op, np.eye(2))@initial_state
    projection_0=np.array([[1, 0],[0, 0]])
    projection_1=np.array([[0, 0],[0, 1]])
    controlled_operator=np.kron(projection_0, np.eye(2))+np.kron(projection_1, operator)
    intermediate_state=controlled_operator@H_cross_ancillary
    
    #Secondary Hadamard operation
    intermediate_state=np.kron(hadamard_op, np.eye(2))@intermediate_state
    
    #determine probabilities
    top_2=np.abs(intermediate_state[0,0])**2+np.abs(intermediate_state[1,0])**2
    bottom_2=np.abs(intermediate_state[2,0])**2+np.abs(intermediate_state[3,0])**2

    return float(top_2-bottom_2)

