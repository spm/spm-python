from spm.__wrapper__ import Runtime


def pm_mask(*args, **kwargs):
    """
      Create a mask that will determine how far to proceed with phase unwrapping  
        FORMAT mask = pm_mask(angvar,mthrea,ndil)  
         
        Input:  
        angvar     : Map of variance of angle estimate.  
        mthres     : Threshold for variance beyond which  
                     phase unwrapping is considered too  
                     uncertain. Default value (pi^2)/6  
                     is half the variance of a U[-pi,pi]  
                     distribution.  
        ndil       : We can optionally specify a no. of  
                     erodes-dilates to apply to the mask  
                     in order to exclude areas connected  
                     only by thin bridges to the rest of  
                     the brain.  
         
        Output:  
        mask       : Well...  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/pm_mask.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("pm_mask", *args, **kwargs)
