from spm._runtime import Runtime


def mne_find_source_space_hemi(*args, **kwargs):
    r"""
       
        function mne_find_source_space_hemi(src)  
         
        Return the hemisphere id for a source space  
         
        src      - The source space to investigate  
        hemi     - Deduced hemisphere id  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_find_source_space_hemi.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_find_source_space_hemi", *args, **kwargs)
