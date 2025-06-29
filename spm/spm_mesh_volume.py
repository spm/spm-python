from spm._runtime import Runtime


def spm_mesh_volume(*args, **kwargs):
    """
      Compute the volume of a closed surface mesh  
        FORMAT V = spm_mesh_volume(M)  
        M        - a patch structure  
          
        V        - volume  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_volume.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_volume", *args, **kwargs)
