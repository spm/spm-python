from spm.__wrapper__ import Runtime


def ft_average_sens(*args, **kwargs):
    """
      FT_AVERAGE_SENS computes average sensor array from a series of input  
        arrays. Corresponding average fiducials can also be computed (optional)  
         
        Use as  
          [asens, afid] = ft_average_sens(sens)  
        where sens is a 1xN structure array containing N sensor arrays  
         
        Additional options should be specified in key-value pairs and can be  
          'weights'    a vector of weights (will be normalized to sum==1)  
          'fiducials'  optional structure array of headshapes  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_PREPARE_VOL_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_average_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_average_sens", *args, **kwargs)
