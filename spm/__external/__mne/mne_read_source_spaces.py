from spm._runtime import Runtime


def mne_read_source_spaces(*args, **kwargs):
    r"""
       
        [src] = mne_read_source_spaces(source,add_geom,tree)  
         
        Reads source spaces from a fif file  
         
        source      - The name of the file or an open file id  
        add_geom    - Add geometry information to the source spaces  
        tree        - Required if source is an open file id, search for the  
                      source spaces here  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_source_spaces.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_source_spaces", *args, **kwargs)
