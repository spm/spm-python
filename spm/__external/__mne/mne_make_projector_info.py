from spm._runtime import Runtime


def mne_make_projector_info(*args, **kwargs):
    r"""
       
        [proj,nproj] = mne_make_projector_info(info)  
         
        Make an SSP operator using the meas info  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_make_projector_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_make_projector_info", *args, **kwargs)
