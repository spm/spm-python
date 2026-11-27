from spm._runtime import Runtime


def spm_padarray(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_padarray.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_padarray", *args, **kwargs)
