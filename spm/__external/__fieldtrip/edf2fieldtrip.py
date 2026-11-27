from spm._runtime import Runtime


def edf2fieldtrip(*args, **kwargs):
    r"""
      EDF2FIELDTRIP reads data from a EDF file with channels that have a different  
        sampling rates. It upsamples all data to the highest sampling rate and  
        concatenates all channels into a raw data structure that is compatible with the  
        output of FT_PREPROCESSING.  
         
        Use as  
          data = edf2fieldtrip(filename)  
        or  
          [data, event] = edf2fieldtrip(filename)  
         
        For reading EDF files in which all channels have the same sampling rate, you can  
        use the standard procedure with FT_DEFINETRIAL and FT_PREPROCESSING.  
         
        See also FT_PREPROCESSING, FT_DEFINETRIAL, FT_REDEFINETRIAL,  
        FT_READ_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/edf2fieldtrip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("edf2fieldtrip", *args, **kwargs)
