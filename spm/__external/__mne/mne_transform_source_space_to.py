from spm.__wrapper__ import Runtime


def mne_transform_source_space_to(*args, **kwargs):
    """
       
        [res] = mne_transform_source_space_to(src,dest,trans)  
         
        Transform source space data to the desired coordinate system  
         
        src        - The source space to transform  
        dest       - The id of the destination coordinate system (FIFFV_COORD_...)  
        trans      - The coordinate transformation structure to use  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_transform_source_space_to.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_transform_source_space_to", *args, **kwargs)
