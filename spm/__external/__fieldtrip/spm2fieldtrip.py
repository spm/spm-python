from spm._runtime import Runtime


def spm2fieldtrip(*args, **kwargs):
    r"""
      SPM2FIELDTRIP converts an SPM8 meeg object into a FieldTrip raw data structure  
         
        Use as  
          data = spm2fieldtrip(D)  
        where D is the SPM meeg object which you can load in with SPM_EEG_LOAD  
        and where data is a FieldTrip raw data structure as if it were returned  
        by FT_PREPROCESSING.  
         
        See also FT_PREPROCESSING, SPM_EEG_LOAD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/spm2fieldtrip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm2fieldtrip", *args, **kwargs)
