from spm._runtime import Runtime


def mne_read_surfaces(*args, **kwargs):
    r"""
       
        [surfs] = mne_read_surfaces(surfname,read_curv,read_left,read_right,subject,subjects_dir,add_info)  
         
        Reads FreeSurfer surface files for both hemispheres  
        as well as curvatures if requested.  
         
        Adds the derived geometry information to the surfaces  
         
        surfname     - The name of the surface to read, e.g., 'pial'  
        read_curv    - read the curvatures as well  
        read_left    - read the left hemisphere (default true)  
        read_right   - read the right hemisphere (default true)  
        subject      - The name of the subject (defaults to SUBJECT environment  
                       variable)  
        subjects_dir - The name of the MRI data directory (defaults to  
                       SUBJECTS_DIR environment variable)  
        add_info     - Add auxilliary information to the surfaces  
                       (vertex normals, triangle centroids, triangle normals, triangle  
                       areas) (default true)  
         
        surfs          - Output structure containing the surfaces  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_surfaces.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_surfaces", *args, **kwargs)
