from spm.__wrapper__ import Runtime


def _hasyokogawa(*args, **kwargs):
    """
      HASYOKOGAWA tests whether the data input toolbox for MEG systems by  
        Yokogawa (www.yokogawa.com, designed by KIT/EagleTechnology) is  
        installed. Only the newest version of the toolbox is accepted.  
         
        Use as  
          string  = hasyokogawa;  
        which returns a string describing the toolbox version, e.g. "12bitBeta3",  
        "16bitBeta3", or "16bitBeta6" for preliminary versions, or '1.5' for the  
        official Yokogawa MEG Reader Toolbox. An empty string is returned if the toolbox  
        is not installed. The string "unknown" is returned if it is installed but  
        the version is unknown.  
         
        Alternatively you can use it as  
          [boolean] = hasyokogawa(desired);  
        where desired is a string with the desired version.  
         
        See also READ_YOKOGAWA_HEADER, READ_YOKOGAWA_DATA, READ_YOKOGAWA_EVENT,  
        YOKOGAWA2GRAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/hasyokogawa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("hasyokogawa", *args, **kwargs)
