from spm.__wrapper__ import Runtime


def _yokogawa2headmodel(*args, **kwargs):
    """
      YOKOGAWA2HEADMODEL converts a spherical volume conductor model that can  
        be present in the header of a datafile into a structure that can  
        be used by FieldTrip.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/yokogawa2headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("yokogawa2headmodel", *args, **kwargs)
