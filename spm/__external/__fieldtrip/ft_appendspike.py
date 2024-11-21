from spm.__wrapper__ import Runtime


def ft_appendspike(*args, **kwargs):
    """
      FT_APPENDSPIKE combines continuous data (i.e. LFP) with point-process data  
        (i.e. spikes) into a single large dataset. For each spike channel an  
        additional continuos channel is inserted in the data that contains  
        zeros most of the time, and an occasional one at the samples at which a  
        spike occurred. The continuous and spike data are linked together using  
        the timestamps.  
         
        Use as  
          [spike] = ft_appendspike(cfg, spike1, spike2, spike3, ...)  
        where the input structures come from FT_READ_SPIKE, or as  
          [data]  = ft_appendspike(cfg, data, spike1, spike2, ...)  
        where the first data structure is the result of FT_PREPROCESSING  
        and the subsequent ones come from FT_READ_SPIKE.  
         
        See also FT_APPENDDATA, FT_PREPROCESSING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_appendspike.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_appendspike", *args, **kwargs)
