from spm._runtime import Runtime


def spm_mesh_volume(*args, **kwargs):
    r"""
      Compute the volume of a closed surface mesh  
        FORMAT V = spm_mesh_volume(M)  
        M        - a patch structure  
          
        V        - volume  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_mesh_volume.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mesh_volume", *args, **kwargs)
