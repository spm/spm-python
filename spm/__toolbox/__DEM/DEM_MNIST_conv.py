from spm._runtime import Runtime


def DEM_MNIST_conv(*args, **kwargs):
    r"""
      Active sampling of MNIST digits  
       __________________________________________________________________________  
         
        This routine demonstrates smart or sparse sampling of outcomes to  
        accumulate evidence for posterior beliefs in an optimal way. Effectively,  
        it scores the expected free energy (i.e., expected information gain) of  
        different policies. Crucially, these policies reflect covert or internal  
        action; namely, subscribing to or querying different subsets of output  
        modalities. This can be regarded as one aspect of proactive message  
        passing; in the sense, it rests upon expected free energy to send  
        requests to nodes that evaluate outcome probabilities. The saving here is  
        in terms of compute time and message passing. Interestingly, this can  
        lead to characteristic overconfidence in classification. In other words,  
        by just sampling a limited subset of outcome modalities, the routine can  
        find a plausible explanation very quickly; however, not necessarily the  
        right explanation.  
          
        In addition, it illustrates active sampling under a simple form of weight  
        sharing implemented by introducing a state dependent mapping between  
        modalities and outcomes. This allows for inference over various  
        transformations between the modalities that are generated and the final  
        outcomes. In this demonstration, the transformations are restricted to X  
        and Y translations of an image. The range of (a fine) transformations can  
        be specified by editing the code below.  
         
        See also: spm_DCM_conv.m  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_MNIST_conv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_MNIST_conv", *args, **kwargs)
