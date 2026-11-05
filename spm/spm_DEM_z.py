from spm._runtime import Runtime


def spm_DEM_z(*args, **kwargs):
    r"""
      Create hierarchical innovations for generating data  
        FORMAT [z,w] = spm_DEM_z(M,N)  
        M    - model structure  
        N    - length of data sequence  
         
        z{i} - innovations for level i (N.B. z{end} corresponds to causes)  
        w{i} - innovations for level i (state noise)  
         
        If there is no fixed or hyper parameterized precision, then unit noise is  
        created. It is assumed that this will be later modulated by state  
        dependent terms, specified by M.ph and M.pg in spm_DEM_int  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_z.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_z", *args, **kwargs)
