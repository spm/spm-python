from spm.__wrapper__ import Runtime


def ft_write_sens(*args, **kwargs):
    """
      FT_WRITE_SENS writes electrode information to an external file for further processing in external software.  
         
        Use as  
         ft_write_sens(filename, sens, ...)  
         
        The specified filename can already contain the filename extention,  
        but that is not required since it will be added automatically.  
         
        Additional options should be specified in key-value pairs and can be  
          'format'     string, see below  
         
        The supported file formats are  
          bioimage_mgrid  
          besa_sfp  
          polhemus_pos  
          matlab  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_WRITE_DATA, FT_WRITE_MRI, FT_WRITE_SENS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_write_sens", *args, **kwargs, nargout=0)
