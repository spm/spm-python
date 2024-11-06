from spm.__wrapper__ import Runtime


def _ft_fetch_sens(*args, **kwargs):
    """
      FT_FETCH_SENS mimics the behavior of FT_READ_SENS, but for a FieldTrip  
        data structure or a FieldTrip configuration instead of a file on disk.  
         
        Use as  
          [sens] = ft_fetch_sens(cfg)  
        or as  
          [sens] = ft_fetch_sens(cfg, data)  
         
        The sensor configuration can be passed into this function in four ways:  
         (1) in a configuration field  
         (2) in a file whose name is passed in a configuration field, see FT_READ_SENS  
         (3) in a layout file, see FT_PREPARE_LAYOUT  
         (4) in a data field  
         
        The following fields are used from the configuration:  
          cfg.elec     = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad     = structure with gradiometer definition or filename, see FT_READ_SENS  
          cfg.opto     = structure with optode definition or filename, see FT_READ_SENS  
          cfg.layout   = structure with layout definition or filename, see FT_PREPARE_LAYOUT  
          cfg.senstype = string, can be 'meg', 'eeg', or 'nirs', this is used to choose in combined data (default = 'eeg')  
         
        When the sensors are not specified in the configuration, this function will  
        fetch the grad, elec or opto field from the data.  
         
        See also FT_READ_SENS, FT_DATATYPE_SENS, FT_FETCH_DATA, FT_PREPARE_LAYOUT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ft_fetch_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_fetch_sens", *args, **kwargs)
