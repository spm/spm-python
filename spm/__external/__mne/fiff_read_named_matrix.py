from spm._runtime import Runtime


def fiff_read_named_matrix(*args, **kwargs):
    r"""
       
        [mat] = fiff_read_named_matrix(fid,node)  
         
        Read named matrix from the given node  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_named_matrix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_named_matrix", *args, **kwargs)
