from spm.__wrapper__ import Runtime


def mne_transpose_named_matrix(*args, **kwargs):
    """
       
        [res] = mne_transpose_named_matrix(mat)  
         
        Transpose a named matrix  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_transpose_named_matrix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_transpose_named_matrix", *args, **kwargs)
