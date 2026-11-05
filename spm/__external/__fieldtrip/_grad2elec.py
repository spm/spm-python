from spm._runtime import Runtime


def _grad2elec(*args, **kwargs):
    r"""
      GRAD2ELEC converts a grad structure to an elec structure  
         
        See also OPTO2ELEC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/grad2elec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("grad2elec", *args, **kwargs)
