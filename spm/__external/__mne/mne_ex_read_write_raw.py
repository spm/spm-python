from spm._runtime import Runtime


def mne_ex_read_write_raw(*args, **kwargs):
    r"""
       
        function mne_ex_read_write_raw(infile,outfile);  
         
        Read and write raw data in 60-sec blocks  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_ex_read_write_raw.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_ex_read_write_raw", *args, **kwargs, nargout=0)
