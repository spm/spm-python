from spm.__wrapper__ import Runtime


def spm_P(*args, **kwargs):
    """
      Return the [un]corrected P value using unified EC theory  
        FORMAT [P,p,Ec,Ek] = spm_P(c,k,Z,df,STAT,R,n,S)  
         
        c     - cluster number   
        k     - extent {RESELS}  
        Z     - height {minimum over n values}  
        df    - [df{interest} df{error}]  
        STAT  - Statistical field  
                'Z' - Gaussian field  
                'T' - T - field  
                'X' - Chi squared field  
                'F' - F - field  
                'P' - Posterior probability  
        R     - RESEL Count {defining search volume}  
        n     - number of component SPMs in conjunction  
        S     - Voxel count  
         
        P     - corrected   P value - P(C >= c | K >= k}  
        p     - uncorrected P value  
        Ec    - expected total number of clusters  
        Ek    - expected total number of resels per cluster  
         
       __________________________________________________________________________  
         
        spm_P determines corrected and uncorrected p values, using the minimum  
        of different valid methods.   
         
        See also: spm_P_RF, spm_P_Bonf  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P", *args, **kwargs)
