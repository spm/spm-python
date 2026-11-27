from spm._runtime import Runtime


def fiff_write_ctf_comp(*args, **kwargs):
    r"""
       
        fiff_write_ctf_comp(fid,comps,ch_rename)  
         
        Writes the CTF compensation data into a fif file  
         
            fid           An open fif file descriptor  
            comps         The compensation data to write  
            ch_rename     Short-to-long channel name mapping  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_ctf_comp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_ctf_comp", *args, **kwargs, nargout=0)
