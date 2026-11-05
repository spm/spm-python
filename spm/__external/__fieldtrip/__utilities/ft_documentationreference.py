from spm._runtime import Runtime


def ft_documentationreference(*args, **kwargs):
    r"""
      FT_DOCUMENTATIONREFERENCE is a helper function to maintain the  
        online reference documentation.  
         
        Normal users will not be calling this function, but will rather look at  
        http://www.fieldtriptoolbox.org/reference where the output of this function can  
        be found.  
         
        See also FT_DOCUMENTATIONCONFIGURATION, MATLAB2MARKDOWN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_documentationreference.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_documentationreference", *args, **kwargs, nargout=0)
