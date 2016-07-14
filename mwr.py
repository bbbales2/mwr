# Code adapted from Gillespy Example
# Model from Internal Huctuations in a model of chemical chaos, J. Guemez, M. A. Matias

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path[:0] = ['..']

import gillespy

V = 10.0

class Simple1(gillespy.Model):
    """
    This is a simple example for mass-action degradation of species S.
    """

    def __init__(self, parameter_values=None):

        # Initialize the model.
        gillespy.Model.__init__(self, name="mwr")
        
        # Parameters
        k1 = gillespy.Parameter(name = 'k1', expression = 30.0)
        self.add_parameter(k1)
        k2 = gillespy.Parameter(name = 'k2', expression = 1.0 / V)
        self.add_parameter(k2)
        k3 = gillespy.Parameter(name = 'k3', expression = 10.0)
        self.add_parameter(k3)
        k4 = gillespy.Parameter(name = 'k4', expression = 0.4 / V)
        self.add_parameter(k4)
        k5 = gillespy.Parameter(name = 'k5', expression = 16.5)
        self.add_parameter(k5)

        km1 = gillespy.Parameter(name = 'km1', expression = 2 * 0.25 / V)
        self.add_parameter(km1)
        km5 = gillespy.Parameter(name = 'km5', expression = 2 * 0.5 / V)
        self.add_parameter(km5)
        
        # Species
        A = gillespy.Species(name = 'A', initial_value = 100)
        self.add_species(A)
        B = gillespy.Species(name = 'B', initial_value = 100)
        self.add_species(B)
        C = gillespy.Species(name = 'C', initial_value = 50)
        self.add_species(C)
        
        # Reactions
        rxn1 = gillespy.Reaction(
                name = 'A -> 2A',
                reactants = { A : 1 },
                products = { A : 2 },
                rate = k1 )
        self.add_reaction(rxn1)

        rxn2 = gillespy.Reaction(
                name = '2A -> A',
                reactants = { A : 2 },
                products = { A : 1 },
                rate = km1 )
        self.add_reaction(rxn2)

        rxn3 = gillespy.Reaction(
                name = 'A + B -> 2B',
                reactants = { A : 1,
                              B : 1 },
                products = { B : 2 },
                rate = k2 )
        self.add_reaction(rxn3)

        rxn4 = gillespy.Reaction(
                name = 'A + C -> null',
                reactants = { A : 1,
                              C : 1 },
                products = {},
                rate = k4 )
        self.add_reaction(rxn4)

        rxn5 = gillespy.Reaction(
                name = 'B -> null',
                reactants = { B : 1 },
                products = {},
                rate = k3 )
        self.add_reaction(rxn5)

        rxn6 = gillespy.Reaction(
                name = 'C -> 2C',
                reactants = { C : 1 },
                products = { C : 2 },
                rate = k5 )
        self.add_reaction(rxn6)

        rxn7 = gillespy.Reaction(
                name = '2C -> C',
                reactants = { C : 2 },
                products = { C : 1 },
                rate = km5 )
        self.add_reaction(rxn7)

        self.timespan(np.linspace(0, 10, 101))

if __name__ == '__main__':

    # Here, we create the model object.
    # We could pass new parameter values to this model here if we wished.
    simple_model = Simple1()
    
    # The model object is simulated with the StochKit solver, and 25 
    # trajectories are returned.
    simple_trajectories = simple_model.run(number_of_trajectories = 1)

    # extract time values
    time = np.array(simple_trajectories[0][:, 0])

    # extract just the trajectories for S into a numpy array
    plt.figure()
    plt.plot(time, simple_trajectories[0][:, 1], 'r-')
    plt.plot(time, simple_trajectories[0][:, 2], 'k--')
    plt.plot(time, simple_trajectories[0][:, 3], 'b.-')

    plt.xlabel('Time')
    plt.title('Two trajectories')
    
    plt.legend(['A', 'B', 'C'])
    plt.show()

    
    
    
    
    
    
    
    
    
    
    
    
    
