from spm._runtime import Runtime


def spm_index(*args, **kwargs):
    r"""
      Multiple subscripts from linear index  
        FORMAT [ind] = spm_index(siz,ndx)  
        siz  - array size  
        ndx  - linear index  
         
        see: SUB2IND, FIND.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_index.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_index", *args, **kwargs)
