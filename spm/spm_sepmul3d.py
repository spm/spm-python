from spm.__wrapper__ import Runtime


def spm_sepmul3d(*args, **kwargs):
    """
      Compute t = kron(B3,kron(B2,B1))*T(:)  
         
        FORMAT t = spm_sepmul3d(B1,B2,B3,T)  
        B1 - x-dim basis functions [nx kx]  
        B2 - y-dim basis functions [ny ky]  
        B3 - z-dim basis functions [nz kz]  
        T  - parameters encoding of the field [kx ky kz]  
        t  - Reconstructed field [nx ny nz]  
         
        If T is a vector, then so is the output  
         
        Note that DCT basis functions are usually used,  
        but other forms are available.  For example,  
        sparse B-spline basis functions could be used.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sepmul3d.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sepmul3d", *args, **kwargs)
