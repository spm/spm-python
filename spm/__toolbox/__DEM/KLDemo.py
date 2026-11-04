from spm._runtime import Runtime


def KLDemo(*args, **kwargs):
    r"""
      Illustration of information gains with Bayesian fusion  
        FORMAT KLDemo)  
         
       --------------------------------------------------------------------------  
        This routine  illustrates the benefit of multimodal or Bayesian fusion in  
        terms of conditional dependencies among parameters. In other words, it  
        shows that even if one data modality contains no information about a  
        particular set of parameters, it can help resolve uncertainty about  
        another set and thereby disclose information contained in the other  
        modality. This is illustrated here using a simple linear model with  
        neuronal and haemodynamic parameters to show that EEG can provide some  
        information gain, in relation to haemodynamic parameters.  
          
        comment the orthogonalisation of the fMRI design matrix below to see the  
        effect of conditional dependencies on the haemodynamic information gain  
        afforded by EEG data  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/KLDemo.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("KLDemo", *args, **kwargs, nargout=0)
