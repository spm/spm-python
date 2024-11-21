from spm.__wrapper__ import Runtime


def _align_neuromag2acpc(*args, **kwargs):
    """
      ALIGN_NEUROMAG2ACPC performs an approximate alignment of the anatomical  
        volume from NEUROMAG towards ACPC coordinates. Only the homogenous transformation  
        matrix is modified and the coordsys-field is updated.  
         
        Use as  
          mri = align_neuromag2acpc(mri)  
          mri = align_neuromag2acpc(mri, method)  
          mri = align_neuromag2acpc(mri, method, template)  
         
        The first input argument is a FieldTrip MRI-structure, and the second optional  
        argument specifies how the registration is to be done:  
          method = 0: only an approximate coregistration  
          method = 1: an approximate coregistration, followed by spm_affreg  
          method = 2: an approximate coregistration, followed by spm_normalise (default)  
         
        When method = 1 or 2, an optional template filename can be specified, which denotes  
        the filename of the target volume. This is required when running in deployed  
        mode.  
         
        See also ALIGN_CTF2ACPC, ALIGN_FSAVERAGE2MNI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/align_neuromag2acpc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_neuromag2acpc", *args, **kwargs)
