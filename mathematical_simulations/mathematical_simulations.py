import numpy as np


def Kraus_solver(rho, channel, probability_of_decay, steps):
    if channel=="amplitude_dampening":
        E0=np.array([[1, 0], [0, np.sqrt(1-probability_of_decay)]])
        E1=np.array([[0, np.sqrt(probability_of_decay)],[0, 0]])
    elif channel=="phase_dampening":
        E0=np.array([[1, 0], [0, np.sqrt(1-probability_of_decay)]])
        E1=np.array([[0, 0],[0, np.sqrt(probability_of_decay]])
    else:
        raise ValueError("Incorrect channel passed")


    tabulated_rho=np.zeros((steps, 2, 2), dtype=complex)
    for i in range(steps):
        rho=E0@rho@E0.conj().T+E1@rho@E1.conj().T
        tabulated_rho[i]=rho
    return tabulated_rho

def Lindblad_solver():

def density_matrix_solver(initial_rho, channel, probability_of_decay, solver, steps):
    """
    Density matrix solver that determines if given a quantum system starting at a known configuration, how does the state change over time when subjected to environmental noise. 

    Inputs
    ------
    initial_rho: np.ndarray
        The initial qubit
    channel: str
        Indicates if we are looking at a "phase_dampening" or "amplitude_dampening" problem
    probability_of_decay: float
        Likelihood of decay with each step
    solver: str
        "Kraus" for discrete probailistic interpretation of noise or "Lindblad" for continuous interpretation of noise
    """

    
