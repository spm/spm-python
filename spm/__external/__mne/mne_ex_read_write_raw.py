from spm.__wrapper__ import Runtime


def mne_ex_read_write_raw(*args, **kwargs):
    """
       
        function mne_ex_read_write_raw(infile,outfile);  
         
        Read and write raw data in 60-sec blocks  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_write_raw.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_ex_read_write_raw", *args, **kwargs, nargout=0)
