from spm._runtime import Runtime


def spm_run_setlevel(*args, **kwargs):
    r"""
      out = spm_run_setlevel(job)  
        test to see how likely it is that an SPM statistical image is a random field.  
        based on:  
         Set-level threshold-free tests on the intrinsic volumes of SPMs.  
          Barnes GR, Ridgway GR, Flandin G, Woolrich M, Friston K. Neuroimage. 2013  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_setlevel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_setlevel", *args, **kwargs)
