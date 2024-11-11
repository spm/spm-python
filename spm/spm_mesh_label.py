from spm.__wrapper__ import Runtime


def spm_mesh_label(*args, **kwargs):
    """
      Label connected components of a surface mesh  
        FORMAT C = spm_mesh_label(M)  
        M        - a [nx3] faces array or a patch structure  
        opt      - return connected components on faces/vertices:  
                   {['faces'] ,'vertices'}  
         
        C        - a [nx1] vector containing labels for the connected components  
                   in M  
        N        - number of vertices per connected component  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_label.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_label", *args, **kwargs)
