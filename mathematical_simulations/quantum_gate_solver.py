"""This module contains functions for solving for the final state after a qubit passes through two gates (Hadamard gate and a NOT gate, starting from the ground state"""
import numpy as np


def apply_gate(qubit: np.array, gate_type: str):
    """
    This function applies a Hadamard or NOT (Pauli-X) gate to a qubit

    Inputs
    ------
    qubit: np.array
        Qubit that is the object on which gate operations will be performed
    gate_type: str
        Gate to be applied to the qubit with options "Hadamard or NOT"

    """
    if gate_type.lower()=="hadamard":
        gate=1/np.sqrt(2)*np.array([[1 , 1],[1 , -1]])
    elif gate_type.lower()=="not":
        gate=np.array([[0, 1],[1 , 0]])
    else:
        raise ValueError("Incorrect gate_type. Please enter Hadamard or NOT for the gate_type")
    return gate@qubit

