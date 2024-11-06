from spm.__wrapper__ import Runtime


def tbx_cfg_fieldmap(*args, **kwargs):
    """
      MATLABBATCH Configuration file for toolbox 'FieldMap'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/FieldMap/tbx_cfg_fieldmap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tbx_cfg_fieldmap", *args, **kwargs)
