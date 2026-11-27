from spm._runtime import Runtime


def spm_mesh(*args, **kwargs):
    r"""
      Load mesh file(s) into memory as patch structure  
        FORMAT M = spm_mesh(meshfilename1,meshfilename2,...)  
         
        M        - patch structure array (.faces and .vertices)   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh", *args, **kwargs)
