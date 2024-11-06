from spm.__wrapper__ import Runtime


def spm2fieldtrip(*args, **kwargs):
    """
      SPM2FIELDTRIP converts an SPM8 meeg object into a FieldTrip raw data structure  
         
        Use as  
          data = spm2fieldtrip(D)  
        where D is the SPM meeg object which you can load in with SPM_EEG_LOAD  
        and where data is a FieldTrip raw data structure as if it were returned  
        by FT_PREPROCESSING.  
         
        See also FT_PREPROCESSING, SPM_EEG_LOAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/spm2fieldtrip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm2fieldtrip", *args, **kwargs)
