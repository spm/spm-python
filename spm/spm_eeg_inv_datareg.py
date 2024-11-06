from spm.__wrapper__ import Runtime


def spm_eeg_inv_datareg(*args, **kwargs):
    """
      Co-registration of two sets of fiducials according to sets of  
        corresponding points and (optionally) headshapes.  
        rigid co-registration  
                  1: fiducials based (3 landmarks: nasion, left ear, right ear)  
                  2: surface matching between sensor mesh and headshape  
                  (starts with a type 1 registration)  
         
        FORMAT M1 = spm_eeg_inv_datareg(S)  
         
        Input:  
         
        S  - input struct  
        fields of S:  
         
        S.sourcefid  - EEG fiducials (struct)  
        S.targetfid = MRI fiducials  
        S.template  - 1 - input is a template (for EEG)  
                      0 - input is an individual head model  
                      2 - input is a template (for MEG) - enforce uniform scaling  
         
        S.useheadshape - 1 use headshape matching 0 - don't  
         
         
        Output:  
        M1 = homogeneous transformation matrix  
         
        If a template is used, the sensor locations are transformed using an  
        affine (rigid body) mapping.  If headshape locations are supplied  
        this is generalised to a full twelve parameter affine mapping (n.b.  
        this might not be appropriate for MEG data).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_datareg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_datareg", *args, **kwargs)
