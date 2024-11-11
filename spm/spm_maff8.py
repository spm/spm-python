from spm.__wrapper__ import Runtime


def spm_maff8(*args, **kwargs):
    """
      Affine registration to MNI space using mutual information  
        FORMAT [M,ll,h] = spm_maff8(P,samp,fwhm,tpm,M0,regtyp)  
        P       - filename or structure handle of image  
        samp    - distance between sample points (mm).  Small values are  
                  better, but things run more slowly.  
        fwhm    - smoothness estimate for computing a fudge factor.  Estimate  
                  is a full width at half maximum of a Gaussian (in mm).   
        tpm     - data structure encoding a tissue probability map, generated  
                  via spm_load_priors8.m.  
        M0      - starting estimates for the affine transform (or [] to use  
                  default values).  
        regtype - regularisation type  
                  'mni'     - registration of European brains with MNI space  
                  'eastern' - registration of East Asian brains with MNI space  
                  'rigid'   - rigid(ish)-body registration  
                  'subj'    - inter-subject registration  
                  'none'    - no regularisation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_maff8.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_maff8", *args, **kwargs)
