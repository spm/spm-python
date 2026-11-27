from spm._runtime import Runtime


def bf_wizard_write(*args, **kwargs):
    r"""
      A handy command-line based batch filler with some defaults for DAiSS  
        write module, pick a few options, and it will default for unpopulated  
        fields  
         
        Currently supported output methods include:  
          - nifti (for volumetric data)  
          - gifti (for surface data)  
          - spmmeeg (for virtual electrodes)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_wizard_write.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_wizard_write", *args, **kwargs)
