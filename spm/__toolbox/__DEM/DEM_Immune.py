from spm.__wrapper__ import Runtime


def DEM_Immune(*args, **kwargs):
    """
      This demo builds upon the results of the COVID modelling demos, which  
        found that the epidemic data could best be explained by appealing to the  
        idea that much of the population may not be susceptible and that of those  
        who are, some may be resistant and only experience a mild illness.  
        This means measures of immunity based upon antibody tests may  
        underestimate the effective herd immunity. This demo formalises several  
        alternative hypotheses as to the mechanisms of resistance. It  
        demonstrates the way in which the underlying model may be inverted to   
        test these hypotheses.   
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_Immune.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_Immune", *args, **kwargs)
