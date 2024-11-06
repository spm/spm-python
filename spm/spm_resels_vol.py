from spm.__wrapper__ import Runtime


def spm_resels_vol(*args, **kwargs):
    """
      Compute the number of resels in a volume - a compiled routine  
        FORMAT R = spm_resels_vol(V,W)  
        V      -  is a memory mapped image volume.  
                  Finite and non-zero values are considered to be part of  
                  the search volume.  
        W      -  smoothness of the component fields {FWHM in voxels}.  
        R      - Resel counts, where:  
                 R(1) - Euler Characteristic of the volume (number of connected  
                        components - number of holes).  
                 R(2) - Resel Diameter (average over all rotations of the  
                        distance between two parallel planes tangent to the  
                        volume in resel space).  
                 R(3) - Resel Surface Area (half the surface area of the  
                        volume in resel space).  
                 R(4) - Resel Volume (the volume in resel space).  
       _______________________________________________________________________  
         
        Reference : Worsley KJ et al 1996, Hum Brain Mapp. 4:58-73  
       _______________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_resels_vol.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_resels_vol", *args, **kwargs)
