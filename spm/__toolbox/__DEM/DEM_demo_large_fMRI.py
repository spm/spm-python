from spm.__wrapper__ import Runtime


def DEM_demo_large_fMRI(*args, **kwargs):
    """
      Demonstration of DCM for CSD (fMRI) with simulated responses  
       __________________________________________________________________________  
        This routine demonstrates Bayesian parameter averaging using the  
        variational inversion of spectral DCMs for fMRI. A random connectivity  
        matrix is generated and inverted. The posterior estimates are then used  
        to create new data, that are used to invert a series of DCMs. After each  
        inversion, basing parameter averaging is used to illustrate convergence  
        to the true values. In principle, this routine can handle large DCMs.  
        We illustrate (for time convenience) the inversion of eight nodes and 64  
        connections.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_large_fMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_large_fMRI", *args, **kwargs, nargout=0)
