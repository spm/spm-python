from spm.__wrapper__ import Runtime


def fiff_pick_info(*args, **kwargs):
    """
       
        [res] = fiff_pick_info(info,sel)  
         
        Pick desired channels from measurement info  
         
        res       - Info modified according to sel  
        info      - The original data  
        sel       - List of channels to select  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_pick_info.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_pick_info", *args, **kwargs)
