from spm._runtime import Runtime


def DEM_swarm(*args, **kwargs):
    r"""
      This routine illustrates self-organisation and swarming under active  
        inference (free energy minimisation).  It exploits the fact that one can  
        express a joint-systems (marginal) Lyapunov function in terms of a  
        variational free energy. This means that one can prescribe an attracting  
        set in terms of the generative model that defines variational free  
        energy.  In this example, the attracting set is an orbit in the phase  
        space of an ensemble (e.g., swarm of drones): where the states correspond  
        to the location and (radio) signal expression of 8 agents. In essence,  
        the systems dynamics rest upon each agent inferring its unique identity  
        (in relation to all others) and behaving in accord with those inferences;  
        in other words, inferring its place in the assembly and realising those  
        inferences by moving.  In this example, the behaviour is rendered  
        autonomous by including hidden states that evolve in time. This allows  
        the frame of reference (within which agents communicate) to change  
        systematically. In this example, this frame of reference uses affine  
        transformations to simulate sequences of swarm dynamics.  
         
        This scheme can be compared with the morphogenesis simulations. The key  
        difference is that we are now dealing with an autonomous system in which  
        behaviour is prescribed by the internal (autonomous) dynamics of the  
        generative model.  
        _________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_swarm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_swarm", *args, **kwargs)
