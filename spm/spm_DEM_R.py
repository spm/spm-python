from spm._runtime import Runtime


def spm_DEM_R(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_R.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_R", *args, **kwargs)
