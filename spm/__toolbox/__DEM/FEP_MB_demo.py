from spm.__wrapper__ import Runtime


def FEP_MB_demo(*args, **kwargs):
    """
      This  routine illustrates a hierarchical decomposition of Markov blankets  
        (of Markov blankets). It rests upon the dual operators of finding a  
        partition (a Markov partition) and then using an adiabatic dimensional  
        reduction (using the eigensolution of the Markov blanket). In brief, this  
        means the states of particles at the next level become mixtures of the  
        Markov blanket of particles at the level below.  
         
        The ensuing hierarchical decomposition is illustrated in terms of  
        Jacobians and locations in a scaling space (evaluated using the graph  
        Laplacian). This demonstration uses a fictive Jacobian that is created by  
        hand - or the equivalent Jacobian of a synthetic soup (i.e., active  
        matter)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/FEP_MB_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("FEP_MB_demo", *args, **kwargs, nargout=0)
