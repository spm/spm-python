from spm.__wrapper__ import Runtime


def _binomialprob(*args, **kwargs):
    """
      BINOMIALPROB computes the probability of observing a significant effect  
        in multiple tests. It allows you to test questions like "How likely  
        is it that there is a significant effect at this time-frequency point  
        for 8 out of 10 subjects, given that the probability of observing a  
        significant effect in a given subject is 5%"  
          
        Use as  
           [bprob] = binomialprob(prob, alpha)  
        where  
          prob   is a Nvoxel X Nsubject matrix with the single-subject probability  
          alpha  is the probability of observing a significant voxel  
         
        The function also has more advanced functionality, please read the code   
        if you are interested.  
         
        See also BINOPDF, BINOCDF  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/binomialprob.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("binomialprob", *args, **kwargs)
