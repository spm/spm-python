from spm._runtime import Runtime


def spm_eeg_inv_results_display(*args, **kwargs):
    r"""
      Displays contrast of evoked responses and power  
        FORMAT spm_eeg_inv_results_display(D)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_results_display.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_results_display", *args, **kwargs, nargout=0)
