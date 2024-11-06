from spm.__wrapper__ import Runtime


def Markov_blankets_and_NESS(*args, **kwargs):
    """
      Meta-modelling of Bayes-optimal responses (Newton's method)  
        FORMAT Markov_blankets_and_NESS  
         
        This demonstration routine deals with the conditional independence in  
        this induced by sparse coupling in a random dynamical systems, where the  
        sparse coupling is characterised in terms of the system's Jacobian. At  
        nonequilibrium steady-state, this places linear constraints on the  
        solenoidal flow (denoted by Q) under a Helmholtz decomposition. The  
        resulting curvature of the log density and at nonequilibrium steady-state  
        encodes conditional independencies; i.e., when the Hessian is zero. What  
        follows are a series of notes illustrating the conditions under which  
        conditional independence between internal and external states under a  
        Markov blanket partition emerges, either asymptotically as the system  
        becomes more dissipative - or under a particular constraints on the  
        Jacobian. When invoked symbolic maths is used to illustrate an analytic  
        solution for a simple the canonical Markov blanket, using a single  
        dimensional state for each subset of a Markovian position. Numerical  
        analyses are then used to illustrate how this generalises to high  
        dimensional systems. Subsequent notes drill down on particular instances  
        in the literature.  
         
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/Markov_blankets_and_NESS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("Markov_blankets_and_NESS", *args, **kwargs, nargout=0)
