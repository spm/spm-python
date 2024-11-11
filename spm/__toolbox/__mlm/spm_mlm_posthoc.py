from spm.__wrapper__ import Runtime


def spm_mlm_posthoc(*args, **kwargs):
    """
      Post-hoc model comparison of multivariate linear models  
        FORMAT [logbf] = spm_mlm_posthoc (mlm,c,a)  
         
        mlm          MLM data structure - see spm_mlm_bayes.m  
                     This contains eg. the [p x d] posterior mean regression    
                     coefficient matrix mlm.wmean.   
         
        c            [k x p*d] contrast matrix defining k-dimensional subspace  
        a            hypothesized value (zeros(k,1) by default)  
         
        The contrast matrix and hypothesized value define the reduced model.   
        The contrast is applied to the vectorised parameters w = vec(mlm.wmean)  
                      
        The Bayes Factor in favour of the alternative hypothesis over the null  
        is computed using a Savage-Dickey ratio (the probability of the  
        hypothesized value under the prior versus its probability under the  
        posterior)  
         
        bf = p(c*w=a|mlm)/p(c*w=a|Y,mlm)                
         
        logbf        Log Bayes Factor  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_mlm_posthoc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mlm_posthoc", *args, **kwargs)
