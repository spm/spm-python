from spm._runtime import Runtime


def mne_patch_info(*args, **kwargs):
    r"""
       
        [pinfo] = mne_patch_info(nearest)  
         
        Generate the patch information from the 'nearest' vector in a source space  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_patch_info.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_patch_info", *args, **kwargs)
