from spm.__wrapper__ import Runtime


def ft_read_headmodel(*args, **kwargs):
    """
      FT_READ_HEADMODEL reads a head model (or volume conduction model of the head) from  
        various manufacturer specific files. Currently supported are ASA, CTF, Neuromag,  
        MBFYS, MATLAB and SimNIBS. The volume conduction model is represented as a  
        structure with fields that depend on the type of model.  
         
        Use as  
          headmodel = ft_read_headmodel(filename, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          'fileformat' = string  
         
        If the fileformat is 'simnibs', an additional options can be used to specify the  
        type of model that is to be returned.  
          'meshtype'   = string, 'volume' or 'surface' (default is automatic)  
         
        See also FT_DATATYPE_HEADMODEL, FT_PREPARE_HEADMODEL, FT_READ_HEADMODEL,  
        FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_headmodel", *args, **kwargs)
