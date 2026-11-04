from spm._runtime import Runtime


def ft_average_sens(*args, **kwargs):
    r"""
      FT_AVERAGE_SENS computes average sensor array from a series of input  
        arrays. Corresponding average fiducials can also be computed (optional)  
         
        Use as  
          [asens, afid] = ft_average_sens(sens)  
        where sens is a 1xN structure array containing N sensor arrays  
         
        Additional options should be specified in key-value pairs and can be  
          'weights'    a vector of weights (will be normalized to sum==1)  
          'fiducials'  optional structure array of headshapes  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_PREPARE_VOL_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_average_sens.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_average_sens", *args, **kwargs)
