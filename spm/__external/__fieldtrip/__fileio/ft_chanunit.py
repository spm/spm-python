from spm.__wrapper__ import Runtime


def ft_chanunit(*args, **kwargs):
    """
      FT_CHANUNIT is a helper function that tries to determine the physical  
        units of each channel. In case the type of channel is not detected, it  
        will return 'unknown' for that channel.  
         
        Use as  
          unit = ft_chanunit(hdr)  
        or as  
          unit = ft_chanunit(hdr, desired)  
         
        If the desired unit is not specified as second input argument, this  
        function returns a Nchan*1 cell-array with a string describing the  
        physical units of each channel, or 'unknown' if those cannot be  
        determined.  
         
        If the desired unit is specified as second input argument, this function  
        returns a Nchan*1 boolean vector with "true" for the channels that match  
        the desired physical units and "false" for the ones that do not match.  
         
        The specification of the channel units depends on the acquisition system,  
        for example the neuromag306 system includes channel with the following  
        units: uV, T and T/cm.  
         
        See also FT_CHANTYPE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_chanunit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_chanunit", *args, **kwargs)
