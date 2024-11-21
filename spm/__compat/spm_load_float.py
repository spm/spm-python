from spm.__wrapper__ import Runtime


def spm_load_float(*args, **kwargs):
    """
      Load a volume into a floating point array  
        FORMAT dat = spm_load_float(V)  
        V   - handle from spm_vol  
        dat - a 3D floating point array  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_load_float.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_load_float", *args, **kwargs)
