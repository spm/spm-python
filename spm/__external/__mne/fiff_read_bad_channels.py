from spm.__wrapper__ import Runtime


def fiff_read_bad_channels(*args, **kwargs):
    """
       
        [bads] = fiff_read_bad_channels(fid,node[,ch_rename])  
         
        Reas the bad channel list from a node if it exists  
         
        fid       - The file id  
        node      - The node of interes  
        ch_rename - Short-to-long channel name mapping  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_bad_channels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_bad_channels", *args, **kwargs)
