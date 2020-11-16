# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:14:23 2019

@author: smorandv
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rm_ext_and_nan(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A dictionary of clean CTG called c_ctg
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    c_ctg = {}

    for feature in set(CTG_features.columns)-{extra_feature}:
        c_ctg[feature] = CTG_features.loc[pd.to_numeric(CTG_features.loc[:, feature], errors='coerce').notnull(), feature]

    # --------------------------------------------------------------------------
    return c_ctg


def nan2num_samp(CTG_features, extra_feature):
    """

    :param CTG_features: Pandas series of CTG features
    :param extra_feature: A feature to be removed
    :return: A pandas dataframe of the dictionary c_cdf containing the "clean" features
    """
    c_cdf = {}

    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    for feature in set(CTG_features.columns)-{extra_feature}:
        tmp = pd.to_numeric(CTG_features.loc[:,feature], errors='coerce')
        #tmp = CTG_features.loc[pd.to_numeric(CTG_features.loc[:,feature], errors='coerce').notnull(), feature]
        tmp[tmp.isnull()] = np.random.choice(tmp[tmp.notnull()], size=np.shape(tmp.isnull()))
        c_cdf[feature] = tmp

    # -------------------------------------------------------------------------
    return pd.DataFrame(c_cdf)


def sum_stat(c_feat):
    """

    :param c_feat: Output of nan2num_cdf
    :return: Summary statistics as a dicionary of dictionaries (called d_summary) as explained in the notebook
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------
    tmp = c_feat
    d_summary = {}
    sumst = tmp.describe()

    for feature in c_feat.columns:
        d_summary[feature] = {'min': sumst.loc['min', feature],
                        'max': sumst.loc['max', feature], 'Q1': sumst.loc['25%', feature],
                        'Q3': sumst.loc['75%', feature], 'mean': sumst.loc['mean', feature],
                        'median': sumst.loc['50%', feature]}


    # -------------------------------------------------------------------------
    return d_summary


def rm_outlier(c_feat, d_summary):  #c_Feat is DATAFrame
    """

    :param c_feat: Output of nan2num_cdf
    :param d_summary: Output of sum_stat
    :return: Dataframe of the dictionary c_no_outlier containing the feature with the outliers removed
    """
    c_no_outlier = {}
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    for feat in c_feat:
        interq = d_summary[feat]['Q3'] - d_summary[feat]['Q1']
        up = (c_feat[feat] < (d_summary[feat]['Q3']+1.5*interq))
        down = (c_feat[feat] > (d_summary[feat]['Q1']-1.5*interq))

        criterion = up & down

        c_no_outlier[feat] = c_feat.loc[criterion, feat]

    # -------------------------------------------------------------------------
    return pd.DataFrame(c_no_outlier)


def phys_prior(c_cdf, feature, thresh):  #c_cdf = c_samp
    """

    :param c_cdf: Output of nan2num_cdf
    :param feature: A string of your selected feature
    :param thresh: A numeric value of threshold
    :return: An array of the "filtered" feature called filt_feature
    """
    # ------------------ IMPLEMENT YOUR CODE HERE:-----------------------------
    filt_feature = c_cdf.loc[(c_cdf[feature]>thresh[0]) & (c_cdf[feature]<thresh[1]), feature]
    # -------------------------------------------------------------------------
    return filt_feature


def norm_standard(CTG_features, selected_feat=('LB', 'ASTV'), mode='none', flag=False):
    """

    :param CTG_features: Pandas series of CTG features
    :param selected_feat: A two elements tuple of strings of the features for comparison
    :param mode: A string determining the mode according to the notebook
    :param flag: A boolean determining whether or not plot a histogram
    :return: Dataframe of the normalized/standardazied features called nsd_res
    """
    x, y = selected_feat
    # ------------------ IMPLEMENT YOUR CODE HERE:------------------------------

    # -------------------------------------------------------------------------
    return pd.DataFrame(nsd_res)
