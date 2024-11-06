from spm.__wrapper__ import Runtime


def spm_MDP_DEM(*args, **kwargs):
    """
      auxiliary (link) function for mixed hierarchical (MDP/DEM) models  
        FORMAT DEM = spm_MDP_DEM(DEM,demi,O,o)  
         
        DEM      - DEM structure  
        demi     - mapping from discrete outcomes to hidden causes  
         demi.C  - cell array of true causes for each combination of outcomes  
                   the appropriate array is then placed in DEM.C  
         demi.U  - cell array of hidden causes for each combination of outcomes  
                   the Bayesian model average is placed in DEM.U  
        O{g}     - cell array of priors over discrete outcomes  
        o(g x 1) - vector of true outcomes  
         
        completes the following fields:  
          DEM.X{g} - posterior probability over g models and t times  
         
        This routine performs a Bayesian model comparison using (DEM) Bayesian  
        filtering and places the results in fields of the DEM structure; so that  
        MDP schemes can pick them up as likelihood terms in the next hierarchical  
        level. The outcomes of the (discrete) MDP scheme at the superordinate  
        level specify the hidden causes at the current level. These enter as  
        Bayesian model averages of the continuous causes. The resulting  
        posterior over hidden causes then furnishes the posterior over outcomes  
        using Bayesian model reduction, based on the free energy accumulated  
        (integrated) over time. This free energy is supplemented with the prior  
        over discrete outcomes; thereby constituting a posterior over outcomes.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_DEM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_DEM", *args, **kwargs)
