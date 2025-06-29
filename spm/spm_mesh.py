from spm._runtime import Runtime


def spm_mesh(*args, **kwargs):
    """
      Load mesh file(s) into memory as patch structure  
        FORMAT M = spm_mesh(meshfilename1,meshfilename2,...)  
         
        M        - patch structure array (.faces and .vertices)   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh", *args, **kwargs)
