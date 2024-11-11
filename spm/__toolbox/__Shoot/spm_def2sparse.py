from spm.__wrapper__ import Runtime


def spm_def2sparse(*args, **kwargs):
    """
      Generate a sparse matrix encoding a deformation  
        [Phi,dim1,dim2] = spm_def2sparse(PY,PI)  
        PY - Filename of deformation field  
        PI - Filename of image defining field of view etc  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_def2sparse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_def2sparse", *args, **kwargs)
