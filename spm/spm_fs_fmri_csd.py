from spm._runtime import Runtime


def spm_fs_fmri_csd(*args, **kwargs):
    r"""
      Spectral feature selection for a CSD DCM  
        FORMAT [y] = spm_fs_fmri_csd(y,M)  
        y      - CSD  
        M      - model structure  
       __________________________________________________________________________  
         
        This supplements cross spectral with cross covariance functions.  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fs_fmri_csd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fs_fmri_csd", *args, **kwargs)
