from spm.__wrapper__ import Runtime


def mne_make_projector(*args, **kwargs):
    """
       
        [proj,nproj,U] = mne_make_projector(projs,ch_names,bads)  
         
        proj     - The projection operator to apply to the data  
        nproj    - How many items in the projector  
        U        - The orthogonal basis of the projection vectors (optional)  
         
        Make an SSP operator  
         
        projs    - A set of projection vectors  
        ch_names - A cell array of channel names  
        bads     - Bad channels to exclude  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_make_projector.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_make_projector", *args, **kwargs)
