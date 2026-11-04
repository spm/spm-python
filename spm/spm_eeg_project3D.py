from spm._runtime import Runtime


def spm_eeg_project3D(*args, **kwargs):
    r"""
      Wrapper function to a fieldtrip function to project 3D locations   
        onto a 2D plane.   
        FORMAT [xy,label] = spm_eeg_project3D(sens, modality)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_project3D.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_project3D", *args, **kwargs)
