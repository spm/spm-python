from spm.__wrapper__ import Runtime


def spm_mesh_get_lm(*args, **kwargs):
    """
      Identification of local maxima on a textured surface mesh  
        FORMAT L = spm_mesh_get_lm(M,T)  
        M        - a [nx3] faces array or a patch structure or a [nxn] adjacency  
                   matrix  
        T        - a [nx1] texture vector  
         
        L        - indices of vertices that are local maxima  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_get_lm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_get_lm", *args, **kwargs)
