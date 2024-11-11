from spm.__wrapper__ import Runtime


def FEP_information_length(*args, **kwargs):
    """
      Demonstration of density dynamics and information length  
        FORMAT FEP_information_length(gi,qi,ci,fi)  
       --------------------------------------------------------------------------  
        gi  - scaling of (isotropic) random fluctuations; i.e., dissipative flow  
        qi  - scaling of solenoidal flow; i.e., conservative flow  
        ci  - colour index for plotting  
        fi  - optional flag to print functional forms  
        ti  - optional flag to reverse time halfway through the simulation  
       __________________________________________________________________________  
        This demonstration routine illustrates the key role of solenoidal flow  
        (that breaks detailed balance) in optimisation and self-organisation. The  
        first section shows that increasing solenoid flow leads to mixing that  
        accelerates the convergence of a random dynamical system to its  
        (nonequilibrium) steady-state or free energy minimum. Heuristically,  
        solenoidal flow—on the level set of on objective function (here the log  
        density of the said steady state)—can be regarded as searching for  
        ‘points of entry’ in state space with 'steep' gradients. The key  
        observation here is that the rate of convergence, scored with the  
        divergence between the current and final density, increases with the  
        relative amount of solenoidal mixing. This is accompanied by an increase  
        in the information length from any initial density to the density in the  
        long-term future.  
         
        The second section rehearses the same mechanics but in the context of  
        self-organisation. To talk about self organisation it is necessary to  
        separate the self from nonself by constructing a random dynamical system  
        with a Markov blanket. One can then associate the conditional density  
        over external states, conditioned on blanket states, with a Bayesian  
        belief encoded by internal states. This corresponds to the variational  
        density that underwrites the free energy principle (under some  
        simplifying assumptions). The marginal density over particular (i.e.,  
        internal states and their blanket) states now plays the role of a  
        description of the dynamics of a particle, that shows the same  
        dependencies on solenoidal flow above. Namely, increasing solenoidal flow  
        decreases the path integral of divergence or the rate of convergence to  
        nonequilibrium steady-state. At the same time, the information length of  
        paths into the future increases. The accompanying information theoretic  
        measures—of the conditional density over external states and particular  
        states—can be read as unfolding in extrinsic and intrinsic information  
        geometries, respectively. These conjugate geometries can, in turn, be  
        associated with variational free energy and thermodynamic free energy.  
         
        An increase in solenoidal flow, relative to dissipative flow, goes  
        hand-in-hand with the size of a particle, where random fluctuations are  
        averaged away. In other words, large particles are necessarily precise  
        particles that feature solenoidal flows. These flows underwrite a rapid  
        convergence to nonequilibrium steady-state from any initial conditions  
        that, necessarily, entail large information lengths. In short, large,  
        precise particles have an itinerant aspect to their dynamics and move  
        through many discernible probabilistic configurations from any initial  
        density. This itinerancy lends precise particles an elemental kind of  
        memory, in the sense that running the system backwards in time evinces a  
        greater number of discernible belief states. This number corresponds to  
        the information length, while the rate at which discernible belief states  
        emerge corresponds to the information rate.  
         
        Note that we can run the system forwards and backwards in time with  
        impunity because the density dynamics are deterministic (as opposed to  
        any stochastic path). This behaviour can be demonstrated by calling the  
        current routine with an additional argument that reverses the direction  
        of time halfway through a simulation.  
         
        Please see the annotated code below for further details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_information_length.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FEP_information_length", *args, **kwargs, nargout=0)
