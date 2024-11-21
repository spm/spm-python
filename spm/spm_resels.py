from spm.__wrapper__ import Runtime


def spm_resels(*args, **kwargs):
    """
      Return the RESEL counts of a search volume  
        FORMAT [R] = spm_resels(FWHM,L,SPACE)  
        FWHM       - smoothness of the component fields {FWHM - voxels}  
        L          - space definition            {in voxels}  
                       L = radius                {Sphere}  
                       L = [height width length] {Box}  
                       L = XYZ pointlist         {Discrete voxels}  
                       L = Mapped image volume   {Image}  
        SPACE      - Search space  
                      'S' - Sphere  
                      'B' - Box  
                      'V' - Discrete voxels  
                      'I' - Image VOI  
         
        R          - RESEL counts {adimensional}  
         
       __________________________________________________________________________  
         
        For one or two dimensional spaces the appropriate manifold is  
        used (e.g. sphere -> disc -> line).    
         
        Reference : Worsley KJ et al 1996, Hum Brain Mapp. 4:58-73  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_resels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_resels", *args, **kwargs)
