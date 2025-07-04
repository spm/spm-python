from spm._runtime import Runtime


def spm_mb_ui(*args, **kwargs):
    """
      VOI extraction of adjusted data and Markov Blanket decomposition  
        FORMAT [MB] = spm_mb_ui('specify',SPM)  
        FORMAT [MB] = spm_mb_ui('blocking',MB)  
        FORMAT [MB] = spm_mb_ui('results' ,MB)  
         
        SPM    - structure containing generic analysis details  
         
        MB.contrast -  contrast name  
        MB.name     -  MB name  
        MB.c        -  contrast weights  
        MB.X        -  contrast subspace  
        MB.Y        -  whitened and adjusted data  
        MB.X0       -  null space of contrast  
         
        MB.XYZ      -  locations of voxels (mm)  
        MB.xyz      -  seed voxel location (mm)  
        MB.VOX      -  dimension of voxels (mm)  
         
        MB.V        -  canonical vectors  (data)  
        MB.v        -  canonical variates (data)  
        MB.W        -  canonical vectors  (design)  
        MB.w        -  canonical variates (design)  
        MB.C        -  canonical contrast (design)  
         
        MB.chi      -  Chi-squared statistics testing D >= i  
        MB.df       -  d.f.  
        MB.p        -  p-values  
         
        also saved in MB_*.mat in the SPM working directory  
         
        FORMAT [MB] = spm_cva_ui('results',MB)  
        Display the results of a MB analysis  
       __________________________________________________________________________  
         
        This routine uses the notion of Markov blankets and the renormalisation  
        group to evaluate the coupling among neuronal systems at increasing  
        spatial scales. The underlying generative model is based upon the  
        renormalisation group: a working definition of renormalization involves  
        three elements: vectors of random variables, a course-graining operation  
        and a requirement that the operation does not change the functional form  
        of the Lagrangian. In our case, the random variables are neuronal states;  
        the course graining operation corresponds to the grouping (G) into a  
        particular partition and adiabatic reduction (R) - that leaves the  
        functional form of the dynamics unchanged.  
         
        Here, the grouping operator (G) is based upon coupling among states as  
        measured by the Jacobian. In brief, the sparsity structure of the  
        Jacobian is used to recursively identify Markov blankets around internal  
        states to create a partition of states - at any level - into particles;  
        where each particle comprises external and blanket states. The ensuing  
        reduction operator (R) eliminates the internal states and retains the slow  
        eigenmodes of the blanket states. These then constitute the (vector)  
        states at the next level and the process begins again.  
         
        This routine starts using a simple form of dynamic causal modelling  
        applied to the principal eigenvariate of local parcels (i.e., particles)  
        of voxels with compact support. The Jacobian is estimated using a  
        linearised dynamic causal (state space) model, where observations are  
        generated by applying a (e.g., haemodynamic) convolution operator to  
        hidden (e.g., neuronal) states. This estimation uses parametric empirical  
        Bayes (PEB: spm_PEB). The ensuing estimates of the Jacobian (i.e.,  
        effective connectivity) are reduced using Bayesian model reduction (BMR:  
        spm_dcm_BMR_all) within a bespoke routine (spm_dcm_J).  
         
        The Jacobian is then partitioned using the course graining operator into  
        particles or parcels (using spm_markov blanket). The resulting partition  
        is then reduced by eliminating internal states and retaining slow  
        eigenmodes with the largest (real) eigenvalues (spm_A_reduce). The  
        Jacobian of the reduced states is then used to repeat the process -  
        recording the locations of recursively coarse-grained particles - until  
        there is a single particle.  
         
        The result of this recursive decomposition (i.e., renormalisation)  
        affords a characterisation of directed coupling, as characterised by a  
        complex Jacobian; namely, a multivariate coupling matrix, describing the  
        coupling between eigenmodes of Markov blankets at successive scales. This  
        can be regarded as a recursive parcellation scheme based upon effective  
        connectivity and a generative (dynamic causal) model of multivariate  
        (neuronal) timeseries.  
         
        The following lists the various results options.  please see main body of  
        this script for a description of the (graphical) output  
          
        display the results in terms of particular partitions and eigenmodes  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'anatomy');  
          
        characterise connectivity at the smallest scale  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'distance');  
          
        characterise scaling behaviour in terms of scaling exponent  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'scaling');  
          
        characterise intrinsic coupling in terms of transfer functions  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'kernels');  
          
        display the results in terms of particular partitions and eigenmodes  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'dynamics');  
          
        characterise extrinsic coupling with a connectogram  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'connectogram');  
          
        characterise extrinsic coupling in terms of cross covariance functions  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'connectivity');  
          
        characterise intrinsic coupling in terms of dissipative flow  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'eigenmodes');  
          
        characterise eigenmodes in terms of design or inputs  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'responses');  
          
        input effects as active states at base level  
       --------------------------------------------------------------------------  
        spm_mb_ui('results',MB,'inputs');  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mb_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mb_ui", *args, **kwargs)
