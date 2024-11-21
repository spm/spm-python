from spm.__wrapper__ import Runtime


def spm_eeg_inv_checkmeshes(*args, **kwargs):
    """
      Display tesselated surfaces of cortex, skull and scalp  
        FORMAT [h_ctx,h_iskl,h_oskl,h_slp] = spm_eeg_inv_checkmeshes(S)  
        S      - input data struct (optional)  
         
        h_ctx  - handle to cortex patch  
        h_iskl - handle to inner skull patch  
        h_oskl - handle to outer skull patch  
        h_slp  - handle to scalp patch  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_checkmeshes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_checkmeshes", *args, **kwargs)
