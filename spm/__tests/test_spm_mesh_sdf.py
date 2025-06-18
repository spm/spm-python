from mpython import Runtime


def test_spm_mesh_sdf(*args, **kwargs):
    """
      Unit Tests for spm_mesh_sdf
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_mesh_sdf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_mesh_sdf", *args, **kwargs)
