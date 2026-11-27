from spm._runtime import Runtime


def _yokogawa2headmodel(*args, **kwargs):
    r"""
      YOKOGAWA2HEADMODEL converts a spherical volume conductor model that can  
        be present in the header of a datafile into a structure that can  
        be used by FieldTrip.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/yokogawa2headmodel.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("yokogawa2headmodel", *args, **kwargs)
