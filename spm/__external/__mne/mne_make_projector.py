from spm._runtime import Runtime


def mne_make_projector(*args, **kwargs):
    r"""
       
        [proj,nproj,U] = mne_make_projector(projs,ch_names,bads)  
         
        proj     - The projection operator to apply to the data  
        nproj    - How many items in the projector  
        U        - The orthogonal basis of the projection vectors (optional)  
         
        Make an SSP operator  
         
        projs    - A set of projection vectors  
        ch_names - A cell array of channel names  
        bads     - Bad channels to exclude  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_make_projector.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_make_projector", *args, **kwargs)
