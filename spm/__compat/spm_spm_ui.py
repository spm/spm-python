from spm.__wrapper__ import Runtime


def spm_spm_ui(*args, **kwargs):
    """
      Setting up the general linear model for independent data  
        FORMATs (given in Programmers Help)  
       _______________________________________________________________________  
         
        spm_spm_ui.m configures the design matrix (describing the general  
        linear model), data specification, and other parameters necessary for  
        the statistical analysis. These parameters are saved in a  
        configuration file (SPM.mat) in the current directory, and are  
        passed on to spm_spm.m which estimates the design. Inference on these  
        estimated parameters is then handled by the SPM results section.  
         
        A separate program (spm_spm_fmri_ui.m) handles design configuration  
        for fMRI time series, though this program can be used for fMRI data  
        when observations can be regarded as independent.  
         
        ----------------------------------------------------------------------  
         
        Various data and parameters need to be supplied to specify the design:  
              * the image files  
              * indicators of the corresponding condition/subject/group  
              * any covariates, nuisance variables, or design matrix partitions  
              * the type of global normalisation (if any)  
              * grand mean scaling options  
              * thresholds and masks defining the image volume to analyse  
         
        The interface supports a comprehensive range of options for all these  
        parameters, which are described below in the order in which the  
        information is requested. Rather than ask for all these parameters,  
        spm_spm_ui.m uses a "Design Definition", a structure describing the  
        options and defaults appropriate for a particular analysis. Thus,  
        once the user has chosen a design, a subset of the following prompts  
        will be presented.  
         
        If the pre-specified design definitions don't quite have the combination  
        of options you want, you can pass a custom design structure D to be used  
        as parameter: spm_spm_ui('cfg',D). The format of the design structure  
        and option definitions are given in the programmers help, at the top of  
        the main body of the code.  
         
                                  ----------------  
         
        Design class & Design type  
        ==========================  
         
        Unless a design definition is passed to spm_spm_ui.m as a parameter,  
        the user is prompted first to select a design class, and then to  
        select a design type from that class.  
         
        The designs are split into three classes:  
          i) Basic stats: basic models for simple statistics  
             These specify designs suitable for simple voxel-by-voxel analyses.  
              - one-sample t-test  
              - two-sample t-test  
              - paired t-test  
              - one way Anova  
              - one way Anova (with constant)  
              - one way Anova (within subject)  
              - simple regression (equivalent to correlation)  
              - multiple regression  
              - multiple regression  (with constant)  
              - basic AnCova (ANalysis of COVAriance)  
                (essentially a two-sample t-test with a nuisance covariate)  
         
         ii) PET models: models suitable for analysis of PET/SPECT experiments  
              - Single-subject: conditions & covariates  
              - Single-subject: covariates only  
         
              - Multi-subj: conditions & covariates  
              - Multi-subj: cond x subj  interaction & covariates  
              - Multi-subj: covariates only  
              - Multi-group: conditions & covariates  
              - Multi-group: covariates only  
         
              - Population main effect: 2 cond's, 1 scan/cond (paired t-test)  
              - Dodgy population main effect: >2 cond's, 1 scan/cond  
              - Compare-populations: 1 scan/subject (two sample t-test)  
              - Compare-populations: 1 scan/subject (AnCova)  
         
              - The Full Monty... (asks you everything!)  
         
        iii) SPM96 PET models: models used in SPM96 for PET/SPECT  
             These models are provided for backward compatibility, but as they  
             don't include some of the advanced modelling features, we recommend  
             you switch to the new (SPM99) models at the earliest opportunity.  
              - SPM96:Single-subject: replicated conditions  
              - SPM96:Single-subject: replicated conditions & covariates  
              - SPM96:Single-subject: covariates only  
              - SPM96:Multi-subject: different conditions  
              - SPM96:Multi-subject: replicated conditions  
              - SPM96:Multi-subject: different conditions & covariates  
              - SPM96:Multi-subject: replicated conditions & covariates  
              - SPM96:Multi-subject: covariates only  
              - SPM96:Multi-group: different conditions  
              - SPM96:Multi-group: replicated conditions  
              - SPM96:Multi-group: different conditions & covariates  
              - SPM96:Multi-group: replicated conditions & covariates  
              - SPM96:Multi-group: covariates only  
              - SPM96:Compare-groups: 1 scan per subject  
         
         
        Random effects, generalisability, population inference...  
        =========================================================  
         
        Note that SPM only considers a single component of variance, the  
        residual error variance. When there are repeated measures, all  
        analyses with SPM are fixed effects analyses, and inference only  
        extends to the particular subjects under consideration (at the times  
        they were imaged).  
         
        In particular, the multi-subject and multi-group designs ignore the  
        variability in response from subject to subject. Since the  
        scan-to-scan (within-condition, within-subject variability is much  
        smaller than the between subject variance which is ignored), this can  
        lead to detection of group effects that are not representative of the  
        population(s) from which the subjects are drawn. This is particularly  
        serious for multi-group designs comparing two groups. If inference  
        regarding the population is required, a random effects analysis is  
        required.  
         
        However, random effects analyses can be effected by appropriately  
        summarising the data, thereby collapsing the model such that the  
        residual variance for the new model contains precisely the variance  
        components needed for a random effects analysis. In many cases, the  
        fixed effects models here can be used as the first stage in such a  
        two-stage procedure to produce appropriate summary data, which can  
        then be used as raw data for a second-level analysis. For instance,  
        the "Multi-subj: cond x subj  interaction & covariates" design can be  
        used to write out an image of the activation for each subject. A  
        simple t-test on these activation images then turns out to be  
        equivalent to a mixed-effects analysis with random subject and  
        subject by condition interaction effects, inferring for the  
        population based on this sample of subjects (strictly speaking the  
        design would have to be balanced, with equal numbers of scans per  
        condition per subject, and also only two conditions per subject). For  
        additional details, see spm_RandFX.man.  
         
                                  ----------------  
         
        Selecting image files & indicating conditions  
        =============================================  
         
        You may now be prompted to specify how many studies, subjects and  
        conditions you have, and then will be prompted to select the scans.  
         
        The data should all have the same orientation and image and voxel size.  
         
        File selection is handled by spm_select.m - the help for which describes  
        efficient use of the interface.  
         
        You may be asked to indicate the conditions for a set of scans, with  
        a prompt like "[12] Enter conditions? (2)". For this particular  
        example you need to indicate for 12 scans the corresponding  
        condition, in this case from 2 conditions. Enter a vector of  
        indicators, like '0 1 0 1...', or a string of indicators, like  
        '010101010101' or '121212121212', or 'rararararara'. (This  
        "conditions" input is handled by spm_input.m, where comprehensive  
        help can be found.)  
         
                                  ----------------  
         
        Covariate & nuisance variable entry  
        ===================================  
         
        * If applicable, you'll be asked to specify covariates and nuisance  
        variables. Unlike SPM94/5/6, where the design was partitioned into  
        effects of interest and nuisance effects for the computation of  
        adjusted data and the F-statistic (which was used to thresh out  
        voxels where there appeared to be no effects of interest), SPM99 does  
        not partition the design in this way. The only remaining distinction  
        between effects of interest (including covariates) and nuisance  
        effects is their location in the design matrix, which we have  
        retained for continuity.  Pre-specified design matrix partitions can  
        be entered. (The number of covariates / nuisance variables specified,  
        is actually the number of times you are prompted for entry, not the  
        number of resulting design matrix columns.) You will be given the  
        opportunity to name the covariate.  
          
        * Factor by covariate interactions: For covariate vectors, you may be  
        offered a choice of interaction options. (This was called "covariate  
        specific fits" in SPM95/6.) The full list of possible options is:  
              - <none>  
              - with replication  
              - with condition (across group)  
              - with subject (across group)  
              - with group  
              - with condition (within group)  
              - with subject (within group)  
         
        * Covariate centering: At this stage may also be offered "covariate  
        centering" options. The default is usually that appropriate for the  
        interaction chosen, and ensures that main effects of the interacting  
        factor aren't affected by the covariate. You are advised to choose  
        the default, unless you have other modelling considerations. The full  
        list of possible options is:  
              - around overall mean  
              - around replication means  
              - around condition means (across group)  
              - around subject means (across group)  
              - around group means  
              - around condition means (within group)  
              - around subject means (within group)  
              - <no centering>  
         
                                  ----------------  
         
        Global options  
        ==============  
         
        Depending on the design configuration, you may be offered a selection  
        of global normalisation and scaling options:  
         
        * Method of global flow calculation  
              - SPM96:Compare-groups: 1 scan per subject  
              - None (assuming no other options requiring the global value chosen)  
              - User defined (enter your own vector of global values)  
              - SPM standard: mean voxel value (within per image fullmean/8 mask)  
         
        * Grand mean scaling : Scaling of the overall grand mean simply  
        scales all the data by a common factor such that the mean of all the  
        global values is the value specified. For qualitative data, this puts  
        the data into an intuitively accessible scale without altering the  
        statistics. When proportional scaling global normalisation is used  
        (see below), each image is separately scaled such that it's global  
        value is that specified (in which case the grand mean is also  
        implicitly scaled to that value). When using AnCova or no global  
        normalisation, with data from different subjects or sessions, an  
        intermediate situation may be appropriate, and you may be given the  
        option to scale group, session or subject grand means separately. The  
        full list of possible options is:  
              - scaling of overall grand mean  
              - scaling of replication grand means  
              - scaling of condition grand means (across group)  
              - scaling of subject grand means (across group)  
              - scaling of group grand means  
              - scaling of condition (within group) grand means  
              - scaling of subject (within group) grand means  
              - implicit in PropSca global normalisation)  
              - no grand Mean scaling>'  
         
        * Global normalisation option : Global nuisance effects are usually  
        accounted for either by scaling the images so that they all have the  
        same global value (proportional scaling), or by including the global  
        covariate as a nuisance effect in the general linear model (AnCova).  
        Much has been written on which to use, and when. Basically, since  
        proportional scaling also scales the variance term, it is appropriate  
        for situations where the global measurement predominantly reflects  
        gain or sensitivity. Where variance is constant across the range of  
        global values, linear modelling in an AnCova approach has more  
        flexibility, since the model is not restricted to a simple  
        proportional regression.  
         
        Considering AnCova global normalisation, since subjects are unlikely  
        to have the same relationship between global and local measurements,  
        a subject-specific AnCova ("AnCova by subject"), fitting a different  
        slope and intercept for each subject, would be preferred to the  
        single common slope of a straight AnCova. (Assuming there's enough  
        scans per subject to estimate such an effect.) This is basically an  
        interaction of the global covariate with the subject factor. You may  
        be offered various AnCova options, corresponding to interactions with  
        various factors according to the design definition: The full list of  
        possible options is:  
              - AnCova  
              - AnCova by replication  
              - AnCova by condition (across group)  
              - AnCova by subject (across group)  
              - AnCova by group  
              - AnCova by condition (within group)  
              - AnCova by subject (within group)  
              - Proportional scaling  
              - <no global normalisation>  
         
        Since differences between subjects may be due to gain and sensitivity  
        effects, AnCova by subject could be combined with "grand mean scaling  
        by subject" to obtain a combination of between subject proportional  
        scaling and within subject AnCova.  
         
        * Global centering: Lastly, for some designs using AnCova, you will  
        be offered a choice of centering options for the global covariate. As  
        with covariate centering, this is only relevant if you have a  
        particular interest in the parameter estimates. Usually, the default  
        of a centering corresponding to the AnCova used is chosen. The full  
        list of possible options is:  
              - around overall mean  
              - around replication means  
              - around condition means (across group)  
              - around subject means (across group)  
              - around group means  
              - around condition means (within group)  
              - around subject means (within group)  
              - <no centering>  
              - around user specified value  
              - (as implied by AnCova)  
              - GM (The grand mean scaled value)  
              - (redundant: not doing AnCova)  
         
         
         
        Note that this is a logical ordering for the global options, which is  
        not the order used by the interface due to algorithm constraints. The  
        interface asks for the options in this order:  
              - Global normalisation  
              - Grand mean scaling options  
                (if not using proportional scaling global normalisation)  
              - Value for grand mean scaling  proportional scaling GloNorm  
                (if appropriate)  
              - Global centering options  
              - Value for global centering (if "user-defined" chosen)  
              - Method of calculation  
         
                                  ----------------  
         
        Masking options  
        ===============  
         
        The mask specifies the voxels within the image volume which are to be  
        assessed. SPM supports three methods of masking. The volume analysed  
        is the intersection of all masks:  
         
          i) Threshold masking : "Analysis threshold"  
              - images are thresholded at a given value and only voxels at  
                which all images exceed the threshold are included in the  
                analysis.  
              - The threshold can be absolute, or a proportion of the global  
                value (after scaling), or "-Inf" for no threshold masking.  
              - (This was called "Grey matter threshold" in SPM94/5/6)  
         
         ii) Implicit masking  
              - An "implicit mask" is a mask implied by a particular voxel  
                value. Voxels with this mask value are excluded from the  
                analysis.  
              - For image data-types with a representation of NaN  
                (see spm_type.m), NaN's is the implicit mask value, (and  
                NaN's are always masked out).  
              - For image data-types without a representation of NaN, zero is  
                the mask value, and the user can choose whether zero voxels  
                 should be masked out or not.  
         
        iii) Explicit masking  
              - Explicit masks are other images containing (implicit) masks  
                that are to be applied to the current analysis.  
              - All voxels with value NaN (for image data-types with a  
                representation of NaN), or zero (for other data types) are  
                excluded from the analysis.  
              - Explicit mask images can have any orientation and voxel/image  
                size. Nearest neighbour interpolation of a mask image is used if  
                the voxel centers of the input images do not coincide with that  
                of the mask image.  
         
         
                                  ----------------  
         
        Non-sphericity correction  
        =========================  
         
        In some instances the i.i.d. assumptions about the errors do not hold:  
         
        Identity assumption:  
        The identity assumption, of equal error variance (homoscedasticity), can  
        be violated if the levels of a factor do not have the same error variance.  
        For example, in a 2nd-level analysis of variance, one contrast may be scaled  
        differently from another.  Another example would be the comparison of  
        qualitatively different dependent variables (e.g. normals vs. patients).  If  
        You say no to identity assumptions, you will be asked whether the error  
        variance is the same over levels of each factor.  Different variances  
        (heteroscedasticy) induce different error covariance components that  
        are estimated using restricted maximum likelihood (see below).  
         
        Independence assumption.  
        In some situations, certain factors may contain random effects.  These induce  
        dependencies or covariance components in the error terms.   If you say no   
        to independence assumptions, you will be asked whether random effects  
        should be modelled for each factor.  A simple example of this would be  
        modelling the random effects of subject.  These cause correlations among the  
        error terms of observation from the same subject.  For simplicity, it is  
        assumed that the random effects of each factor are i.i.d.  One can always  
        re-specify the covariance components by hand in SPM.xVi.Vi for more  
        complicated models  
         
        ReML  
        The ensuing covariance components will be estimated using ReML in spm_spm  
        (assuming the same for all responsive voxels) and used to adjust the   
        statistics and degrees of freedom during inference. By default spm_spm  
        will use weighted least squares to produce Gauss-Markov or Maximum  
        likelihood estimators using the non-sphericity structure specified at this   
        stage. The components will be found in xX.xVi and enter the estimation   
        procedure exactly as the serial correlations in fMRI models.  
          
        see also: spm_reml.m and spm_non_sphericity.m  
          
                                  ----------------  
         
        Multivariate analyses  
        =====================  
         
        Mulitvariate analyses with n-variate response variables are supported  
        and automatically invoke a ManCova and CVA in spm_spm.  Multivariate  
        designs are, at the moment limited to Basic and PET designs.  
         
        ----------------------------------------------------------------------  
         
        Variables saved in the SPM structure  
         
        xY.VY         - nScan x 1 struct array of memory mapped images  
                        (see spm_vol for definition of the map structure)  
        xX            - structure describing design matrix  
        xX.D          - design definition structure  
                        (See definition in main body of spm_spm_ui.m)  
        xX.I          - nScan x 4 matrix of factor level indicators  
                        I(n,i) is the level of factor i corresponding to image n  
        xX.sF         - 1x4 cellstr containing the names of the four factors  
                        xX.sF{i} is the name of factor i  
        xX.X          - design matrix  
        xX.xVi        - correlation constraints for non-spericity correction  
        xX.iH         - vector of H partition (condition effects) indices,  
                        identifying columns of X corresponding to H  
        xX.iC         - vector of C partition (covariates of interest) indices  
        xX.iB         - vector of B partition (block effects) indices  
        xX.iG         - vector of G partition (nuisance variables) indices  
        xX.name     - p x 1 cellstr of effect names corresponding to columns  
                        of the design matrix  
          
        xC            - structure array of covariate details  
        xC(i).rc      - raw (as entered) i-th covariate  
        xC(i).rcname  - name of this covariate (string)  
        xC(i).c       - covariate as appears in design matrix (after any scaling,  
                        centering of interactions)  
        xC(i).cname   - cellstr containing names for effects corresponding to  
                        columns of xC(i).c  
        xC(i).iCC     - covariate centering option  
        xC(i).iCFI    - covariate by factor interaction option  
        xC(i).type    - covariate type: 1=interest, 2=nuisance, 3=global  
        xC(i).cols    - columns of design matrix corresponding to xC(i).c  
        xC(i).descrip - cellstr containing a description of the covariate  
          
        xGX           - structure describing global options and values  
        xGX.iGXcalc   - global calculation option used  
        xGX.sGXcalc   - string describing global calculation used  
        xGX.rg        - raw globals (before scaling and such like)  
        xGX.iGMsca    - grand mean scaling option  
        xGX.sGMsca    - string describing grand mean scaling  
        xGX.GM        - value for grand mean (/proportional) scaling  
        xGX.gSF       - global scaling factor (applied to xGX.rg)  
        xGX.iGC       - global covariate centering option  
        xGX.sGC       - string describing global covariate centering option  
        xGX.gc        - center for global covariate  
        xGX.iGloNorm  - Global normalisation option  
        xGX.sGloNorm  - string describing global normalisation option  
          
        xM            - structure describing masking options  
        xM.T          - Threshold masking value (-Inf=>None,  
                        real=>absolute, complex=>proportional (i.e. times global) )  
        xM.TH         - nScan x 1 vector of analysis thresholds, one per image  
        xM.I          - Implicit masking (0=>none, 1=>implicit zero/NaN mask)  
        xM.VM         - struct array of explicit mask images  
                        (empty if no explicit masks)  
        xM.xs         - structure describing masking options  
                        (format is same as for xsDes described below)  
          
        xsDes         - structure of strings describing the design:  
                        Fieldnames are essentially topic strings (use "_"'s for  
                        spaces), and the field values should be strings or cellstr's  
                        of information regarding that topic. spm_DesRep.m  
                        uses this structure to produce a printed description  
                        of the design, displaying the fieldnames (with "_"'s   
                        converted to spaces) in bold as topics, with  
                        the corresponding text to the right  
          
        SPMid         - String identifying SPM and program versions  
         
                                  ----------------  
         
        NB: The SPM.mat file is not very portable: It contains  
        memory-mapped handles for the images, which hardcodes the full file  
        pathname and datatype. Therefore, subsequent to creating the  
        SPM.mat, you cannot move the image files, and cannot move the  
        entire analysis to a system with a different byte-order (even if the  
        full file pathnames are retained. Further, the image scalefactors  
        will have been pre-scaled to effect any grand mean or global  
        scaling.  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_spm_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_spm_ui", *args, **kwargs)
