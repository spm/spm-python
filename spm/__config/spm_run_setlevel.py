from spm.__wrapper__ import Runtime


def spm_run_setlevel(*args, **kwargs):
    """
      out = spm_run_setlevel(job)  
        test to see how likely it is that an SPM statistical image is a random field.  
        based on:  
         Set-level threshold-free tests on the intrinsic volumes of SPMs.  
          Barnes GR, Ridgway GR, Flandin G, Woolrich M, Friston K. Neuroimage. 2013  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_setlevel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_setlevel", *args, **kwargs)
