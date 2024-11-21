from spm.__wrapper__ import Runtime


def ft_struct2double(*args, **kwargs):
    """
      FT_STRUCT2DOUBLE converts all single precision numeric data in a structure  
        into double precision. It will also convert plain matrices and  
        cell-arrays.  
         
        Use as  
          x = ft_struct2double(x)  
         
        Starting from MATLAB 7.0, you can use single precision data in your  
        computations, i.e. you do not have to convert back to double precision.  
         
        MATLAB version 6.5 and older only support single precision for storing  
        data in memory or on disk, but do not allow computations on single  
        precision data. Therefore you should converted your data from single to  
        double precision after reading from file.  
         
        See also FT_STRUCT2SINGLE, FT_STRUCT2CHAR, FT_STRUCT2STRING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_struct2double.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_struct2double", *args, **kwargs)
