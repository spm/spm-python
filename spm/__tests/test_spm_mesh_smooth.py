from spm._runtime import Runtime


def test_spm_mesh_smooth(*args, **kwargs):
    """
      Unit Tests for spm_mesh_smooth  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_mesh_smooth.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_mesh_smooth", *args, **kwargs)
