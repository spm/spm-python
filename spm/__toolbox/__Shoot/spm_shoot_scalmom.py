from spm.__wrapper__ import Runtime


def spm_shoot_scalmom(*args, **kwargs):
    """
      Generate ``scalar momenta'' for use as features in pattern recognition  
        FORMAT out = spm_shoot_scalmom(job)  
         
        See:  
        Singh, Nikhil, P. Fletcher, J. Preston, Linh Ha, Richard King,  
        J. Marron, Michael Wiener, and Sarang Joshi. "Multivariate  
        statistical analysis of deformation momenta relating anatomical  
        shape to neuropsychological measures." Medical Image Computing  
        and Computer-Assisted Intervention-MICCAI 2010 (2010): 529-537.  
         
        Singh, Nikhil, Angela Wang, Preethi Sankaranarayanan, P. Fletcher,  
        and Sarang Joshi. "Genetic, Structural and Functional Imaging  
        Biomarkers for Early Detection of Conversion from MCI to AD."  
        Medical Image Computing and Computer-Assisted Intervention-MICCAI  
        2012 (2012): 132-140.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_scalmom.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_scalmom", *args, **kwargs)
