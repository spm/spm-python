from spm.__wrapper__ import Runtime


def _MNestimator(*args, **kwargs):
    """
      function [Linv,W]=MNestimator(L,C,SNR2,trunc)  
        This function makes a basic minimum-morm pseudoinverse operator = MN estimator.  
        - L: the forward solution, lead-field matrix  
        - C: noise covariance matrix  
              This is used for combining different sensortypes, whitening the  
              data and setting the regularisation parameter. If C is empty, it is  
              assumed eye matrix --- that would be the basic Tikhonov 0  
              regularization for one sensortype.  
        - SNR2: the assumed ratio of variances of signal and noise, used for  
              setting the regularisation parameter.   
        - trunc: the number of (smallest) singular values of C that are set to   
              zero before making the whitener. For example, if the data / C has  
              been SSP-projected, "trunc" needs to be at least the number of  
              components projected away.  
         
        The whitening/regularization approach of this routine follows that used in  
        the MNE software,   
        http://martinos.org/mne/,   
        http://www.martinos.org/meg/manuals/MNE-manual-2.7.pdf  
        --- the influence of MNE software on this function is fully acknowledged!  
          
        Copyright (c) 2011--2013 Matti Stenroos (matti.stenroos@aalto.fi)  
         -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
                       !! There is no warranty of any kind !!  
        -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
        17 Oct 2013  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/MNestimator.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("MNestimator", *args, **kwargs)
