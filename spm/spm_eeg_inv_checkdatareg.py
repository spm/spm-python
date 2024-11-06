from spm.__wrapper__ import Runtime


def spm_eeg_inv_checkdatareg(*args, **kwargs):
    """
      Display of the coregistred meshes and sensor locations in MRI space  
        FORMAT spm_eeg_inv_checkdatareg(D, val, ind)  
         
        Fiducials which were used for rigid registration are also displayed.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_checkdatareg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_checkdatareg", *args, **kwargs, nargout=0)
