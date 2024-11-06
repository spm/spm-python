from spm.__wrapper__ import Runtime


def ft_trackusage(*args, **kwargs):
    """
      FT_TRACKUSAGE tracks the usage of specific FieldTrip components using a central  
        tracking server. This involves sending a small snippet of information to the  
        server. Tracking is only used to gather data on the usage of the FieldTrip  
        toolbox, to get information on the number of users and on the frequency of use  
        of specific toolbox functions. This allows the toolbox developers to improve the  
        FIeldTrip toolbox source code, documentation and to provide better support.  
         
        This function will NOT upload any information about the data, nor about the  
        configuration that you are using in your analyses.  
         
        This function will NOT upload any identifying details about you. Your username  
        and computer name are "salted" and subsequently converted with the MD5  
        cryptographic hashing function into a unique identifier. Not knowing the salt,  
        it is impossible to decode these MD5 hashes and recover the original  
        identifiers.  
         
        It is possible to disable the tracking for all functions by specifying  
        the following  
          global ft_defaults  
          ft_default.trackusage = 'no'  
         
        See the following online documentation for more information  
          http://en.wikipedia.org/wiki/MD5  
          http://en.wikipedia.org/wiki/Salt_(cryptography)  
          http://www.fieldtriptoolbox.org/faq/tracking  
         
        See also FT_DEFAULTS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_trackusage.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_trackusage", *args, **kwargs, nargout=0)
