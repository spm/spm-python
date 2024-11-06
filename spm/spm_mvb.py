from spm.__wrapper__ import Runtime


def spm_mvb(*args, **kwargs):
    """
      Bayesian optimisation of a multivariate linear model with a greedy search  
        FORMAT model = spm_mvb(X,Y,X0,U,V,nG,sG)  
         
        X      - contrast or target vector  
        Y      - date feature matrix  
        X0     - confounds  
        U      - patterns  
        V      - observation noise covariance  
        nG     - number of Greedy iterations (nG = 1 => uniform hyperpriors)  
               - if not specified, the search will terminate when F falls  
        sG     - size of successive subdivisions [default is 1/2)  
         
        returns model:  
                       F: log-evidence [F(0), F(1),...]  
                       G: covariance partition indices  
                       h: covariance hyperparameters  
                       U: ordered patterns  
                       M: MAP projector: qE = M*X  
                      qE: conditional expectation of voxel weights   
                      qC: conditional variance of voxel weights  
                      Cp: empirical prior covariance (ordered  pattern space)  
                      cp: empirical prior covariance (original pattern space)  
       __________________________________________________________________________  
         
        model: X = Y*P + X0*Q + R  
               P = U*E;             
          cov(E) = h1*diag(G(:,1)) + h2*diag(G(:,2)) + ...  
         
        This routine uses a multivariate Bayesian (MVB) scheme to decode or  
        recognise brain states from neuroimages. It resolves the ill-posed  
        many-to-one mapping, from voxel values or data features to a target  
        variable, using a parametric empirical or hierarchical Bayesian model.  
        This model is inverted using standard variational techniques, in this  
        case Variational Laplace, to furnish the model evidence and the  
        conditional density of the model's parameters. This allows one to compare  
        different models or hypotheses about the mapping from functional or  
        structural anatomy to perceptual and behavioural consequences (or their  
        deficits). The aim of MVB is not to predict (because the outcomes are  
        known) but to enable inference on different models of structure-function  
        mappings; such as distributed and sparse representations. This allows one  
        to optimise the model itself and produce predictions that outperform  
        standard pattern classification approaches, like support vector machines.  
        Technically, the model inversion and inference uses the same empirical  
        Bayesian procedures developed for ill-posed inverse problems (e.g.,  
        source reconstruction in EEG).  
         
        CAUTION: MVB should not be used to establish a significant mapping  
        between brain states and some classification or contrast vector. Its use  
        is limited to comparison of different models under the assumption  
        (hyperprior) that this mapping exists. To ensure the mapping exists, use  
        CVA or related approaches.  
         
        See spm_mvb_ui and:  
         
        Bayesian decoding of brain images.  
        Friston K, Chu C, Mourão-Miranda J, Hulme O, Rees G, Penny W, Ashburner J.  
        Neuroimage. 2008 Jan 1;39(1):181-205  
          
        Multiple sparse priors for the M/EEG inverse problem.  
        Friston K, Harrison L, Daunizeau J, Kiebel S, Phillips C, Trujillo-Barreto   
        N, Henson R, Flandin G, Mattout J.  
        Neuroimage. 2008 Feb 1;39(3):1104-20.  
          
        Characterizing dynamic brain responses with fMRI: a multivariate approach.  
        Friston KJ, Frith CD, Frackowiak RS, Turner R.  
        Neuroimage. 1995 Jun;2(2):166-72.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb", *args, **kwargs)
