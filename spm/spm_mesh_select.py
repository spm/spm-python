from spm.__wrapper__ import Runtime


def spm_mesh_select(*args, **kwargs):
    """
      Select vertices interactively on a triangle mesh  
        FORMAT P = spm_mesh_select(M,N)  
        M        - a mesh filename or GIfTI object or patch structure  
        N        - number of points to be interactively selected [default: 3]  
                   or cell array of char vectors containing label of points  
         
        P        - array of selected vertices coordinates [3xN]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_select.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_select", *args, **kwargs)
