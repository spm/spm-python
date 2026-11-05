from spm._runtime import Runtime


def spm_normalise_disp(*args, **kwargs):
    r"""
      Display results of spatial normalisation  
        FORMAT spm_normalise_disp(matname)  
        matname - name of parameter file *_sn.mat  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldNorm/spm_normalise_disp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_normalise_disp", *args, **kwargs, nargout=0)
