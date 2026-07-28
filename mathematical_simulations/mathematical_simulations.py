import numpy as np


def Kraus_solver(rho, channel, probability_of_decay, steps):
    """
    Uses the Kraus operator to calculate the density matrix.
    
    Inputs
    ------
    initial_rho: np.ndarray
        The initial qubit
    channel: str
        Indicates if we are looking at a "phase_dampening" or "amplitude_dampening" problem
    probability_of_decay: float
        Likelihood of decay with each step
    steps: int
        Number of steps for Kraus algorithm
    """
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


def Lindblad_solver(rho, channel, probability_of_decay, time, H):
    """
    Uses the Lindblad master equation to calculate the density matrix under continuous time evolution. 
    
    Inputs
    ------
    initial_rho: np.ndarray
        The initial qubit
    channel: str
        Indicates if we are looking at a "phase_dampening" or "amplitude_dampening" problem
    probability_of_decay: float
        Likelihood of decay with each step
    time: tuple
        Initial and final timescale for tracking time evolution of the system
    H: np.array
        Hamiltonian in the form of a 2X2 array.
    """
    gamma=1/(time[1]-time[0])
    if channel=="amplitude_dampening":
        L=np.sqrt(gamma)*np.array([[0,1], [0,0]])
    elif channel=="phase_dampening":
        L=np.sqrt(gamma)*np.array([[1,0], [0,-1]])
    else:
        raise ValueError("Incorrect channel passed")
    tabulated_drho_dt=np.zeros((steps, 2, 2), dtype=complex)
    for i in range(time[0], time[1]):
        unitary_multiplication=complex(0,-1)*(H@rho-rho@H)
        drho_dt=unitary_multiplication+L@rho@L.conj().T-0.5*((L.conj().T@L)@rho+rho@(L.conj().T@L))
        tabulated_drho_dt[i]=drho_dt
    tabulated_rho=scipy.integrate.solve_ivp(tabulated_drho_dt)
    return tabulated_rho

def density_matrix_solver(initial_rho, channel, probability_of_decay, solver, steps_or_time, H=None):
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
    steps_or_time: int/tuple
        Number of steps for Kraus algorithm or time tuple for Linblad algorithm
    H: np.array
        Hamiltonian in the form of a 2X2 array.
    """
    if solver.lower()=="kraus":
        return Kraus_solver(initial_rho, channel, probability_of_decay, steps_or_time)
    elif solver.lower()=="Lindblad":
        if H==None:
            raise ValueError("Hamiltonian needed for Lindblad solver")       
        return Lindblad_solver(initial_rho, channel, probability_of_decay, steps_or_time, H)

    
