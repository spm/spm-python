from spm._runtime import Runtime


def spm_setmeshpaths(*args, **kwargs):
    r"""
     function D=spm_setmeshpaths(D,newpath,val)  
        update paths in spm mesh structure  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_setmeshpaths.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_setmeshpaths", *args, **kwargs)
