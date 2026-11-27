from spm._runtime import Runtime


def spm_eeg_inv_extract(*args, **kwargs):
    r"""
      Exports source activity using the MAP projector  
        FORMAT [Ds] = spm_eeg_inv_extract(D)  
        Requires:  
         
            D.inv{i}.source.XYZ   - (n x 3) matrix of MNI coordinates  
         
        Optional:  
         
            D.inv{i}.source.rad   - radius (mm) of VOIs (default 5 mm)  
            D.inv{i}.source.label - label(s) for sources (cell array)  
            D.inv{i}.source.fname - output file name  
            D.inv{i}.source.type  - output type ('evoked'/'trials')  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_extract.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_extract", *args, **kwargs)
