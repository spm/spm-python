from spm.__wrapper__ import Runtime


def spm_immune_plot(*args, **kwargs):
    """
      Plotting for immune model  
        FORMAT y = spm_immune_plot(P,c,M,U)  
        P - Priors  
        c - covariance  
        U - inputs (timing of measurements)  
        Y - data  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_immune_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_immune_plot", *args, **kwargs)
