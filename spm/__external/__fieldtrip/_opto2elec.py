from spm._runtime import Runtime


def _opto2elec(*args, **kwargs):
    r"""
      OPTTO2ELEC converts an opto structure to an elec structure  
         
        See also GRAD2ELEC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/opto2elec.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("opto2elec", *args, **kwargs)
