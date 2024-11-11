from spm.__wrapper__ import Runtime


def spm_DEM_R(*args, **kwargs):
    """
      Precision of the temporal derivatives of a Gaussian process  
        FORMAT [R,V] = spm_DEM_R(n,s,form)  
       __________________________________________________________________________  
        n    - truncation order  
        s    - temporal smoothness - s.d. of kernel {bins}  
        form - 'Gaussian', '1/f' [default: 'Gaussian']  
         
                                e[:] <- E*e(0)  
                                e(0) -> D*e[:]  
                        <e[:]*e[:]'> = R  
                                     = <E*e(0)*e(0)'*E'>  
                                     = E*V*E'  
         
        R    - (n x n)     E*V*E: precision of n derivatives  
        V    - (n x n)     V:    covariance of n derivatives  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_R.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_R", *args, **kwargs)
