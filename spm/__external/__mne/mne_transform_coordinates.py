from spm.__wrapper__ import Runtime


def mne_transform_coordinates(*args, **kwargs):
    """
       
        [trans_pos] = mne_transform_coordinates(filename,pos,from,to)  
         
        Transform locations between various MRI-related coordinate frames  
         
        filename   - Name of a fif file containing the coordinate transformations  
                     This file can be conveniently created with mne_collect_transforms  
        pos        - N x 3 array of locations to transform (in meters)  
        from       - Coordinate frame of the above locations  
                     Allowed choices are: FIFFV_COORD_MRI (surface RAS coordinates)  
                     and FIFFV_COORD_HEAD (MEG head coordinates)  
        to         - Coordinate frame of the result  
                     Allowed choices are: FIFFV_COORD_MRI, FIFFV_COORD_HEAD,  
                     FIFFV_MNE_COORD_MNI_TAL (MNI Talairach), and  
                     FIFFV_MNE_COORD_FS_TAL (FreeSurfer Talairach)  
         
                     All of the above constants are define in fiff_define_constants  
         
        trans_pos  - The transformed locations  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_transform_coordinates.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_transform_coordinates", *args, **kwargs)
