from spm.__wrapper__ import Runtime


def spm_P_FDR(*args, **kwargs):
    """
      Return the corrected FDR P value  
         
        FORMAT [P] = spm_P_FDR(Z,df,STAT,n,Ps)  
         
        Z     - height (minimum of n statistics)  
        df    - [df{interest} df{error}]  
        STAT  - Statistical field  
              'Z' - Gaussian field  
              'T' - T - field  
              'X' - Chi squared field  
              'F' - F - field  
              'P' - P - value  
        n     - Conjunction number  
        Ps    - Vector of sorted (ascending) p-values in search volume  
         
        P     - corrected FDR P value  
         
         
        FORMAT [P] = spm_P_FDR(p)  
         
        p     - vector or array of all uncorrected P values, from which  
                non-finite values will be excluded (but zeros and ones are kept)  
         
        P     - corrected FDR P values (a vector or array of the same shape as p)  
         
       __________________________________________________________________________  
         
        The Benjamini & Hochberch (1995) False Discovery Rate (FDR) procedure  
        finds a threshold u such that the expected FDR is at most q.  spm_P_FDR  
        returns the smallest q such that Z>u.   
         
        Background  
         
        For a given threshold on a statistic image, the False Discovery Rate  
        is the proportion of suprathreshold voxels which are false positives.  
        Recall that the thresholding of each voxel consists of a hypothesis  
        test, where the null hypothesis is rejected if the statistic is larger  
        than threshold.  In this terminology, the FDR is the proportion of  
        rejected tests where the null hypothesis is actually true.  
         
        A FDR procedure produces a threshold that controls the expected FDR  
        at or below q.  The FDR adjusted p-value for a voxel is the smallest q  
        such that the voxel would be suprathreshold.  
         
        In comparison, a traditional multiple comparisons procedure  
        (e.g. Bonferroni or random field methods) controls Familywise Error  
        rate (FWER) at or below alpha.  FWER is the *chance* of one or more  
        false positives anywhere (whereas FDR is a *proportion* of false  
        positives).  A FWER adjusted p-value for a voxel is the smallest alpha  
        such that the voxel would be suprathreshold.   
         
        If there is truly no signal in the image anywhere, then a FDR  
        procedure controls FWER, just as Bonferroni and random field methods  
        do. (Precisely, controlling E(FDR) yields weak control of FWE).  If  
        there is some signal in the image, a FDR method should be more powerful  
        than a traditional method.  
         
        For careful definition of FDR-adjusted p-values (and distinction between  
        corrected and adjusted p-values) see Yekutieli & Benjamini (1999).  
         
         
        References  
         
        Benjamini & Hochberg (1995), "Controlling the False Discovery Rate: A  
        Practical and Powerful Approach to Multiple Testing". J Royal Stat Soc,  
        Ser B.  57:289-300.  
         
        Benjamini & Yekutieli (2001), "The Control of the false discovery rate  
        in multiple testing under dependency". Annals of Statistics,   
        29(4):1165-1188.  
         
        Yekutieli & Benjamini (1999). "Resampling-based false discovery rate  
        controlling multiple test procedures for correlated test  
        statistics".  J of Statistical Planning and Inference, 82:171-196.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P_FDR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P_FDR", *args, **kwargs)
