from spm.__wrapper__ import Runtime


def spm_Pec_resels(*args, **kwargs):
    """
      Return the resel count for a point-list of voxels  
        FORMAT R = spm_Pec_resels(L,W)  
        L   - point list of voxels {in voxels}  
        W   - smoothness of the component fields {FWHM in voxels}  
        R   - vector of RESEL counts  
       ___________________________________________________________________________  
         
        Reference : Worsley KJ et al 1996, Hum Brain Mapp. 4:58-73  
       ___________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Pec_resels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Pec_resels", *args, **kwargs)
