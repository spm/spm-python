from spm._runtime import Runtime


def spm_def2sparse(*args, **kwargs):
    r"""
      Generate a sparse matrix encoding a deformation  
        [Phi,dim1,dim2] = spm_def2sparse(PY,PI)  
        PY - Filename of deformation field  
        PI - Filename of image defining field of view etc  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Shoot/spm_def2sparse.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_def2sparse", *args, **kwargs)
