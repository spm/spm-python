from spm.__wrapper__ import Runtime


def spm_dcm_specify(*args, **kwargs):
    """
      Specify inputs of an fMRI DCM (wrapper around spm_dcm_specify_ui)  
        FORMAT DCM = spm_dcm_specify(SPM,xY,settings)  
         
        SPM      - SPM structure or its filename  
        xY       - (optional) VOI structures to be inserted into the DCM  
        settings - (optional) predefined configuration options  
         
        DCM      - DCM structure (see spm_dcm_ui)  
         
        Example for a task-based experiment:  
        -------------------------------------------------------------------------  
        n   = 3;    % number of regions  
        nu  = 2;    % number of inputs (experimental conditions)  
        TR  = 2;    % volume repetition time (seconds)  
        TE  = 0.03; % echo time (seconds)  
         
        % Experimental conditions to include from the SPM.  
        % To see the conditions' names, load your SPM.mat into the workspace and   
        % inspect SPM.Sess(s).U.name, where s is the session (run) number.  
        cond = struct();  
        cond(1).name    = 'Condition1'; % desired name for the condition  
        cond(1).spmname = {'c1','c2'};  % (optional) corresponding name(s) of   
                                        % conditions in the SPM.mat file, see  
                                        % SPM.Sess(s).U.name. If multiple names   
                                        % are provided then they will be combined   
                                        % by binarizing the regressors and performing   
                                        an 'OR' operation.  
         
        cond(2).name    = 'Condition2';  
        cond(2).spmname = {'c3','c4'};   
          
        % Connectivity matrices  
        a  = ones(n,n);  
        b  = zeros(n,n,nu);  
        c  = ones(n,nu);  
        d  = zeros(n,n,0);  
         
        s = struct();  
        s.name       = 'test';  
        s.cond       = cond;  
        s.delays     = repmat(TR/2, 1, n);  
        s.TE         = TE;  
        s.nonlinear  = false;  
        s.two_state  = false;  
        s.stochastic = false;  
        s.centre     = true;  
        s.induced    = 0;  
        s.a          = a;  
        s.b          = b;  
        s.c          = c;  
        s.d          = d;  
        DCM = spm_dcm_specify(SPM,xY,s);  
         
         
        Tips:   
        - You can either select which experimental conditions to include by using  
        the s.cond structure, as illustrated above, or by specifying a matrix  
        s.u(i,j), which sets whether to include regressor j of condition i from    
        the SPM design matrix. If there are no parametric regressors, then j   
        will always equal one.  
         
        - xY is a cell array of strings containing the filenames of the VOIs to   
        include.  
         
        Example for a resting state experiment:  
        -------------------------------------------------------------------------  
        n   = 2;    % number of regions  
        nu  = 1;    % number of inputs. For DCM for CSD we have one input: null  
        TR  = 2;    % volume repetition time (seconds)  
        TE  = 0.03; % echo time (seconds)  
          
        % Connectivity matrices  
        a  = ones(n,n);  
        b  = zeros(n,n,nu);  
        c  = zeros(n,nu);  
        d  = zeros(n,n,0);  
          
        % Specify DCM  
        s = struct();  
        s.name       = model_name;  
        s.u          = [];  
        s.delays     = repmat(TR/2, 1, n);  
        s.TE         = TE;  
        s.nonlinear  = false;  
        s.two_state  = false;  
        s.stochastic = false;  
        s.centre     = false;  
        s.induced    = 1;       % indicates DCM for CSD  
        s.a          = a;  
        s.b          = b;  
        s.c          = c;  
        s.d          = d;  
          
        DCM = spm_dcm_specify(SPM,xY,s);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_specify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_specify", *args, **kwargs)
