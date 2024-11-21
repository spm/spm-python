from spm.__wrapper__ import Runtime


def _uidisplaytext(*args, **kwargs):
    """
      UIDISPLAYTEXT opens a figure for displaying multi-line text  
        in an "edit" user interface control element.  
         
        Use as  
          uidisplaytext(str, title)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/uidisplaytext.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("uidisplaytext", *args, **kwargs, nargout=0)
