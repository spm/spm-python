from spm.__wrapper__ import Runtime


def spm_mesh_resels(*args, **kwargs):
    """
      Return the RESEL counts of a search volume on a surface mesh  
        FORMAT R = spm_mesh_resels(M,T,[S])  
        M        - a patch structure or [nx3] faces array (#faces = n)  
        T        - a [mx1] logical vector (#vertices = m) defining search volume  
        S        - a [mxp] array of standardised residuals [optional]  
        ndf      - a 2-vector, [n df], the original n & dof of the linear model  
         
        R        - a [1xD] array of RESEL counts {adimensional}  
        RPV      - a [mx1] vector of RESELs per vertex  
       __________________________________________________________________________  
         
        References:  
         
        [1] Detecting Sparse Signals in Random Fields, With an Application to  
        Brain Imaging, J.E. Taylor and K.J. Worsley, Journal of the American  
        Statistical Association, 102(479):913-928, 2007.  
         
        [2] SurfStat: http://www.math.mcgill.ca/keith/surfstat/, K.J. Worsley.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_resels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_resels", *args, **kwargs)
