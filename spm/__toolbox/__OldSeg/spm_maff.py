from spm.__wrapper__ import Runtime


def spm_maff(*args, **kwargs):
    """
      Affine registration to MNI space using mutual information  
        FORMAT M = spm_maff(P,samp,x,b0,MF,M,regtyp,ff)  
        P       - filename or structure handle of image  
        x       - cell array of {x1,x2,x3}, where x1 and x2 are  
                  co-ordinates (from ndgrid), and x3 is a list of  
                  slice numbers to use  
        b0      - a cell array of belonging probability images  
                  (see spm_load_priors.m).  
        MF      - voxel-to-world transform of belonging probability  
                  images  
        M       - starting estimates  
        regtype - regularisation type  
                  'mni'   - registration of European brains with MNI space  
                  'eastern' - registration of East Asian brains with MNI space  
                  'rigid' - rigid(ish)-body registration  
                  'subj'  - inter-subject registration  
                  'none'  - no regularisation  
        ff      - a fudge factor (derived from the one above)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldSeg/spm_maff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_maff", *args, **kwargs)
