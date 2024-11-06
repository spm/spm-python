from spm.__wrapper__ import Runtime


def ft_chantype(*args, **kwargs):
    """
      FT_CHANTYPE determines for each individual channel what chantype of data it  
        represents, e.g. a planar gradiometer, axial gradiometer, magnetometer,  
        trigger channel, etc. If you want to know what the acquisition system is  
        (e.g. ctf151 or neuromag306), you should not use this function but  
        FT_SENSTYPE instead.  
         
        Use as  
          type = ft_chantype(hdr)  
          type = ft_chantype(sens)  
          type = ft_chantype(label)  
        or as  
          type = ft_chantype(hdr,   desired)  
          type = ft_chantype(sens,  desired)  
          type = ft_chantype(label, desired)  
         
        If the desired unit is not specified as second input argument, this  
        function returns a Nchan*1 cell-array with a string describing the type  
        of each channel.  
         
        If the desired unit is specified as second input argument, this function  
        returns a Nchan*1 boolean vector with "true" for the channels of the  
        desired type and "false" for the ones that do not match.  
         
        The specification of the channel types depends on the acquisition system,  
        for example the ctf275 system includes the following type of channels:  
        meggrad, refmag, refgrad, adc, trigger, eeg, headloc, headloc_gof.  
         
        See also FT_READ_HEADER, FT_SENSTYPE, FT_CHANUNIT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_chantype.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_chantype", *args, **kwargs)
