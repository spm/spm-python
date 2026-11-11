from spm._runtime import Runtime


def mne_transpose_named_matrix(*args, **kwargs):
    r"""
       
        [res] = mne_transpose_named_matrix(mat)  
         
        Transpose a named matrix  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_transpose_named_matrix.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_transpose_named_matrix", *args, **kwargs)
