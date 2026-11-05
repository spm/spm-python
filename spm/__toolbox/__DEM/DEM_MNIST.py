from spm._runtime import Runtime


def DEM_MNIST(*args, **kwargs):
    r"""
      Demo of structure learning (i.e.,disentanglement) of MNIST digits  
       __________________________________________________________________________  
         
        This routine provides a simple illustration of disentanglement or  
        structure learning using a static (image) recognition problem; namely the  
        MNIST digits. It casts the structure learning problem as a data  
        assimilation problem by accumulating latent states as discrete levels of  
        a factor in a hidden Markov model with two factors — the second factor  
        being the digit class. The key procedure demonstrated here is the  
        addition of a new latent (style) state using Bayesian model comparison  
        under the prior that additional states will increase expected free  
        energy. In the absence of any prior costs or constraints; this reduces to  
        accepting a new training exemplar if adding Dirichlet counts to a new  
        state (i.e., Column of the likelihood tensor) decreases variational and  
        expected free energy. In other words, increases the marginal likelihood  
        of the new observation under the prior constraint that the resulting  
        likelihood mapping has a greater mutual information.  
          
        In this example, an upper bound of 128 styles is implemented as an  
        additional hyperprior and the model is learned during exposure to 1024  
        training exemplars for each digit class. The ensuing classification  
        accuracy is established using a test dataset of 10,000. Performance is  
        between 95 and 100%; depending upon whether one accepts all the test data  
        or just those with a sufficiently high marginal likelihood (as scored by  
        the variational free energy).  
          
        The code below contains a number of subroutines and alternative  
        formulations of structure learning. It also examines the information  
        geometry inherent in the discovered structures. This routine can take  
        some time to ingest the training data (and will require downloading of a  
        MATLAB file as described in the preparation subroutine).  
          
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_MNIST.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_MNIST", *args, **kwargs)
