from spm._runtime import Runtime


def fiff_pick_info(*args, **kwargs):
    r"""
       
        [res] = fiff_pick_info(info,sel)  
         
        Pick desired channels from measurement info  
         
        res       - Info modified according to sel  
        info      - The original data  
        sel       - List of channels to select  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_pick_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_pick_info", *args, **kwargs)
