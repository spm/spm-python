from spm.__wrapper__ import Runtime


def _align_ctf2acpc(*args, **kwargs):
    """
      ALIGN_CTF2ACPC performs an approximate rigid body alignment of the anatomical  
        volume from CTF towards ACPC coordinates. Only the homogeneous transformation  
        matrix is modified and the coordsys-field is updated.  
         
        Use as  
          mri = align_ctf2acpc(mri)  
          mri = align_ctf2acpc(mri, method)  
          mri = align_ctf2acpc(mri, method, template)  
         
        The first input argument is a FieldTrip MRI-structure, and the second optional  
        argument specifies how the registration is to be done:  
          method = 0: only an approximate coregistration  
          method = 1: an approximate coregistration, followed by spm_affreg  
          method = 2: an approximate coregistration, followed by spm_normalise (default)  
         
        When method = 1 or 2, an optional template filename can be specified, which denotes  
        the filename of the target volume. This is required when running in deployed  
        mode.  
         
        See also ALIGN_NEUROMAG2ACPC, ALIGN_FSAVERAGE2MNI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/align_ctf2acpc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("align_ctf2acpc", *args, **kwargs)
