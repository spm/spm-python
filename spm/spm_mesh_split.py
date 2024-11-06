from spm.__wrapper__ import Runtime


def spm_mesh_split(*args, **kwargs):
    """
      Split a surface mesh into its connected components   
        FORMAT MS = spm_mesh_split(M, C)  
        M         - a [nx3] faces array or a patch structure  
        C         - a [nx1] vector containing labels for the connected components  
                    or a logical vector indicating vertices to keep  
         
        MS        - a patch structure array  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_split.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_split", *args, **kwargs)
