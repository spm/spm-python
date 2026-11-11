from spm._runtime import Runtime


def _dimnum(*args, **kwargs):
    r"""
      This function returns the number of the given dimension 'dim' in the dimord string.  
         
        Syntax: [num,dims]=dimnum(dimord, dim)  
         
        e.g. when dimord='rpt_chancmb_freq_time' and dim='time', dimnum returns num=4  
              and dims contains {'rpt','chancmb','freq','tim'}.  
        e.g. when dimord='rpt_chancmb_freq_time' and dim='chancmb', dimnum returns num=2  
              and dims again contains {'rpt','chancmb','freq','tim'}.  
          
        For the known dimension types dim can also be 'time' or 'frequency'.  
        The known types are:  
        tim: 'time'  
        freq: 'frq', 'frequency'  
        chancmb: 'sgncmb', 'channel', 'signal combination', 'channels'  
        rpt: 'trial','trials'  
         
        When dim is not found in dimord, an empty matrix is returned, but  
        dims then still contains all dims in dimord.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/dimnum.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dimnum", *args, **kwargs)
