from spm._runtime import Runtime


def spm_COVID_plot(*args, **kwargs):
    r"""
      Graphics for coronavirus simulations  
        FORMAT spm_COVID_plot(Y,X,Z)  
        Y      - expected timeseries (i.e., new depths and cases)  
        X      - latent (marginal ensemble density) states  
        Z      - optional empirical data  
        u      - optional bed capacity threshold  
        U      - optional indices of outcomes  
         
        This auxiliary routine plots the trajectory of outcome variables  
        and underlying latent or hidden states, in the form of marginal densities  
        over the four factors that constitute the COVID model. if empirical data  
        are supplied, they will be superimposed.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_COVID_plot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_plot", *args, **kwargs, nargout=0)
