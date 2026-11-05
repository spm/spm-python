from spm._runtime import Runtime


def spm_browser(*args, **kwargs):
    r"""
      Display an HTML document in a web browser  
        FORMAT spm_browser(url,[format])  
         
        url    - string containing URL (e.g. 'http://...' or 'file://...')  
        format - data format {['html'],'md'}  
                 'md' option uses Markdown:  
                   https://www.wikipedia.org/wiki/Markdown  
                   http://showdownjs.com/  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_browser.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_browser", *args, **kwargs, nargout=0)
