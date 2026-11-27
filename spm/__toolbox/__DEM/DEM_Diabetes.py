from spm._runtime import Runtime


def DEM_Diabetes(*args, **kwargs):
    r"""
      dynamic causal model of Indian-type diabetes  
       __________________________________________________________________________  
          
        This demonstration routine illustrates a dynamic causal model of  
        Indian-type diabetes, with a focus on genetic and epigenetic mechanisms.  
        Technically, it illustrates the use of population density dynamics  
        modelled with a Master Equation; namely, a probability transition matrix  
        that determines the probability of moving from one state to another.  
        Crucially, these states are discrete, assuming that a person sampled at  
        random is in one of a finite number of states. These states can be  
        factored into a number of relevant dimensions (e.g., age, genotype, et  
        cetera), creating a state space of cells in a high dimensional array. The  
        population dynamics are determined by the (sparse) probabilities of  
        moving from one cell to another cell, generally expressed as rate  
        constants (i.e., the inverse of the time a particular cell is occupied).  
        Equipped with the transition matrix one can then solve the master  
        equation over time where, some parameters can change in response to  
        exogenous causes. This provides the basis for a generative model that is  
        completed by a likelihood mapping from the probability distribution over  
        states to observations over time. Generally, these observations are  
        nonnegative prevalences that can be modelled with a Gaussian likelihood,  
        based upon a binomial approximation. In this example, the ensuing  
        generative model is inverted using variational Laplace: a generic  
        variational scheme that uses a gradient descent on variational free  
        energy under Gaussian assumptions about free parameters and  
        hyperparameters; namely, transition rates and the precision of random  
        sampling effects. Priors over the model parameters are specified in terms  
        of their means and variances.  
         
        This demo sets up the priors over parameters that are used to generate  
        timeseries to which appropriate noise is added. These synthetic data are  
        inverted to illustrate the recovery of the parameters from sparse data  
        that are sampled asynchronously; here, every few years over a century.  
         
        The generative model includes all the states that are necessary to  
        generate population demographics, clinical data and metrics of economic  
        or agricultural activity. In turn, fluctuations in the state of the  
        population are caused by discrete events (i.e., famines) that change the  
        transition from a food secure to an insecure state. The effects of food  
        insecurity are modelled through an epigenetic mechanism, in which  
        interactions between the environment (food security) and genetics (high  
        versus low genotypic risk) are mediated at the point of birth. This  
        mediation is modelled by a simple form of replicator dynamics, in which  
        the rate of moving from a gene pool to a particular phenotype (high,  
        typical or low BMI) depends on both the environment (food security) and  
        genotype. This replication rate can be regarded as reproductive fitness,  
        where having a low risk (i.e., normal) genotype reduces reproductive  
        fitness when, and only when food insecure. The replicator dynamics are  
        situated in transitions among age groups, from child to adults and then  
        old. Mortality entails moving to the gene pool that slowly equilibriates  
        over time. This means that replicator dynamics are mediated by  
        replication rates that themselves depend upon genetic-environment  
        interactions. The clinical phenotype inherits from the BMI phenotype, in  
        the sense that the probability of moving from healthy to diabetic is  
        increased for a low BMI phenotype (when at high genetic risk). This model  
        also features direct environment-phenotype interactions; for example,  
        food security determines the transitions between BMI phenotypes, with the  
        potential risk of obesity in food secure states. In addition, under food  
        insecurity, there is a probability of dying and moving to the pool state.  
        The transition rates among the age groups determine the number of people  
        in each group and the composition of phenotypes and genotypes that enter  
        the genetic pool.  
         
        Although a gross simplification, this model features the minimum number  
        of states necessary to model interactions between genotype, phenotype and  
        environment in a way that incorporates age-dependent effects at the  
        population level. With the probability of being in any particular  
        combination of such states, one can then generate population data that  
        are, in principle, measurable; thereby affording the opportunity to  
        estimate the underlying genetic and epigenetic contributions to disease  
        burden, where the genetic and epigenetic legacies are expressed within  
        and between generations, respectively.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_Diabetes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_Diabetes", *args, **kwargs)
