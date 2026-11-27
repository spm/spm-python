from spm._runtime import Runtime


def spm_i2p(*args, **kwargs):
    r"""
      Converts an array of indices into a cell array of probabilities  
        FORMAT P = spm_i2p(X,s)  
        X   - (m,n) : 0 < X(i,j) < s  
        P   - {m,n} : P{i,j}(X(i,j),j) = 1  
          
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_i2p.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_i2p", *args, **kwargs)
