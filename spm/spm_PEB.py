from spm.__wrapper__ import Runtime


def spm_PEB(*args, **kwargs):
    """
      Parametric empirical Bayes (PEB) for hierarchical linear models  
        FORMAT [C,P,F] = spm_PEB(y,P,[hP],OPT))  
         
        y       - (n x 1)     response variable  
         
        MODEL SPECIFICATION  
         
        P{i}.X  - (n x m)     ith level design matrix i.e: constraints on <Eb{i - 1}>  
        P{i}.C  - {q}(n x n)  ith level constraints on Cov{e{i}} = Cov{b{i - 1}}  
         
        hP      - enforces positively constraints on the covariance hyperparameters  
                  by adopting a log-normal hyperprior, with precision hP  
        OPT     - suppress reporting  
          
         
        POSTERIOR OR CONDITIONAL ESTIMATES  
         
        C{i}.E  - (n x 1)     conditional expectation E{b{i - 1}|y}  
        C{i}.C  - (n x n)     conditional covariance  Cov{b{i - 1}|y} = Cov{e{i}|y}  
        C{i}.M  - (n x n)     ML estimate of Cov{b{i - 1}} = Cov{e{i}}  
        C{i}.h  - (q x 1)     ith level ReML  hyperparameters for covariance:  
                              Cov{e{i}} = P{i}.h(1)*P{i}.C{1} +  ...  
         
        LOG EVIDENCE  
         
        F       - [-ve] free energy F = log evidence = p(y|X,C)  
         
        If P{i}.C is not a cell the covariance at that level is assumed to be  
        known and Cov{e{i}} = P{i}.C (i.e. the hyperparameter is fixed at 1)  
         
        If P{n}.C is not a cell this is taken to indicate that a full Bayesian  
        estimate is required where P{n}.X is the prior expectation and P{n}.C is  
        the known prior covariance.  For consistency, with PEB, this is  
        implemented by setting b{n} = 1 through appropriate constraints at level  
        {n + 1}.  
         
        To implement non-hierarchical Bayes with priors on the parameters use a  
        two level model setting the second level design matrix to zeros.  
       __________________________________________________________________________  
         
        Returns the moments of the posterior p.d.f. of the parameters of a  
        hierarchical linear observation model under Gaussian assumptions  
         
                                   y = X{1}*b{1} + e{1}  
                                b{1} = X{2}*b{2} + e{2}  
                                        ...  
         
                            b{n - 1} = X{n}*b{n} + e{n}  
         
        e{n} ~ N{0,Ce{n}}  
         
        using Parametric Emprical Bayes (PEB)  
         
        Ref: Dempster A.P., Rubin D.B. and Tsutakawa R.K. (1981) Estimation in  
        covariance component models.  J. Am. Stat. Assoc. 76;341-353  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_PEB", *args, **kwargs)
