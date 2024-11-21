from spm.__wrapper__ import Runtime


def spm_padarray(*args, **kwargs):
    """
      FORMAT Y = spm_padarray(X, padsize, [method], [direction])  
        X         - numeric array  
        padsize   - padding size along each dimension of the array (>= 0)  
        method    - 'circular', 'replicate', 'symmetric' or a value [0]  
        direction - 'pre'/'post'/['both']  
         
        Note that:  
        * 'circular'  corresponds to the boundary condition of an FFT  
        * 'symmetric' corresponds to the boundary condition of a DCT-II  
         
        If padsize < 0, it is set to 0 instead.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_padarray.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_padarray", *args, **kwargs)
