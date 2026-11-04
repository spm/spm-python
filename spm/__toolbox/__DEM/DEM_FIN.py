from spm._runtime import Runtime


def DEM_FIN(*args, **kwargs):
    r"""
      FORMAT [Tab,F,DEM] = DEM_FIN(SIM)  
         
        Demonstration of financial modelling using variational Laplace  
       __________________________________________________________________________  
        This demonstration routine illustrates the complex system modelling of  
        financial markets using a generic (Helmholtz Hodge) generative model of  
        stochastic chaos under the prior are there exists a pullback attractor.  
        This endows the dynamics with a compact functional form; especially when  
        using second-order approximations (cf., A generalisation of the Laplace  
        approximation).  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_FIN.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_FIN", *args, **kwargs)
