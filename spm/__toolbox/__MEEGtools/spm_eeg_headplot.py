from spm._runtime import Runtime


def spm_eeg_headplot(*args, **kwargs):
    r"""
      SPM interface to headplot function from EEGLAB  
        FORMAT spm_eeg_headplot(Y, D, H)  
         
                Y - data vector  
                D - M/EEG object  
                H - (optional) axes handle  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_headplot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_headplot", *args, **kwargs, nargout=0)
