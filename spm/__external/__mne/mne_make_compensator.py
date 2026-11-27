from spm._runtime import Runtime


def mne_make_compensator(*args, **kwargs):
    r"""
       
        [comp] = mne_make_compensator(info,from,to,exclude_comp_chs)  
         
        info              - measurement info as returned by the fif reading routines  
        from              - compensation in the input data  
        to                - desired compensation in the output  
        exclude_comp_chs  - exclude compensation channels from the output (optional)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_make_compensator.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_make_compensator", *args, **kwargs)
