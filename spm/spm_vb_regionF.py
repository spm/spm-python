from spm.__wrapper__ import Runtime


def spm_vb_regionF(*args, **kwargs):
    """
      Get log model evidence over a region of data for a GLM  
        FORMAT [F] = spm_vb_regionF (Y,xY,SPM)  
         
        Y     Matrix of fMRI data (eg. from spm_summarise.m)  
        xY    Coordinates etc from region (eg. from spm_voi.m)  
        SPM   SPM data structure (this must be loaded in from an   
              SPM.mat file). If this field is not specified this function  
              will prompt you for the name of an SPM.mat file  
         
        F     Log model evidence (single number for whole region)  
         
        Importantly, the design matrix is normalised so that when you compare  
        models their regressors will be identically scaled.  
         
        Valid model comparisons also require that the DCT basis set used in high   
        pass filtering, as specified in SPM.xX.K.X0, is the same for all models   
        that are to be compared.  
          
        W. Penny, G. Flandin, and N. Trujillo-Barreto. (2007). Bayesian Model   
        Comparison of Spatially Regularised General Linear Models. Human   
        Brain Mapping, 28(4):275-293.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_regionF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_regionF", *args, **kwargs)
