from spm.__wrapper__ import Runtime


def spm_convmtx(*args, **kwargs):
    """
      As for convmtx but with boundary conditions  
        FORMAT t = spm_convmtx(C,N,OPT)  
         
        OPT  - 'circular' boundary conditions  
             - 'square'   top and tail convolution matrix  
         
       --------------------------------------------------------------------------  
          CONVMTX(C,N) returns the convolution matrix for vector C.  
          If C is a column vector and X is a column vector of length N,  
          then CONVMTX(C,N)*X is the same as CONV(C,X).  
          If R is a row vector and X is a row vector of length N,  
          then X*CONVMTX(R,N) is the same as CONV(R,X).  
          See also CONV.%  
          With the circular option the convolution matrix is reduced to N X N  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_convmtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_convmtx", *args, **kwargs)
