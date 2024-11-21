from spm.__wrapper__ import Runtime


def spm_mvb_ui(*args, **kwargs):
    """
      Multivariate Bayes (Bayesian decoding of a contrast)  
        FORMAT [MVB] = spm_mvb_ui(xSPM,SPM,MVB)  
         
        Sets up, evaluates and saves an MVB structure:  
         
        MVB.contrast            % contrast structure  
        MVB.name                % name  
        MVB.c                   % contrast weight vector  
        MVB.M                   % MVB model (see below)  
        MVB.X                   % subspace of design matrix  
        MVB.Y                   % multivariate response  
        MVB.X0                  % null space of design  
        MVB.XYZ                 % location of voxels (mm)  
        MVB.V                   % serial correlation in response  
        MVB.K                   % whitening matrix  
        MVB.VOX                 % voxel scaling  
        MVB.xyzmm               % centre of VOI (mm)  
        MVB.Space               % VOI definition  
        MVB.Sp_info             % parameters of VOI  
        MVB.Ni                  % number of greedy search steps  
        MVB.sg                  % size of reedy search split  
        MVB.priors              % model (spatial prior)  
        MVB.fSPM                % SPM analysis (.mat file)  
         
        where MVB.M contains the following fields:  
         
                       F: log-evidence [F(0), F(1),...]  
                       G: covariance partition indices  
                       h: covariance hyperparameters  
                       U: ordered patterns  
                      qE: conditional expectation of voxel weights  
                      qC: conditional variance of voxel weights  
                      Cp: prior covariance (ordered  pattern space)  
                      cp: prior covariance (original pattern space)  
         
       --------------------------------------------------------------------------  
        This routine uses a multivariate Bayesian (MVB) scheme to decode or  
        recognise brain states from neuroimages. It resolves the ill-posed  
        many-to-one mapping, from voxel values or data features to a target  
        variable, using a parametric empirical or hierarchical Bayesian model.  
        This model is inverted using standard variational techniques, in this  
        case expectation maximisation, to furnish the model evidence and the  
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
        CVA or compute the randomisation p-value (see spm_mvb_p)  
         
        See: spm_mvb and  
         
        Bayesian decoding of brain images.  
        Friston K, Chu C, Mourao-Miranda J, Hulme O, Rees G, Penny W, Ashburner J.  
        Neuroimage. 2008 Jan 1;39(1):181-205  
          
        Multiple sparse priors for the M/EEG inverse problem.  
        Friston K, Harrison L, Daunizeau J, Kiebel S, Phillips C, Trujillo-Barreto   
        N, Henson R, Flandin G, Mattout J.  
        Neuroimage. 2008 Feb 1;39(3):1104-20.  
          
        Characterizing dynamic brain responses with fMRI: a multivariate approach.  
        Friston KJ, Frith CD, Frackowiak RS, Turner R.  
        Neuroimage. 1995 Jun;2(2):166-72.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mvb_ui", *args, **kwargs)
