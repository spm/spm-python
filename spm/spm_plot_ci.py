from spm.__wrapper__ import Runtime


def spm_plot_ci(*args, **kwargs):
    """
      Plot mean and conditional confidence intervals  
        FORMAT spm_plot_ci(E,C,x,j,s)  
        E - expectation (structure or array)  
        C - variance or covariance (structure or array)  
        x - domain  
        j - rows of E to plot  
        s - string to specify plot type:e.g. '--r' or 'exp', 'log' etc  
         
        -------------------------------------------------------------------------  
        The style of plot depends on the dimensions of the arguments provided:  
         
        1. Bar chart with n bars:  
           E:[n x 1], C:[n x 1] or [n x n]  
         
        2. Grouped bar chart with n bars in g groups:  
           E:[g x n], C:[g x n]  (transposed if 'exp' option is chosen)  
         
        3. Line chart with n lines, each with length g, where g >= 8:  
           E:[n x g], C:[n x g]  
         
        4. Elliptical confidence region:  
           E:[1 x 2], C:[1 x 2]  
         
        All errors bars or error regions denote 90% credible intervals.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_plot_ci.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_plot_ci", *args, **kwargs, nargout=0)
