from spm._runtime import Runtime


def spm_fMRI_design(*args, **kwargs):
    """
      Assemble a design for fMRI studies  
        FORMAT [SPM] = spm_fMRI_design(SPM)  
         
        1st level  
       --------------------------------------------------------------------------  
        SPM.  
              xY: [1x1 struct] - data structure  
           nscan: [1xs double] - nscan(s) = number of scans in session s  
             xBF: [1x1 struct] - Basis function structure  
            Sess: [1xs struct] - Session structure array  
              xX: [1x1 struct] - Design matrix structure  
         
         
           2nd level  
           ----------------------------------------------------------------------  
           SPM.xY  
                  RT: - repetition time {seconds)  
         
           SPM.xBF  
                   T: - microtime resolution (number of time bins per scan)  
                  T0: - microtime onset (reference time bin, see slice timing)  
               UNITS: - 'scans'|'secs' - units in which onsets are specified  
            Volterra: - 1|2 - order of [Volterra] convolution  
                  dt: - length of time bin {seconds}  
                name: - name of basis set  
              length: - support of basis set {seconds}  
               order: - order of basis set  
                  bf: - basis set matrix  
         
           SPM.Sess(s)  
                   U: - Input structure array  
                   C: - User specified covariate structure  
                 row: - scan   indices for session s  
                 col: - effect indices for session s  
                  Fc: - F Contrast information for input-specific effects  
         
           SPM.xX  
                   X: - design matrix  
                  iH: - vector of H partition (indicator variables) indices  
                  iC: - vector of C partition (covariates)          indices  
                  iB: - vector of B partition (block effects)       indices  
                  iG: - vector of G partition (nuisance variables)  indices  
                name: - cellstr of names for design matrix columns  
         
         
               3rd level  
               ------------------------------------------------------------------  
               SPM.Sess(s).U  
                      dt: - time bin length {seconds}  
                    name: - {1 x j} cell of names for each input or cause  
                     ons: - (q x 1) onsets for q  trials {in UNITS}  
                     dur: - (q x 1) durations for trials {in UNITS}  
                       P: - Parameter structure  
                       u: - (t x j) inputs or stimulus function matrix  
                     pst: - (1 x k) peristimulus times (seconds)  
                    orth: - boolean: orthogonalise inputs?  
         
         
               SPM.Sess(s).C  
         
                       C: - [kx1 double] of user specified regressors  
                    name: - {1xk} cellstr of regressor names  
         
         
               SPM.Sess(s).Fc  
         
                       i: - indices pertaining to each input  
                    name: - names pertaining to each input  
                       p: - grouping of regressors per parameter  
         
         
                   4th level  
                   --------------------------------------------------------------  
                   SPM.Sess(s).U(i).P(p)  
         
                        name: - parameter name  
                           P: - (q x 1) parameter matrix  
                           h: - order of polynomial expansion (0 = none)  
                           i: - sub-indices of U(i).u for plotting  
         
         
        saves SPM.mat if save_SPM==1 (this is the default)  
       __________________________________________________________________________  
         
        spm_fMRI_design allows you to build design matrices with separable  
        session-specific partitions.  Each partition may be the same (in which  
        case it is only necessary to specify it once) or different.  Responses  
        can be either event- or epoch related, where the latter model prolonged  
        and possibly time-varying responses to state-related changes in  
        experimental conditions.  Event-related response are modelled in terms  
        of responses to instantaneous events.  Mathematically they are both  
        modelled by convolving a series of delta (stick) or box-car functions,  
        encoding the input or stimulus function. with a set of hemodynamic  
        basis functions.  
         
        spm_fMRI_design allows you to combine both event- and epoch-related  
        responses in the same model and/or regressor. You specify the number  
        of trial (event or epoch) types.  Epoch and event-related  
        responses are modeled in exactly the same way by first specifying their  
        onsets [in terms of onset times] and then their durations.  Events are  
        specified with a duration of 0.  If you enter a single number for the  
        durations it will be assumed that all trials conform to this duration.  
         
        Interactions or response modulations can enter at two levels.  Firstly  
        the stick function itself can be modulated by some parametric variate  
        (this can be time or some trial-specific variate like reaction time)  
        modeling the interaction between the trial and the variate or, secondly  
        interactions among the trials themselves can be modeled using a Volterra  
        series formulation that accommodates interactions over time (and therefore  
        within and between trial types).  The first sort of interaction is  
        specified by extra (modulated) stick functions in Sess(s).u.  If  
        a polynomial expansion of the specified variate is requested there will  
        be more than one column.  The corresponding name of the explanatory  
        variables in X.name is Sn(s) trial(u)xparam(p)^q*bf(i) for the qth  
        order expansion of the parameter convolved with the ith basis function  
        for the uth trial in the sth session.  If no parametric variate is  
        specified the name is simply Sn(s) trial(u)*bf(i).  Interactions among  
        and within trials enter as new trial types but do not have .pst or .ons  
        fields.  These interactions can be characterized later, in results, in  
        terms of the corresponding second order Volterra Kernels.  
         
        The design matrix is assembled on a much finer time scale (xBF.dt) than the  
        TR and is then sub-sampled at the acquisition times.  After down-sampling  
        the regressors for each input are othogonalised.  This ensures that  
        components due to the canonical hrf are not explained away by other basis  
        functions or parametric modulators.  
         
        Sess(s).ons(u) contains onset times in seconds or scans relative to the  
        timing of the first scan  
         
        Notes on spm_get_ons, spm_get_bf and spm_Volterra are included below  
        for convenience.  
         
                                  ----------------  
         
        spm_get_ons constructs a struct array containing sparse input  
        functions U(i).u specifying occurrence events or epochs (or both).  
        These are convolved with a basis set at a later stage to give  
        regressors that enter into the design matrix. Interactions of evoked  
        responses with some parameter (time or a specified  variate P) enter at  
        this stage as additional columns in U(u).u with each trial multiplied  
        by the [expansion of the] trial-specific parameter. If parametric  
        modulation is modeled, P(p).P contains the original variate and  
        P(p).name is its name. The 0th order expansion of this is simply the main  
        effect in the first column of U(u).u  
         
                                  ----------------  
         
        spm_get_bf prompts for basis functions to model hemodynamic  
        responses.  The basis functions returned are orthogonalized  
        and defined as a function of peri-stimulus time in time-bins.  
         
                                  ----------------  
         
        For first order expansions spm_Volterra simply convolves the causes  
        (e.g. stick functions) in U(u).u by the basis functions in Sess(s).bf  
        to create design matrix X.  For second order expansions new entries appear  
        in the design matrix that correspond to the hemodynamic interaction among the  
        original causes (if the events are sufficiently close in time).  
        The basis functions for these are two dimensional and are used to  
        assemble the second order kernel in spm_graph.m.  Second order effects  
        are computed for only the first column of U(u).u.  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fMRI_design.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fMRI_design", *args, **kwargs)
