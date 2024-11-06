from spm.__wrapper__ import Runtime


def _prepare_freq_matrices(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
        SUBFUNCTION that converts a freq structure into Cf, Cr and Pr  
        this is used in FT_SOURCEANALYSIS  
         
        This function returns data matrices with a channel order that is consistent  
        with the original channel order in the data.  
         
        The order of the channels in the output data is according to the input cfg.channel,  
        which therefore must be specified as a cell-array with actual labels, not as an  
        input like 'all' that still needs to be interpreted by FT_CHANNELSELECTION.  
         
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_freq_matrices.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_freq_matrices", *args, **kwargs)
