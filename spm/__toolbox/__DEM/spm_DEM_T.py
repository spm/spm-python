from spm.__wrapper__ import Runtime


def spm_DEM_T(*args, **kwargs):
    """
      returns temporal delay operator  
        FORMAT [T] = spm_DEM_T(n,dt)  
       __________________________________________________________________________  
        n    - order of temporal embedding  
        dt   - time interval {time steps}  
         
        T    - (n x n)  for generalised state vectors x[t + dt] = T(dt)*x[t]  
         
        NB:  T(-dt) = inv(T(dt)), T(-dt)*T(dt) = I and T(i*dT) = T(dt)^i  
       ==========================================================================  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_DEM_T.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_T", *args, **kwargs)
