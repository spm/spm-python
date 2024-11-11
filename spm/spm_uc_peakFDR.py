from spm.__wrapper__ import Runtime


def spm_uc_peakFDR(*args, **kwargs):
    """
      Peak False Discovery critical height threshold  
        FORMAT [u, Ps] = spm_uc_peakFDR(q,df,STAT,R,n,Z,XYZ,ui[,G])  
         
        q     - prespecified upper bound on False Discovery Rate  
        df    - [df{interest} df{residuals}]  
        STAT  - statistical field  
                'Z' - Gaussian field  
                'T' - T - field  
                'X' - Chi squared field  
                'F' - F - field  
        R     - RESEL Count {defining search volume}  
        n     - conjunction number  
        Z     - height {minimum over n values}  
                or mapped statistic image(s)  
        XYZ   - locations [x y x]' {in voxels}  
                or vector of indices of elements within mask  
                or mapped mask image  
        ui    - feature-inducing threshold  
        G     - patch structure (for surface-based inference)  
         
        u     - critical height threshold  
        Ps    - sorted p-values  
       __________________________________________________________________________  
         
        References  
         
        J.R. Chumbley and K.J. Friston, "False discovery rate revisited: FDR and   
        topological inference using Gaussian random fields". NeuroImage,  
        44(1):62-70, 2009.  
         
        J.R. Chumbley, K.J. Worsley, G. Flandin and K.J. Friston, "Topological  
        FDR for NeuroImaging". NeuroImage, 49(4):3057-3064, 2010.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uc_peakFDR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uc_peakFDR", *args, **kwargs)
