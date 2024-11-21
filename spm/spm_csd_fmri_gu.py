from spm.__wrapper__ import Runtime


def spm_csd_fmri_gu(*args, **kwargs):
    """
      Spectra of neuronal fluctuations and noise  
        FORMAT [Gu,Gn,Hz,dt] = spm_csd_fmri_gu(P,dt)  
         
        P  - model parameters  
        dt - sampling interval  
         
        This routine returns the spectra of neuronal fluctuations and noise for a  
        standard frequency range specified by the sampling interval.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_csd_fmri_gu.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_fmri_gu", *args, **kwargs)
