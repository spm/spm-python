from spm._runtime import Runtime


def spm_clf(*args, **kwargs):
    r"""
      Clear specified figure of objects with visible handles  
        FORMAT spm_clf(F)  
        F - Figure number, or 'Tag' string of figure(s) to clear  
       __________________________________________________________________________  
         
        Clears the specified figure, deleting all objects with visible  
        handles ('HandleVisibility'=='on').  
         
        If the current window is 'Tag'ged interactive, then the figures name  
        is cleared and the pointer reset.  
         
        F Defaults to the current figure, if there is one.  
         
        This is just a gateway to spm_figure('Clear',F).  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_clf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_clf", *args, **kwargs, nargout=0)
