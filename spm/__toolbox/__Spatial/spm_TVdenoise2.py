from spm._runtime import Runtime


def spm_TVdenoise2(*args, **kwargs):
    """
       
        FORMAT y = spm_TVdenoise2(x, lambda, nit, y)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_TVdenoise2", *args, **kwargs)
