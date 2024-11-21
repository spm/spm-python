from spm.__wrapper__ import Runtime


def bf_wizard_write(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        write module, pick a few options, and it will default for unpopulated  
        fields  
         
        Currently supported output methods include:  
          - nifti (for volumetric data)  
          - gifti (for surface data)  
          - spmmeeg (for virtual electrodes)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_write.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_write", *args, **kwargs)
