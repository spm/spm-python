from spm.__wrapper__ import Runtime


def spm_reml_ancova(*args, **kwargs):
    """
      Classical inference for [hierarchial] linear models using ReML  
        FORMAT [F,df,xX,xCon,beta,V] = spm_reml_ancova(y,P,Fc);  
         
        y       - (n x 1)     response variable  
        P{i}.X  - (n x m)     ith level design matrix i.e:  
        P{i}.C  - {q}(n x n)  ith level constraints on the form of Cov{e{i}}  
        Fc      - (m x q)     contrast matrix for the last level  
         
        F     -  T or F values  
        df    -  degrees of freedom  
        beta  -  parameter estimates  
        xX    -  design matrix structure  
        xCon  -  contrast structure  
       __________________________________________________________________________  
         
        spm_ancova uses a General Linear Model of the form:  
         
                                   y = X{1}*b{1} + e{1}  
                                b{1} = X{2}*b{2} + e{2}  
                                        ...  
         
                            b{n - 1} = X{n}*b{n} + e{n}  
         
        e{n} ~ N{0,Ce{n}}   
         
        An F ratio is formed using OLS estimators of the parameters and ReML   
        estimators of the hyperparamters.  
        If Fc has only one column a T statistic is returned,  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_reml_ancova.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_reml_ancova", *args, **kwargs)
