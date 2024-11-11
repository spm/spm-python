from spm.__wrapper__ import Runtime


def mne_combine_xyz(*args, **kwargs):
    """
       
        function [comb] = mne_combine_xyz(vec)  
         
        Compute the three Cartesian components of a vector together  
         
         
        vec         - Input row or column vector [ x1 y1 z1 ... x_n y_n z_n ]  
        comb        - Output vector [x1^2+y1^2+z1^2 ... x_n^2+y_n^2+z_n^2 ]  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_combine_xyz.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_combine_xyz", *args, **kwargs)
