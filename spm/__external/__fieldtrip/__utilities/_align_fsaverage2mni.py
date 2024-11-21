from spm.__wrapper__ import Runtime


def _align_fsaverage2mni(*args, **kwargs):
    """
      ALIGN_FSAVERAGE2MNI performs an affine alignment of the anatomical volume from  
        FSAVERAGE towards MNI coordinates. Only the homogeneous transformation matrix is  
        modified and the coordsys-field is updated.  
         
        Use as  
          mri = align_fsaverage2mni(mri)  
        where the first input argument is a FieldTrip MRI-structure.  
         
        with fsaverage we mean MNI305  
        with mni       we mean MNI152, i.e. the template used in SPM  
         
        See http://freesurfer.net/fswiki/CoordinateSystems  
         
        See also ALIGN_CTF2ACPC, ALIGN_NEUROMAG2ACPC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/align_fsaverage2mni.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_fsaverage2mni", *args, **kwargs)
