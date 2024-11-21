from spm.__wrapper__ import Runtime


def spm_eeg_inv_rigidreg(*args, **kwargs):
    """
      Computes homogeneous transformation matrix based on two sets  
        of points from two coordinate systems  
         
        FORMAT [M1] = spm_eeg_inv_rigidreg(data1, data2)  
        Input:  
        data1      - locations of the first set of points corresponding to the  
                   3D surface to register onto   
        data2      - locations of the second set of points corresponding to the  
                   second 3D surface to be registered   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_rigidreg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_rigidreg", *args, **kwargs)
