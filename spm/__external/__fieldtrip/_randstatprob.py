from spm.__wrapper__ import Runtime


def _randstatprob(*args, **kwargs):
    """
      RANDSTATPROB computes the non-parametric probability of the observed  
        value under the assumption that the random observations are equally  
        probable under the null hypothesis.  
         
        Use as  
          p = randstatprob(randobs, realobs, tail, correctm)  
        where  
          randobs  = Nvox x Nrnd  
          realobs  = Nvox x 1, or Nvox x Nobs (for multiple observations)  
          tail     =  0 for two-sided test  
          tail     =  1 for one-sided test with realobs>=randobs  
          tail     = -1 for one-sided test with realobs<=randobs  
          correctm =  0 do not correct for multiple comparisons  
                      1 correct for multiple comparisons using the maximum statistic  
                      2 correct for multiple comparisons using ordered statistics  
         
        Each row of the input data contains all the (real or randomized)  
        observations in one voxel. Multiple comparison can be performed by  
        creating a reference distribution based on the minimum or maximum  
        of all voxels for each randomization.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/randstatprob.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("randstatprob", *args, **kwargs)
