from spm.__wrapper__ import Runtime


def _dimnum(*args, **kwargs):
    """
      This function returns the number of the given dimention 'dim' in the dimord string.  
         
        Syntax: [num,dims]=dimnum(dimord, dim)  
         
        e.g. when dimord='rpt_chancmb_freq_time' and dim='time', dimnum returns num=4  
              and dims contains {'rpt','chancmb','freq','tim'}.  
        e.g. when dimord='rpt_chancmb_freq_time' and dim='chancmb', dimnum returns num=2  
              and dims again contains {'rpt','chancmb','freq','tim'}.  
          
        For the known dimentiontypes dim can also be 'time' or 'frequency'.  
        The known types are:  
        tim: 'time'  
        freq: 'frq', 'frequency'  
        chancmb: 'sgncmb', 'channel', 'signal combination', 'channels'  
        rpt: 'trial','trials'  
         
        When dim is not found in dimord, an empty matrix is returned, but  
        dims then still contains all dims in dimord.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/dimnum.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dimnum", *args, **kwargs)
