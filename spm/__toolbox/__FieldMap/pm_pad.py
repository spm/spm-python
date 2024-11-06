from spm.__wrapper__ import Runtime


def pm_pad(*args, **kwargs):
    """
      Pads a (partially) unwrapped phasemap such that the phase  
        at a non-unwrapped location is a weighted average of unwrapped  
        neighbouring phase-values.  
        FORMAT [pm,wmap] = pm_pad(pm,wmap,kernel)  
         
        Input:  
        pm     : 2 or 3D phasemap where some voxels have been unwrapped  
                 and some not.  
        wmap   : Wrap-map, where a non-zero value indicates corresponding  
                 phase-value in pm has been unwrapped.  
        kernel : kernel used to generate a weighted average of surrounding  
                 voxels.  
         
        Output:  
        pm     : Same as pm in, but where some previously unwrapped  
                 phase-values have now been replaced.  
        wmap   : Same as wmap in, but where values that was replaced  
                 by weighted average in pm have now been set.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_pad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_pad", *args, **kwargs)
