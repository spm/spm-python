from spm._runtime import Runtime


def spm_csd_fmri_gu(*args, **kwargs):
    r"""
      Spectra of neuronal fluctuations and noise  
        FORMAT [Gu,Gn,Hz,dt] = spm_csd_fmri_gu(P,dt)  
         
        P  - model parameters  
        dt - sampling interval  
         
        This routine returns the spectra of neuronal fluctuations and noise for a  
        standard frequency range specified by the sampling interval.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_csd_fmri_gu.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_csd_fmri_gu", *args, **kwargs)
