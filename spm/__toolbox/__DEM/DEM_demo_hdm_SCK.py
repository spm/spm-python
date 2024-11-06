from spm.__wrapper__ import Runtime


def DEM_demo_hdm_SCK(*args, **kwargs):
    """
      Demo for Hemodynamic deconvolution: Cross-validation of Laplace scheme  
       __________________________________________________________________________  
        This demonstration compares generalised filtering and SCKS in the context   
        of a nonlinear convolution model using synthetic data. Here, we look at  
        estimating three of the hemodynamic parameters. This is a particularly  
        difficult (almost impossible) problem, given their distance from the data  
        and the conditional dependencies with the hidden states. Furthermore,   
        this is an unrealistic simulation, because we assume the data are almost   
        noiseless. The key thing to focus on is the comparative performance in  
        recovering the hidden states and causes.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_hdm_SCK.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_hdm_SCK", *args, **kwargs, nargout=0)
