from spm.__wrapper__ import Runtime


def spm_P_clusterFDR(*args, **kwargs):
    """
      Return the corrected FDR q-value  
        FORMAT [Q] = spm_P_clusterFDR(k,df,STAT,R,n,ui,Ps)  
          
        k        - extent {RESELS}  
        df       - [df{interest} df{residuals}]  
        STAT     - Statistical field  
                   'Z' - Gaussian field  
                   'T' - T - field  
                   'X' - Chi squared field  
                   'F' - F - field  
        R        - RESEL Count {defining search volume}  
        n        - Conjunction number  
        ui       - feature-inducing threshold  
        Ps       - Vector of sorted (ascending) p-values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P_clusterFDR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P_clusterFDR", *args, **kwargs)
