from spm.__wrapper__ import Runtime


def spm_eeg_inv_extract(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_extract.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_extract", *args, **kwargs)
