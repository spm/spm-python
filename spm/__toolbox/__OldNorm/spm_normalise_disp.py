from spm.__wrapper__ import Runtime


def spm_normalise_disp(*args, **kwargs):
    """
      Display results of spatial normalisation  
        FORMAT spm_normalise_disp(matname)  
        matname - name of parameter file *_sn.mat  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_normalise_disp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_normalise_disp", *args, **kwargs, nargout=0)
