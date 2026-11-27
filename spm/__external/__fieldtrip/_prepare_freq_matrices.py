from spm._runtime import Runtime


def _prepare_freq_matrices(*args, **kwargs):
    r"""
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
        SUBFUNCTION that converts a freq structure into Cf, Cr and Pr  
        this is used in FT_SOURCEANALYSIS  
         
        This function returns data matrices with a channel order that is consistent  
        with the original channel order in the data.  
         
        The order of the channels in the output data is according to the input cfg.channel,  
        which therefore must be specified as a cell-array with actual labels, not as an  
        input like 'all' that still needs to be interpreted by FT_CHANNELSELECTION.  
         
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/prepare_freq_matrices.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("prepare_freq_matrices", *args, **kwargs)
