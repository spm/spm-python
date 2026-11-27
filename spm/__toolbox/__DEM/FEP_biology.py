from spm._runtime import Runtime


def FEP_biology(*args, **kwargs):
    r"""
      This demonstration  uses an ensemble of particles with intrinsic (Lorenz  
        attractor) dynamics and (Newtonian) short-range coupling. The setup is  
        used to solve for dynamics among an ensemble of particles; from which a  
        Markov blanket emerges, which forms a particle at the next hierarchical  
        scale. These ensemble dynamics are then used to illustrate different  
        perspectives; namely, those afforded by quantum, statistical, classical  
        and Bayesian mechanics. A detailed description of each of these three  
        treatments precedes each of the sections in the script. these  
        descriptions are in the form of a figure legend, where each section is  
        summarised with a figure.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/FEP_biology.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("FEP_biology", *args, **kwargs, nargout=0)
