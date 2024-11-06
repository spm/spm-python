from spm.__wrapper__ import Runtime


def spm_t2z(*args, **kwargs):
    """
      Student's t to standard Normal (z-score) distribution  
        FORMAT [z,t1,z1] = spm_t2z(t,df,Tol)  
        t   - t values   
        df  - degrees of freedom  
        Tol - minimum tail probability for direct computation  
              Defaults to 10^(-16), a z of about 8.2  
        t1  - (absolute) t-value where linear extrapolation starts  
              empty if no extrapolation  
        z1  - Equivalent standard Normal ordinate to t-value t1  
       __________________________________________________________________________  
         
        spm_t2z implements a distributional transformation from the Student's  
        t to the unit Gaussian using incomplete Beta functions and the  
        inverse error function.  
         
        Returns z as deviates from the standard Normal (Gaussian)  
        distribution with lower tail probability equal to that of the  
        supplied t statistics with df degrees of freedom.  
         
        The standard normal distribution approximates Student's  
        t-distribution for large degrees of freedom. In univariate  
        situations, conventional wisdom states that 30 degrees of freedom is  
        sufficient for such an approximation. In the imaging context, the  
        multiple comparisons problem places emphasis on the extreme tails of  
        the distribution. For PET neuroimaging simulation suggests that 120  
        degrees of freedom are required before the distribution of the  
        maximal voxel value in a t-statistic image is adequately approximated  
        by that of the maxima of a gaussian statistic image (these  
        distributions usually being approximated using the theory of  
        continuous random fields)  (KJW - private communication). For fMRI  
        with it's higher resolution, it is likely that even greater degrees  
        of freedom are required for such an approximation.  
         
        *No* one-one approximation is made in this code for high df: This is  
        because the t2z accuracy reduces as t increases in absolute value  
        (particularly in the extrapolation region, underestimating the true  
        z. In this case imposing a one-one relationship for df>d say would  
        give a jump from df=d-1 to df=d.  
         
        For t deviates with very small tail probabilities (< Tol = 10^(-10),  
        corresponding to a z of about 6), the corresponding z is computed by  
        extrapolation of the t2z relationship z=f(t). This extrapolation  
        takes the form of z = log(t-t1+l0) + (z1-log(l0)). Here (t1,z1) is  
        the t & z ordinates with tail probability Tol. l0 is chosen such that  
        at the point where extrapolation takes over (t1,z1), continuity of  
        the first derivative is maintained. Thus, the gradient of the f(t) at  
        t1 is estimated as m using six points equally spaced to t1-0.5, and  
        l0 is then 1/m.  Experience suggests that this underestimates z,  
        especially for ludicrously high t and/or high df, giving conservative  
        (though still significant) results.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_t2z.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_t2z", *args, **kwargs)
