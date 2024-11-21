from spm.__wrapper__ import Runtime


def _ft_inv(*args, **kwargs):
    """
      FT_INV computes a matrix inverse with optional regularization.  
         
        Use as  
         Y = ft_inv(X, ...)  
         
        Additional options should be specified in key-value pairs and can be  
          method    = string, method for inversion and regularization (see below).  
                      The default method is 'lavrentiev'.  
          lambda    = scalar value, or string (expressed as a percentage), specifying   
                      the regularization parameter for Lavrentiev or Tikhonov   
                      regularization, or the replacement value for winsorization.   
                      When lambda is specified as a string containing a percentage,   
                      e.g. '5%', it will be computed as the percentage of the average   
                      eigenvalue.  
          kappa     = scalar integer, reflects the ordinal singular value at which  
                      the singular value spectrum will be truncated.  
          tolerance = scalar, reflects the fraction of the largest singular value  
                      at which the singular value spectrum will be truncated.  
                      The default is 10*eps*max(size(X)).  
          feedback  = boolean, to visualize the singular value spectrum with the   
                      lambda regularization and kappa truncation.  
         
        The supported methods are:  
         
        'vanilla' - the MATLAB inv() function is used for inversion, no regularization is  
        applied.  
         
        'moorepenrose' - the Moore-Penrose pseudoinverse is computed, no regularization is  
        applied.  
         
        'tsvd' - this results in a pseudoinverse based on a singular value decomposition,  
        truncating the singular values according to either kappa or tolerance parameter  
        before reassembling the inverse.  
         
        'tikhonov' - the matrix is regularized according to the Tikhonov method using the  
        labmda parameter, after which the truncated svd method (i.e. similar to MATLAB  
        pinv) is used for inversion.  
         
        'lavrentiev' - the matrix is regularized according to the Lavrentiev method with a  
        weighted identity matrix using the labmda parameter, after which the truncated svd  
        method (i.e. similar to MATLAB pinv) is used for inversion.  
         
        'winsorize' - a truncated svd is computed, based on either kappa or tolerance  
        parameters, but in addition the singular values smaller than lambda are replaced by  
        the value according to lambda.  
         
        Both for the lambda and the kappa option you can specify 'interactive' to pop up an  
        interactive display of the singular value spectrum that allows you to click in the figure.   
         
        Rather than specifying kappa, you can also specify the tolerance as the ratio of  
        the largest eigenvalue at which eigenvalues will be truncated.  
         
        See also INV, PINV, CONDEST, RANK  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ft_inv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_inv", *args, **kwargs)
