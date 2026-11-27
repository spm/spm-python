from spm._runtime import Runtime


def spm_eeg_inv_checkmeshes(*args, **kwargs):
    r"""
      Display tesselated surfaces of cortex, skull and scalp  
        FORMAT [h_ctx,h_iskl,h_oskl,h_slp] = spm_eeg_inv_checkmeshes(S)  
        S      - input data struct (optional)  
         
        h_ctx  - handle to cortex patch  
        h_iskl - handle to inner skull patch  
        h_oskl - handle to outer skull patch  
        h_slp  - handle to scalp patch  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_checkmeshes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_checkmeshes", *args, **kwargs)
