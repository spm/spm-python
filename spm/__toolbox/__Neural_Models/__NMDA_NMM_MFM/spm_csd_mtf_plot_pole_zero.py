from spm.__wrapper__ import Runtime


def spm_csd_mtf_plot_pole_zero(*args, **kwargs):
    """
      Spectral response of a NMM (transfer function x noise spectrum)  
        FORMAT [b,a] = spm_csd_mtf_plot_pole_zero(P,M,U,region_stab)  
         
        P - parameters  
        M - neural mass model structure  
        U - trial-specific effects  
        regions stab: which region in the DCM (per source list) to examine  
        stability  
         
        Returns poles and zeros and plots them   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/NMDA_NMM_MFM/spm_csd_mtf_plot_pole_zero.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_mtf_plot_pole_zero", *args, **kwargs)
