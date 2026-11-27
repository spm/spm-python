from spm._runtime import Runtime


def fiff_read_bad_channels(*args, **kwargs):
    r"""
       
        [bads] = fiff_read_bad_channels(fid,node[,ch_rename])  
         
        Reas the bad channel list from a node if it exists  
         
        fid       - The file id  
        node      - The node of interes  
        ch_rename - Short-to-long channel name mapping  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_bad_channels.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_bad_channels", *args, **kwargs)
