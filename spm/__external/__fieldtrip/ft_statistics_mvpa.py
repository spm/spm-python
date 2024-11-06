from spm.__wrapper__ import Runtime


def ft_statistics_mvpa(*args, **kwargs):
    """
      FT_STATISTICS_MVPA performs multivariate pattern classification or regression using  
        the MVPA-Light toolbox. The function supports cross-validation, searchlight  
        analysis, generalization, nested preprocessing, a variety of classification and  
        regression metrics, as well as statistical testing of these metrics. This function  
        should not be called directly, instead you should call the function that is  
        associated with the type of data on which you want to perform the test.  
         
        Use as  
          stat = ft_timelockstatistics(cfg, data1, data2, data3, ...)  
          stat = ft_freqstatistics    (cfg, data1, data2, data3, ...)  
          stat = ft_sourcestatistics  (cfg, data1, data2, data3, ...)  
         
        where the data is obtained from FT_TIMELOCKANALYSIS, FT_FREQANALYSIS or  
        FT_SOURCEANALYSIS respectively, or from FT_TIMELOCKGRANDAVERAGE,  
        FT_FREQGRANDAVERAGE or FT_SOURCEGRANDAVERAGE respectively  
        and with cfg.method = 'mvpa'  
         
        The configuration options that can be specified are:  
          cfg.features        = specifies the name or index of the dimension(s)  
                                that serve(s) as features for the classifier or  
                                regression model. Dimensions that are not  
                                samples or features act as search  
                                dimensions. For instance, assume the data is a  
                                3D array of size [samples x channels x time].  
                                If mvpa.features = 2, the channels serve as  
                                features. A classification is then performed for  
                                each time point (we call time a searchlight  
                                dimension). Conversely, if mvpa.features = 3, the  
                                time points serve as features. A classification  
                                is performed for each channel (channel is a  
                                searchlight dimension).  
                                If cfg.features = [], then all non-sample  
                                dimensions serve as searchlight dimensions.  
                                If the dimensions have names (i.e. cfg.dimord  
                                exists), then instead of numbers the feature can  
                                be specified as a string (e.g. 'chan').  
                                Default value is chosen based on the (optional)  
                                specification of the other searchlight options (see  
                                below). If nothing is defined, the default will be 'chan'/2.  
          cfg.generalize      = specifies the name or index of the dimensions  
                                that serves for generalization (if any). For  
                                instance, if the data is [samples x channels x  
                                time], and mvpa.generalize = 3, a time x time  
                                generalization is performed. If mvpa.generalize =  
                                2, a electrode x electrode generalization is  
                                performed. mvpa.generalize must refer to a  
                                searchlight dimension, therefore its value must  
                                be different from the value of mvpa.features.  
                                (default [])  
         
        The configuration contains a substruct cfg.mvpa that contains detailed  
        options for the MVPA. Possible fields  
          cfg.mvpa.classifier  = string specifying the classifier  
                                Available classifiers:  
                                'ensemble'     Ensemble of classifiers. Any of the other  
                                               classifiers can be used as a learner.  
                                'kernel_fda'   Kernel Fisher Discriminant Analysis  
                                'lda'          Regularized linear discriminant analysis  
                                               (LDA) (for two classes)  
                                'logreg'       Logistic regression  
                                'multiclass_lda' LDA for more than two classes  
                                'naive_bayes'  Naive Bayes  
                                'svm'          Support Vector Machine (SVM)  
                                More details on the classifiers: https://github.com/treder/MVPA-Light#classifiers-for-two-classes-  
                                Additionally, you can choose 'libsvm' or  
                                'liblinear' as a model. They provide interfaces  
                                for logistic regression, SVM, and Support Vector  
                                Regression. Note that they can act as either  
                                classifiers or regression models. An installation  
                                of LIBSVM or LIBLINEAR is required.  
          cfg.mvpa.model       = string specifying the regression model. If a  
                                regression model has been specified,  
                                cfg.mvpa.classifier should be empty (and vice  
                                versa). If neither a classifier nor regression  
                                model is specified, a LDA classifier is used by  
                                default.  
         
                                Available regression models:  
                                'ridge         Ridge regression  
                                'kernel_ridge' Kernel Ridge regression  
                                More details on the regression models: https://github.com/treder/MVPA-Light#regression-models-  
          cfg.mvpa.metric      = string, classification or regression metric, or  
                                cell array with multiple metrics.  
                                Classification metrics: accuracy auc confusion  
                                    dval f1 kappa precision recall tval  
                                Regression metrics: mae mse r_squared  
         
          cfg.mvpa.hyperparameter = struct, structure with hyperparameters for the  
                                classifier or regression model (see HYPERPARAMETERS below)  
          cfg.mvpa.feedback       = 'yes' or 'no', whether or not to print feedback on the console (default 'yes')  
         
        To obtain a realistic estimate of classification performance, cross-validation  
        is used. It is controlled by the following parameters:  
          cfg.mvpa.cv          = string, cross-validation type, either 'kfold', 'leaveout'  
                                'holdout', or 'predefined'. If 'none', no cross-validation is  
                                used and the model is tested on the training  
                                set. (default 'kfold')  
          cfg.mvpa.k           = number of folds in k-fold cross-validation (default 5)  
          cfg.mvpa.repeat      = number of times the cross-validation is repeated  
                                with new randomly assigned folds (default 5)  
          cfg.mvpa.p           = if cfg.cv is 'holdout', p is the fraction of test  
                                samples (default 0.1)  
          cfg.mvpa.stratify    = if 1, the class proportions are approximately  
                                preserved in each test fold (default 1)  
          cfg.mvpa.fold        = if cv='predefined', fold is a vector of length  
                                #samples that specifies the fold each sample belongs to  
         
        More information about each classifier is found in the documentation of  
        MVPA-Light (github.com/treder/MVPA-Light/).  
         
        HYPERPARAMETERS:  
        Each classifier comes with its own set of hyperparameters, such as  
        regularization parameters and the kernel. Hyperparameters can be set  
        using the cfg.mvpa.hyperparameter substruct. For instance, in LDA,  
        cfg.mvpa.hyperparameter = 'auto' sets the lambda regularization parameter.  
         
        The specification of the hyperparameters is found in the training function  
        for each model at github.com/treder/MVPA-Light/tree/master/model  
        If a hyperparameter is not specified, default values are used.  
         
        SEARCHLIGHT ANALYSIS:  
        Data dimensions that are not samples or features serve as 'search  
        dimensions'. For instance, if the data is [samples x chan x time]  
        and mvpa.features = 'time', then the channel dimension serves as search  
        dimension: a separate analysis is carried out for each channel. Instead  
        of considering each channel individually, a searchlight can be defined  
        such that each channel is used together with its neighbours. Neighbours  
        can be specified using the cfg.neighbours field:  
         
          cfg.neighbours   = neighbourhood structure, see FT_PREPARE_NEIGHBOURS  
          cfg.timwin       = integer, if MVPA is performed for each time point,  
                             timwin specfies the total size of the time window  
                             that is considered as features.  
                             Example: for cfg.timwin = 3 a given time point is considered  
                             together with the immediately preceding and following  
                             time points. Increasing timwin typially  
                             leads to smoother results along the time axis.  
          cfg.freqwin      = integer, acts like cfg.timwin but across frequencies  
         
        This returns:  
          stat.metric = this contains the requested metric  
         
        See also FT_TIMELOCKSTATISTICS, FT_FREQSTATISTICS, FT_SOURCESTATISTICS,  
        FT_STATISTICS_ANALYTIC, FT_STATISTICS_STATS, FT_STATISTICS_MONTECARLO, FT_STATISTICS_CROSSVALIDATE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_statistics_mvpa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_statistics_mvpa", *args, **kwargs)
