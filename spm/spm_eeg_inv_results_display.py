from spm.__wrapper__ import Runtime


def spm_eeg_inv_results_display(*args, **kwargs):
    """
      Displays contrast of evoked responses and power  
        FORMAT spm_eeg_inv_results_display(D)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_results_display.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_results_display", *args, **kwargs, nargout=0)
