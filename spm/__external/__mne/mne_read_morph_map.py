from spm._runtime import Runtime


def mne_read_morph_map(*args, **kwargs):
    r"""
       
        [leftmap,rightmap] = mne_read_morph_map(from,to,subjects_dir)  
         
        Read the morphing map from subject 'from' to subject 'to'.  
        If subjects_dir is not specified, the SUBJECTS_DIR environment  
        variable is used  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_morph_map.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_morph_map", *args, **kwargs)
