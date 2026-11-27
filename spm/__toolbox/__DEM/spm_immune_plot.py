from spm._runtime import Runtime


def spm_immune_plot(*args, **kwargs):
    r"""
      Plotting for immune model  
        FORMAT y = spm_immune_plot(P,c,M,U)  
        P - Priors  
        c - covariance  
        U - inputs (timing of measurements)  
        Y - data  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_immune_plot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_immune_plot", *args, **kwargs)
