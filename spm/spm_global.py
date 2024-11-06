from spm.__wrapper__ import Runtime


def spm_global(*args, **kwargs):
    """
      Compute the global mean for a volume image - a compiled routine  
        FORMAT GX = spm_global(V)  
        V   - image handle structure  
        GX  - global mean  
       __________________________________________________________________________  
         
        spm_global returns the mean counts integrated over all the slices from  
        the volume.  
         
        The mean is estimated after discounting voxels outside the object using  
        a criteria of greater than > (global mean)/8.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_global.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_global", *args, **kwargs)
