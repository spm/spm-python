from spm.__wrapper__ import Runtime


def spm_P_RF(*args, **kwargs):
    """
      Return the [un]corrected P value using unifed EC theory  
        FORMAT [P,p,Ec,Ek] = spm_P_RF(c,k,z,df,STAT,R,n)  
         
        c     - cluster number   
        k     - extent {RESELS}  
        z     - height {minimum over n values}  
        df    - [df{interest} df{error}]  
        STAT  - Statistical field  
              'Z' - Gaussian field  
              'T' - T - field  
              'X' - Chi squared field  
              'F' - F - field  
        R     - RESEL Count {defining search volume}  
        n     - number of component SPMs in conjunction  
         
        P     - corrected   P value  - P(C >= c | K >= k}  
        p     - uncorrected P value  
        Ec    - expected number of clusters (maxima)  
        Ek    - expected number of resels per cluster  
         
       __________________________________________________________________________  
         
        spm_P_RF returns the probability of c or more clusters with more than  
        k resels in volume process of R RESELS thresholded at u.  All p values  
        can be considered special cases:  
         
        spm_P_RF(1,0,z,df,STAT,1,n) = uncorrected p value  
        spm_P_RF(1,0,z,df,STAT,R,n) = corrected p value {based on height z)  
        spm_P_RF(1,k,u,df,STAT,R,n) = corrected p value {based on extent k at u)  
        spm_P_RF(c,k,u,df,STAT,R,n) = corrected p value {based on number c at k and u)  
        spm_P_RF(c,0,u,df,STAT,R,n) = omnibus   p value {based on number c at u)  
         
        If n > 1 a conjunction probility over the n values of the statistic  
        is returned.  
       __________________________________________________________________________  
         
        References:  
          
        [1] Hasofer AM (1978) Upcrossings of random fields  
        Suppl Adv Appl Prob 10:14-21  
        [2] Friston KJ et al (1994) Assessing the Significance of Focal Activations  
        Using Their Spatial Extent  
        Human Brain Mapping 1:210-220  
        [3] Worsley KJ et al (1996) A Unified Statistical Approach for Determining  
        Significant Signals in Images of Cerebral Activation  
        Human Brain Mapping 4:58-73  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P_RF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P_RF", *args, **kwargs)
