from spm._runtime import Runtime


def spm_fs_fmri_csd(*args, **kwargs):
    """
      Spectral feature selection for a CSD DCM  
        FORMAT [y] = spm_fs_fmri_csd(y,M)  
        y      - CSD  
        M      - model structure  
       __________________________________________________________________________  
         
        This supplements cross spectral with cross covariance functions.  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fs_fmri_csd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fs_fmri_csd", *args, **kwargs)
