from spm.__wrapper__ import Runtime


def spm_P_peakFDR(*args, **kwargs):
    """
      Return the corrected peak FDR q-value  
        FORMAT [Q] = spm_P_peakFDR(Z,df,STAT,R,n,ui,Ps)  
         
        Z        - height {minimum over n values}  
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
         
        Q        - FDR q-value  
       __________________________________________________________________________  
         
        References  
        J.R. Chumbley and K.J. Friston, "False discovery rate revisited: FDR and   
        topological inference using Gaussian random fields". NeuroImage,  
        44(1):62-70, 2009.  
         
        J.R. Chumbley, K.J. Worsley, G. Flandin and K.J. Friston, "Topological  
        FDR for NeuroImaging". NeuroImage, 49(4):3057-3064, 2010.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P_peakFDR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P_peakFDR", *args, **kwargs)
