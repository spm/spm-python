from spm.__wrapper__ import Runtime


def tcdf(*args, **kwargs):
    """
      TCDF Student's T cumulative distribution function (cdf).  
         
        P = TCDF(X,V) computes the cdf for Student's T distribution  
        with V degrees of freedom, at the values in X. V must be a  
        scalar or have the same size as T.  
         
        P = TCDF(X,V,'upper') computes it for the upper tail instead  
        of the lower tail.  
         
        This is an alternative to the TCDF function that is implemented  
        in the Matlab statistics toolbox. This version originates from  
        http://www.statsci.org/matlab/statbox.html and originally was called TP.  
        It has been renamed to TCDF for drop-in compatibility with the Matlab  
        version.  
         
        Gordon Smyth, University of Queensland, gks@maths.uq.edu.au  
        3 Apr 97  
         
        NaN compatible - Markus Bauer and Eric Maris, FCDC  
        27 Jan 2005  
         
        fixed bug concerning NaN compatibility  
        21 Aug 2006, Markus Siegel  
         
        added support for upper tail, see http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=3045  
        13 Jan 2016, Robert Oostenveld  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/tcdf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tcdf", *args, **kwargs)
