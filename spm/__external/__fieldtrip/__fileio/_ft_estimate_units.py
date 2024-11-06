from spm.__wrapper__ import Runtime


def _ft_estimate_units(*args, **kwargs):
    """
      FT_ESTIMATE_UNITS tries to determine the units of a geometrical object by  
        looking at its size and by relating this to the approximate size of the  
        human head according to the following table:  
          from  0.050 to   0.500 -> meter  
          from  0.500 to   5.000 -> decimeter  
          from  5.000 to  50.000 -> centimeter  
          from 50.000 to 500.000 -> millimeter  
         
        Use as  
          unit = ft_estimate_units(size)  
         
        This function will return one of the following strings  
          'm'  
          'cm'  
          'mm'  
         
        See also FT_CONVERT_UNITS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ft_estimate_units.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_estimate_units", *args, **kwargs)
