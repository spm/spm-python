from spm._runtime import Runtime


def _uidisplaytext(*args, **kwargs):
    r"""
      UIDISPLAYTEXT opens a figure for displaying multi-line text  
        in an "edit" user interface control element.  
         
        Use as  
          uidisplaytext(str, title)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/uidisplaytext.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("uidisplaytext", *args, **kwargs, nargout=0)
