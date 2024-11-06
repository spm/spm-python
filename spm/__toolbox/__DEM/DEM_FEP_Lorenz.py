from spm.__wrapper__ import Runtime


def DEM_FEP_Lorenz(*args, **kwargs):
    """
     --------------------------------------------------------------------------  
        This is a simple demonstration of deterministic convergence to  
        nonequilibrium steady-state, using the Lorenz system. Deterministic  
        solutions (with a Rayleigh parameter of 28) are obtained for 2048 initial  
        states, integrating over eight seconds (with a time step of 1/64  
        seconds). Crucially, the initial autonomous states are the same for each  
        solution and yet the final density over the autonomous (i.e., active)  
        state converges to the non-equilibrium steady-state density over time.  
        This is apparent in the collapse of the divergence between the sample  
        densities (over all states) and the final (NESS) density - as evaluated  
        simply using a Gaussian approximation to the ensemble densities at each  
        point in time. The upper plots show the propagated states at four points  
        in time. As time progresses, this density comes to assume the familiar  
        butterfly form of the Lorenz attractor. However, these states are not  
        trajectories through state space, they are the endpoints of paths from an  
        ensemble of starting locations (shown in the right plot). In this  
        illustration, we treat the first state of the Lorenz system as the active  
        state, the second state as the sensory state and the third state plays  
        the role of an external or hidden state. This designation is based upon  
        the fact that the first state is not influenced by the first. In short,  
        this numerical example shows how uncertainty about external states is  
        propagated over time to induce uncertainty about a particle's state; even  
        when the initial (particular) state is known.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_FEP_Lorenz.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_FEP_Lorenz", *args, **kwargs, nargout=0)
